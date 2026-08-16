#!/usr/bin/env python3
"""Repair typing semantics in Sage stubs without weakening their mathematics.

This pass addresses diagnostics that reveal a malformed type model rather than
an unknown mathematical object: incorrect static/class method receivers,
explicit self annotations, free TypeVars, bare containers, untyped class
attributes, and Liskov-incompatible parameter narrowing.  Base/subclass
signatures are reconciled by expressing the union of values that the runtime
actually accepts, never by replacing a type with ``Any``.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
STUB_ROOT = ROOT / "sage-stubs"
SOURCE_ROOT = ROOT / "sage-src" / "src" / "sage"
ERASED = {"Any", "object", "_SageObject"}
BARE_GENERICS = {"list", "tuple", "dict", "set", "frozenset", "type"}

IMPORTS: dict[str, tuple[str, str]] = {
    "Element": ("sage.structure.element", "Element"),
    "Parent": ("sage.structure.parent", "Parent"),
    "SageObject": ("sage.structure.sage_object", "SageObject"),
    "Hashable": ("collections.abc", "Hashable"),
    "Iterable": ("collections.abc", "Iterable"),
    "Iterator": ("collections.abc", "Iterator"),
    "Mapping": ("collections.abc", "Mapping"),
    "Sequence": ("collections.abc", "Sequence"),
    "Self": ("typing", "Self"),
    "TypeVar": ("typing", "TypeVar"),
}
BUILTINS = {
    "None", "bool", "int", "float", "complex", "str", "bytes", "bytearray",
    "memoryview", "list", "tuple", "dict", "set", "frozenset", "type",
    "slice", "range",
}
PROTOCOL_OBJECT_PARAMETERS = {"__eq__", "__ne__", "__contains__"}


@dataclass
class ClassRecord:
    module: str
    node: ast.ClassDef
    path: Path


def parse(path: Path) -> ast.Module | None:
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeError):
        return None


def dotted(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = dotted(node.value)
        return f"{base}.{node.attr}" if base else node.attr
    return None


def names(node: ast.expr | None) -> set[str]:
    if node is None:
        return set()
    result: set[str] = set()
    for child in ast.walk(node):
        value = dotted(child)
        if value:
            result.add(value)
            result.add(value.rsplit(".", 1)[-1])
    return result


def text(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    try:
        return ast.unparse(node)
    except Exception:
        return None


def ann(value: str) -> ast.expr:
    return ast.parse(value, mode="eval").body


def erased(node: ast.expr | None) -> bool:
    return node is None or bool(names(node) & ERASED)


def module_name(path: Path) -> str:
    rel = path.relative_to(STUB_ROOT).with_suffix("")
    return "sage." + ".".join(rel.parts)


def source_path(path: Path) -> Path | None:
    rel = path.relative_to(STUB_ROOT).with_suffix("")
    for suffix in (".py", ".pyx"):
        candidate = (SOURCE_ROOT / rel).with_suffix(suffix)
        if candidate.exists():
            return candidate
    return None


def source_imports(tree: ast.Module | None) -> dict[str, tuple[str, str]]:
    result: dict[str, tuple[str, str]] = {}
    if tree is None:
        return result
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            module = "." * node.level + node.module
            for alias in node.names:
                result[alias.asname or alias.name] = (module, alias.name)
    return result


def functions(node: ast.Module | ast.ClassDef) -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    return {
        child.name: child
        for child in node.body
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def classes(tree: ast.Module | None) -> dict[str, ast.ClassDef]:
    if tree is None:
        return {}
    return {node.name: node for node in tree.body if isinstance(node, ast.ClassDef)}


def decorators(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str]:
    return {(dotted(node) or "").rsplit(".", 1)[-1] for node in fn.decorator_list}


def source_kind(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> str:
    decs = decorators(fn)
    if "staticmethod" in decs:
        return "static"
    if "classmethod" in decs or fn.name == "__new__":
        return "class"
    return "instance"


def direct_returns(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> list[ast.expr | None]:
    result: list[ast.expr | None] = []

    class Visitor(ast.NodeVisitor):
        def visit_Return(self, node: ast.Return) -> None:
            result.append(node.value)
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            if node is fn:
                self.generic_visit(node)
        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            if node is fn:
                self.generic_visit(node)
        def visit_Lambda(self, node: ast.Lambda) -> None:
            return

    Visitor().visit(fn)
    return result


def returns_self(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    values = direct_returns(fn)
    return bool(values) and all(isinstance(value, ast.Name) and value.id == "self" for value in values)


def constructed_class(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    names_found: set[str] = set()
    for value in direct_returns(fn):
        if isinstance(value, ast.Call):
            called = (dotted(value.func) or "").rsplit(".", 1)[-1]
            if called and called[:1].isupper():
                names_found.add(called)
    return next(iter(names_found)) if len(names_found) == 1 else None


def infer_value(node: ast.expr | None, env: dict[str, str]) -> str | None:
    if node is None:
        return None
    if isinstance(node, ast.Constant):
        if node.value is None:
            return "None"
        if isinstance(node.value, bool):
            return "bool"
        if isinstance(node.value, int):
            return "int"
        if isinstance(node.value, float):
            return "float"
        if isinstance(node.value, complex):
            return "complex"
        if isinstance(node.value, str):
            return "str"
        if isinstance(node.value, bytes):
            return "bytes"
    if isinstance(node, ast.Name):
        return env.get(node.id)
    if isinstance(node, ast.List):
        values = {infer_value(item, env) for item in node.elts}
        values.discard(None)
        return f"list[{next(iter(values))}]" if len(values) == 1 else None
    if isinstance(node, ast.Set):
        values = {infer_value(item, env) for item in node.elts}
        values.discard(None)
        return f"set[{next(iter(values))}]" if len(values) == 1 else None
    if isinstance(node, ast.Tuple):
        values = [infer_value(item, env) for item in node.elts]
        return "tuple[" + ", ".join(values) + "]" if values and all(values) else None
    if isinstance(node, ast.Dict):
        keys = {infer_value(item, env) for item in node.keys if item}
        values = {infer_value(item, env) for item in node.values}
        keys.discard(None)
        values.discard(None)
        return f"dict[{next(iter(keys))}, {next(iter(values))}]" if len(keys) == len(values) == 1 else None
    if isinstance(node, ast.Call):
        called = (dotted(node.func) or "").rsplit(".", 1)[-1]
        if called in {"bool", "int", "float", "complex", "str", "bytes"}:
            return called
        if called in {"list", "set", "frozenset", "tuple"} and node.args:
            source = infer_value(node.args[0], env)
            match = re.fullmatch(r"(?:Iterable|Iterator|Sequence|list|set|frozenset|tuple)\[(.+?)(?:, \.\.\.)?\]", source or "")
            if match:
                item = match.group(1)
                return f"tuple[{item}, ...]" if called == "tuple" else f"{called}[{item}]"
        if called in {"Integer", "ZZ"}:
            return "Integer"
        if called in {"matrix", "Matrix"}:
            return "Matrix"
        if called in {"vector", "FreeModuleElement"}:
            return "FreeModuleElement"
        if called and called[:1].isupper():
            return called
    return None


def union(left: str, right: str) -> str:
    parts: list[str] = []
    for value in (left, right):
        for piece in value.split(" | "):
            piece = piece.strip()
            if piece and piece not in parts:
                parts.append(piece)
    return " | ".join(parts)


def typevar_bounds(tree: ast.Module) -> dict[str, str | None]:
    result: dict[str, str | None] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        if not isinstance(node.value, ast.Call) or (dotted(node.value.func) or "").rsplit(".", 1)[-1] != "TypeVar":
            continue
        bound = None
        for keyword in node.value.keywords:
            if keyword.arg == "bound":
                bound = text(keyword.value)
        result[node.targets[0].id] = bound
    return result


class Corpus:
    def __init__(self) -> None:
        self.by_name: dict[str, list[ClassRecord]] = defaultdict(list)

    @classmethod
    def build(cls) -> "Corpus":
        corpus = cls()
        for path in STUB_ROOT.rglob("*.pyi"):
            tree = parse(path)
            if tree is None:
                continue
            module = module_name(path)
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    corpus.by_name[node.name].append(ClassRecord(module, node, path))
        return corpus

    def resolve_base(self, name: str, current_module: str) -> ClassRecord | None:
        short = name.rsplit(".", 1)[-1]
        candidates = self.by_name.get(short, [])
        if len(candidates) == 1:
            return candidates[0]
        local = [candidate for candidate in candidates if candidate.module == current_module]
        return local[0] if len(local) == 1 else None


class Repairer:
    def __init__(self, path: Path, source: Path | None, corpus: Corpus) -> None:
        self.path = path
        self.source_path = source
        self.corpus = corpus
        self.stub = parse(path)
        self.source = parse(source) if source and source.suffix == ".py" else None
        self.import_map = source_imports(self.source)
        self.module = module_name(path)
        self.required: dict[str, tuple[str, str]] = {}
        self.changed = False
        self.bounds = typevar_bounds(self.stub) if self.stub else {}

    def require_type(self, value: str) -> None:
        try:
            expression = ann(value)
        except SyntaxError:
            return
        for name in names(expression):
            short = name.rsplit(".", 1)[-1]
            if short in BUILTINS or short.startswith("_T"):
                continue
            if short in IMPORTS:
                self.required[short] = IMPORTS[short]
            elif short in self.import_map:
                self.required[short] = self.import_map[short]
            else:
                records = self.corpus.by_name.get(short, [])
                modules = {record.module for record in records}
                if len(modules) == 1 and next(iter(modules)) != self.module:
                    self.required[short] = (next(iter(modules)), short)

    def align_receiver(self, source_fn: ast.FunctionDef | ast.AsyncFunctionDef, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        kind = source_kind(source_fn)
        source_decs = decorators(source_fn)
        stub_decs = decorators(stub_fn)
        wanted = {name for name in source_decs if name in {"staticmethod", "classmethod", "property", "abstractmethod"}}
        preserved = [node for node in stub_fn.decorator_list if (dotted(node) or "").rsplit(".", 1)[-1] not in {"staticmethod", "classmethod", "property", "abstractmethod"}]
        if stub_decs & {"staticmethod", "classmethod", "property", "abstractmethod"} != wanted:
            stub_fn.decorator_list = [*preserved, *(ast.Name(id=name) for name in sorted(wanted))]
            self.changed = True
        args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
        if kind == "static":
            # Source is authoritative about whether a parameter merely happens
            # to be named self/cls in a static method.
            source_args = [*source_fn.args.posonlyargs, *source_fn.args.args]
            if args and args[0].arg in {"self", "cls"} and (not source_args or source_args[0].arg not in {"self", "cls"}):
                target = stub_fn.args.posonlyargs if stub_fn.args.posonlyargs else stub_fn.args.args
                target.pop(0)
                self.changed = True
        else:
            receiver_name = "cls" if kind == "class" else "self"
            args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
            if not args:
                stub_fn.args.args.insert(0, ast.arg(arg=receiver_name))
                self.changed = True
            else:
                receiver = args[0]
                if receiver.arg != receiver_name:
                    receiver.arg = receiver_name
                    self.changed = True
                if receiver.annotation is not None:
                    receiver.annotation = None
                    self.changed = True

    def repair_free_typevar(self, source_fn: ast.FunctionDef | ast.AsyncFunctionDef | None, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef, owner: str | None) -> None:
        return_names = names(stub_fn.returns)
        free = [name for name in return_names if name in self.bounds]
        if not free:
            return
        argument_names: set[str] = set()
        for arg in [*stub_fn.args.posonlyargs, *stub_fn.args.args, *stub_fn.args.kwonlyargs]:
            argument_names |= names(arg.annotation)
        if stub_fn.args.vararg:
            argument_names |= names(stub_fn.args.vararg.annotation)
        if stub_fn.args.kwarg:
            argument_names |= names(stub_fn.args.kwarg.annotation)
        for variable in free:
            if variable in argument_names:
                continue
            replacement: str | None = None
            if source_fn and returns_self(source_fn):
                replacement = "Self"
            if source_fn and not replacement:
                replacement = constructed_class(source_fn)
            if not replacement:
                replacement = self.bounds.get(variable)
            if not replacement and owner:
                replacement = owner
            if replacement:
                current = text(stub_fn.returns) or variable
                stub_fn.returns = ann(re.sub(rf"\b{re.escape(variable)}\b", replacement, current))
                self.require_type(replacement)
                self.changed = True

    def repair_bare_generic(self, source_fn: ast.FunctionDef | ast.AsyncFunctionDef | None, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        env = {
            arg.arg: text(arg.annotation) or ""
            for arg in [*stub_fn.args.posonlyargs, *stub_fn.args.args, *stub_fn.args.kwonlyargs]
            if not erased(arg.annotation)
        }
        nodes: list[tuple[ast.arg | None, ast.expr | None]] = [(arg, arg.annotation) for arg in [*stub_fn.args.posonlyargs, *stub_fn.args.args, *stub_fn.args.kwonlyargs]]
        nodes.append((None, stub_fn.returns))
        for argument, annotation_node in nodes:
            if not isinstance(annotation_node, ast.Name) or annotation_node.id not in BARE_GENERICS:
                continue
            base = annotation_node.id
            inferred: str | None = None
            if source_fn and argument is None:
                values = [infer_value(value, env) for value in direct_returns(source_fn)]
                values = [value for value in values if value]
                if len(set(values)) == 1:
                    inferred = values[0]
            if not inferred:
                inferred = {
                    "list": "list[Element]",
                    "tuple": "tuple[Element, ...]",
                    "dict": "dict[Hashable, Element]",
                    "set": "set[Element]",
                    "frozenset": "frozenset[Element]",
                    "type": "type[SageObject]",
                }[base]
            if argument is None:
                stub_fn.returns = ann(inferred)
            else:
                argument.annotation = ann(inferred)
            self.require_type(inferred)
            self.changed = True

    def repair_protocol_dunders(self, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        if stub_fn.name not in PROTOCOL_OBJECT_PARAMETERS:
            return
        args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
        value_args = args[1:] if args and args[0].arg in {"self", "cls"} else args
        if value_args and text(value_args[0].annotation) != "object":
            value_args[0].annotation = ann("object")
            self.changed = True
        if stub_fn.name in {"__eq__", "__ne__", "__contains__"} and text(stub_fn.returns) != "bool":
            stub_fn.returns = ann("bool")
            self.changed = True

    def repair_attributes(self, source_class: ast.ClassDef, stub_class: ast.ClassDef) -> None:
        init = functions(source_class).get("__init__")
        if not init:
            return
        stub_init = functions(stub_class).get("__init__")
        env: dict[str, str] = {}
        if stub_init:
            env.update(
                (arg.arg, text(arg.annotation) or "")
                for arg in [*stub_init.args.posonlyargs, *stub_init.args.args, *stub_init.args.kwonlyargs]
                if not erased(arg.annotation)
            )
        inferred: dict[str, str] = {}
        for node in ast.walk(init):
            if isinstance(node, ast.Assign):
                value_type = infer_value(node.value, env)
                if not value_type:
                    continue
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                        inferred[target.attr] = value_type
            elif isinstance(node, ast.AnnAssign):
                target = node.target
                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                    value_type = text(node.annotation) or infer_value(node.value, env)
                    if value_type:
                        inferred[target.attr] = value_type
        existing = {
            node.target.id: node
            for node in stub_class.body
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
        }
        for name, value_type in inferred.items():
            if name.startswith("_"):
                continue
            node = existing.get(name)
            if node and erased(node.annotation):
                node.annotation = ann(value_type)
                self.require_type(value_type)
                self.changed = True
            elif not node:
                stub_class.body.insert(0, ast.AnnAssign(target=ast.Name(id=name, ctx=ast.Store()), annotation=ann(value_type), value=None, simple=1))
                self.require_type(value_type)
                self.changed = True

    def base_methods(self, stub_class: ast.ClassDef) -> list[dict[str, ast.FunctionDef | ast.AsyncFunctionDef]]:
        result: list[dict[str, ast.FunctionDef | ast.AsyncFunctionDef]] = []
        for base in stub_class.bases:
            name = text(base) or ""
            if "[" in name:
                name = name.split("[", 1)[0]
            record = self.corpus.resolve_base(name, self.module)
            if record:
                result.append(functions(record.node))
        return result

    def reconcile_override(self, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef, bases: list[dict[str, ast.FunctionDef | ast.AsyncFunctionDef]]) -> None:
        base_functions = [mapping[stub_fn.name] for mapping in bases if stub_fn.name in mapping]
        if not base_functions:
            return
        sub_args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
        if sub_args and sub_args[0].arg in {"self", "cls"}:
            sub_args = sub_args[1:]
        for base_fn in base_functions:
            base_args = [*base_fn.args.posonlyargs, *base_fn.args.args]
            if base_args and base_args[0].arg in {"self", "cls"}:
                base_args = base_args[1:]
            for sub_arg, base_arg in zip(sub_args, base_args):
                sub_type = text(sub_arg.annotation)
                base_type = text(base_arg.annotation)
                if not sub_type or not base_type or sub_type == base_type:
                    continue
                if erased(base_arg.annotation):
                    continue
                widened = union(sub_type, base_type)
                if widened != sub_type:
                    sub_arg.annotation = ann(widened)
                    self.require_type(widened)
                    self.changed = True

    def repair_function(self, source_fn: ast.FunctionDef | ast.AsyncFunctionDef | None, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef, owner: str | None, bases: list[dict[str, ast.FunctionDef | ast.AsyncFunctionDef]]) -> None:
        if source_fn:
            self.align_receiver(source_fn, stub_fn)
            if source_fn.returns is not None and not erased(source_fn.returns):
                source_return = text(source_fn.returns)
                if source_return and text(stub_fn.returns) != source_return:
                    stub_fn.returns = ann(source_return)
                    self.require_type(source_return)
                    self.changed = True
        else:
            args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
            if args and args[0].arg in {"self", "cls"} and args[0].annotation is not None:
                args[0].annotation = None
                self.changed = True
        self.repair_protocol_dunders(stub_fn)
        self.repair_free_typevar(source_fn, stub_fn, owner)
        self.repair_bare_generic(source_fn, stub_fn)
        self.reconcile_override(stub_fn, bases)
        if stub_fn.name == "__new__" and owner and text(stub_fn.returns) in {"Self", "object", None}:
            stub_fn.returns = ann(owner)
            self.changed = True

    def install_imports(self) -> None:
        assert self.stub is not None
        existing: set[str] = set()
        import_nodes: dict[tuple[str, int], ast.ImportFrom] = {}
        for node in self.stub.body:
            if isinstance(node, ast.ImportFrom) and node.module:
                import_nodes[(node.module, node.level)] = node
                existing.update(alias.asname or alias.name for alias in node.names)
            elif isinstance(node, ast.Import):
                existing.update(alias.asname or alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                existing.add(node.name)
        position = 0
        if self.stub.body and isinstance(self.stub.body[0], ast.Expr) and isinstance(self.stub.body[0].value, ast.Constant) and isinstance(self.stub.body[0].value.value, str):
            position = 1
        while position < len(self.stub.body) and isinstance(self.stub.body[position], ast.ImportFrom) and self.stub.body[position].module == "__future__":
            position += 1
        additions: list[ast.ImportFrom] = []
        for local, (module, original) in sorted(self.required.items()):
            if local in existing:
                continue
            level = len(module) - len(module.lstrip("."))
            clean = module.lstrip(".")
            key = (clean, level)
            alias = ast.alias(name=original, asname=local if local != original else None)
            if key in import_nodes:
                import_nodes[key].names.append(alias)
            else:
                node = ast.ImportFrom(module=clean, names=[alias], level=level)
                import_nodes[key] = node
                additions.append(node)
            existing.add(local)
        if additions:
            self.stub.body[position:position] = additions
            self.changed = True

    def remove_stale_suppressions(self) -> None:
        # Suppressions are removed only after structural repairs have been
        # applied.  Subsequent mypy/basedpyright runs remain authoritative.
        original = self.path.read_text(encoding="utf-8")
        cleaned = "\n".join(
            line for line in original.splitlines()
            if not re.match(r"^\s*#\s*(mypy:|pyright:|type:\s*ignore|noqa)", line)
        ) + "\n"
        if cleaned != original:
            self.path.write_text(cleaned, encoding="utf-8")
            reparsed = parse(self.path)
            if reparsed is not None:
                self.stub = reparsed
                self.changed = True

    def run(self) -> bool:
        if self.stub is None:
            return False
        source_class_map = classes(self.source)
        stub_class_map = classes(self.stub)
        source_function_map = functions(self.source) if self.source else {}
        stub_function_map = functions(self.stub)
        for name, stub_fn in stub_function_map.items():
            self.repair_function(source_function_map.get(name), stub_fn, None, [])
        for name, stub_class in stub_class_map.items():
            source_class = source_class_map.get(name)
            if source_class:
                self.repair_attributes(source_class, stub_class)
            source_methods = functions(source_class) if source_class else {}
            bases = self.base_methods(stub_class)
            for method_name, stub_fn in functions(stub_class).items():
                self.repair_function(source_methods.get(method_name), stub_fn, name, bases)
        self.install_imports()
        if not self.changed:
            return False
        ast.fix_missing_locations(self.stub)
        self.path.write_text(ast.unparse(self.stub).rstrip() + "\n", encoding="utf-8")
        return True


def load_paths(path: Path | None) -> list[Path]:
    if path is None:
        return sorted(STUB_ROOT.rglob("*.pyi"))
    result: list[Path] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        candidate = Path(raw)
        if not candidate.is_absolute():
            candidate = ROOT / candidate
        if candidate.exists() and candidate.suffix == ".pyi" and STUB_ROOT in candidate.parents:
            result.append(candidate)
    return sorted(set(result))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--files-from", type=Path)
    args = parser.parse_args()
    if not STUB_ROOT.is_dir() or not SOURCE_ROOT.is_dir():
        print("stub tree or pinned Sage source is unavailable", file=sys.stderr)
        return 2
    corpus = Corpus.build()
    changed: list[Path] = []
    for path in load_paths(args.files_from):
        repairer = Repairer(path, source_path(path), corpus)
        if repairer.run():
            changed.append(path)
    print(f"typing-semantic repair: {len(changed)} file(s) changed")
    for path in changed[:350]:
        print(path.relative_to(ROOT))
    if len(changed) > 350:
        print(f"... {len(changed) - 350} additional file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
