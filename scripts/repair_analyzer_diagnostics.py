#!/usr/bin/env python3
"""Repair actionable mypy/basedpyright diagnostics using Sage source semantics.

The input reports identify malformed typing constructs.  This script handles
only diagnostics with a source-grounded repair: receiver/decorator mismatch,
free TypeVars, bare generics, missing class-attribute annotations, shadowed
builtin type names, and contravariant override domains.  Diagnostics requiring
new mathematical knowledge remain untouched and visible.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUB_ROOT = ROOT / "sage-stubs"
SOURCE_ROOT = ROOT / "sage-src" / "src" / "sage"

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
    "TypeAlias": ("typing", "TypeAlias"),
}
BARE_REPLACEMENTS = {
    "list": "list[Element]",
    "tuple": "tuple[Element, ...]",
    "dict": "dict[Hashable, Element]",
    "set": "set[Element]",
    "frozenset": "frozenset[Element]",
    "type": "type[SageObject]",
    "Parent": "Parent[Element]",
    "Sequence": "Sequence[Element]",
    "Mapping": "Mapping[Hashable, Element]",
    "Iterable": "Iterable[Element]",
    "Iterator": "Iterator[Element]",
}
SHADOW_ALIASES = {
    "list": "_BuiltinList",
    "tuple": "_BuiltinTuple",
    "dict": "_BuiltinDict",
    "set": "_BuiltinSet",
    "frozenset": "_BuiltinFrozenSet",
    "str": "_BuiltinStr",
    "bytes": "_BuiltinBytes",
    "int": "_BuiltinInt",
    "float": "_BuiltinFloat",
    "complex": "_BuiltinComplex",
    "bool": "_BuiltinBool",
    "type": "_BuiltinType",
}


@dataclass(frozen=True)
class Diagnostic:
    path: Path
    line: int
    column: int
    message: str
    rule: str | None


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


def text(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    try:
        return ast.unparse(node)
    except Exception:
        return None


def ann(value: str) -> ast.expr:
    return ast.parse(value, mode="eval").body


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


def parse_mypy(path: Path) -> list[Diagnostic]:
    pattern = re.compile(r"^(?P<path>.+?\.pyi):(?P<line>\d+):(?P<column>\d+): error: (?P<message>.*?)(?:\s+\[(?P<rule>[^]]+)\])?$")
    result: list[Diagnostic] = []
    if not path.exists():
        return result
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = pattern.match(raw)
        if not match:
            continue
        candidate = Path(match.group("path"))
        if not candidate.is_absolute():
            candidate = ROOT / candidate
        if candidate.exists() and STUB_ROOT in candidate.parents:
            result.append(Diagnostic(candidate, int(match.group("line")), int(match.group("column")), match.group("message"), match.group("rule")))
    return result


def parse_pyright(path: Path) -> list[Diagnostic]:
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    result: list[Diagnostic] = []
    for item in data.get("generalDiagnostics", []):
        candidate = Path(item.get("file", ""))
        if not candidate.is_absolute():
            candidate = ROOT / candidate
        if not candidate.exists() or STUB_ROOT not in candidate.parents:
            continue
        start = item.get("range", {}).get("start", {})
        result.append(
            Diagnostic(
                candidate,
                int(start.get("line", 0)) + 1,
                int(start.get("character", 0)) + 1,
                str(item.get("message", "")),
                str(item.get("rule")) if item.get("rule") else None,
            )
        )
    return result


def containing(tree: ast.Module, line: int, kinds: tuple[type[ast.AST], ...]) -> ast.AST | None:
    nodes = [
        node for node in ast.walk(tree)
        if isinstance(node, kinds)
        and getattr(node, "lineno", 0) <= line <= getattr(node, "end_lineno", getattr(node, "lineno", 0))
    ]
    return min(nodes, key=lambda node: getattr(node, "end_lineno", node.lineno) - node.lineno) if nodes else None


def functions(node: ast.Module | ast.ClassDef | None) -> dict[str, ast.FunctionDef | ast.AsyncFunctionDef]:
    if node is None:
        return {}
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
    return {(dotted(item) or "").rsplit(".", 1)[-1] for item in fn.decorator_list}


def source_function(source: ast.Module | None, stub_tree: ast.Module, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    if source is None:
        return None
    stub_class = containing(stub_tree, stub_fn.lineno, (ast.ClassDef,))
    if isinstance(stub_class, ast.ClassDef):
        source_class = classes(source).get(stub_class.name)
        return functions(source_class).get(stub_fn.name)
    return functions(source).get(stub_fn.name)


def infer_assignment(value: ast.expr | None, env: dict[str, str]) -> str | None:
    if value is None:
        return None
    if isinstance(value, ast.Constant):
        if value.value is None:
            return "None"
        if isinstance(value.value, bool):
            return "bool"
        if isinstance(value.value, int):
            return "int"
        if isinstance(value.value, float):
            return "float"
        if isinstance(value.value, complex):
            return "complex"
        if isinstance(value.value, str):
            return "str"
        if isinstance(value.value, bytes):
            return "bytes"
    if isinstance(value, ast.Name):
        return env.get(value.id)
    if isinstance(value, ast.List):
        values = {infer_assignment(item, env) for item in value.elts}
        values.discard(None)
        return f"list[{next(iter(values))}]" if len(values) == 1 else None
    if isinstance(value, ast.Tuple):
        values = [infer_assignment(item, env) for item in value.elts]
        return "tuple[" + ", ".join(values) + "]" if values and all(values) else None
    if isinstance(value, ast.Dict):
        keys = {infer_assignment(item, env) for item in value.keys if item}
        values = {infer_assignment(item, env) for item in value.values}
        keys.discard(None)
        values.discard(None)
        return f"dict[{next(iter(keys))}, {next(iter(values))}]" if len(keys) == len(values) == 1 else None
    if isinstance(value, ast.Call):
        called = (dotted(value.func) or "").rsplit(".", 1)[-1]
        if called in {"bool", "int", "float", "complex", "str", "bytes"}:
            return called
        if called in {"Integer", "ZZ"}:
            return "Integer"
        if called and called[:1].isupper():
            return called
    return None


def merge_types(left: str, right: str) -> str:
    parts: list[str] = []
    for value in (left, right):
        for part in value.split(" | "):
            part = part.strip()
            if part and part not in parts:
                parts.append(part)
    return " | ".join(parts)


class FileEditor:
    def __init__(self, path: Path, diagnostics: list[Diagnostic]) -> None:
        self.path = path
        self.diagnostics = diagnostics
        self.tree = parse(path)
        source = source_path(path)
        self.source = parse(source) if source and source.suffix == ".py" else None
        self.required: dict[str, tuple[str, str]] = {}
        self.aliases: dict[str, str] = {}
        self.changed = False

    def require(self, type_text: str) -> None:
        try:
            expression = ann(type_text)
        except SyntaxError:
            return
        for node in ast.walk(expression):
            name = dotted(node)
            if not name:
                continue
            short = name.rsplit(".", 1)[-1]
            if short in IMPORTS:
                self.required[short] = IMPORTS[short]

    def align_receiver(self, stub_fn: ast.FunctionDef | ast.AsyncFunctionDef, source_fn: ast.FunctionDef | ast.AsyncFunctionDef | None) -> None:
        if source_fn is None:
            args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
            if args and args[0].arg in {"self", "cls"} and args[0].annotation is not None:
                args[0].annotation = None
                self.changed = True
            return
        source_decs = decorators(source_fn)
        kind = "static" if "staticmethod" in source_decs else "class" if "classmethod" in source_decs or source_fn.name == "__new__" else "instance"
        managed = {"staticmethod", "classmethod", "property", "abstractmethod"}
        wanted = source_decs & managed
        current = decorators(stub_fn) & managed
        if current != wanted:
            stub_fn.decorator_list = [
                node for node in stub_fn.decorator_list
                if (dotted(node) or "").rsplit(".", 1)[-1] not in managed
            ] + [ast.Name(id=name) for name in sorted(wanted)]
            self.changed = True
        args = [*stub_fn.args.posonlyargs, *stub_fn.args.args]
        if kind == "static":
            source_args = [*source_fn.args.posonlyargs, *source_fn.args.args]
            if args and args[0].arg in {"self", "cls"} and (not source_args or source_args[0].arg not in {"self", "cls"}):
                target = stub_fn.args.posonlyargs if stub_fn.args.posonlyargs else stub_fn.args.args
                target.pop(0)
                self.changed = True
        else:
            wanted_name = "cls" if kind == "class" else "self"
            if not args:
                stub_fn.args.args.insert(0, ast.arg(arg=wanted_name))
                self.changed = True
            else:
                if args[0].arg != wanted_name:
                    args[0].arg = wanted_name
                    self.changed = True
                if args[0].annotation is not None:
                    args[0].annotation = None
                    self.changed = True

    def repair_line(self, diagnostic: Diagnostic) -> None:
        assert self.tree is not None
        message = diagnostic.message
        fn = containing(self.tree, diagnostic.line, (ast.FunctionDef, ast.AsyncFunctionDef))
        source_fn = source_function(self.source, self.tree, fn) if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) else None
        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and (
            "explicit self annotation" in message
            or "Static methods should not take" in message
            or "self parameter missing" in message
            or diagnostic.rule in {"reportSelfClsParameterName", "reportGeneralTypeIssues"}
        ):
            self.align_receiver(fn, source_fn)

        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and (
            "Missing type arguments for generic type" in message
            or "Expected type arguments for generic class" in message
            or diagnostic.rule == "reportMissingTypeArgument"
        ):
            target = containing(self.tree, diagnostic.line, (ast.arg, ast.FunctionDef, ast.AsyncFunctionDef, ast.AnnAssign))
            annotation_node = None
            setter = None
            if isinstance(target, ast.arg):
                annotation_node = target.annotation
                setter = lambda value: setattr(target, "annotation", value)
            elif isinstance(target, (ast.FunctionDef, ast.AsyncFunctionDef)):
                annotation_node = target.returns
                setter = lambda value: setattr(target, "returns", value)
            elif isinstance(target, ast.AnnAssign):
                annotation_node = target.annotation
                setter = lambda value: setattr(target, "annotation", value)
            if isinstance(annotation_node, ast.Name) and annotation_node.id in BARE_REPLACEMENTS and setter:
                replacement = BARE_REPLACEMENTS[annotation_node.id]
                setter(ann(replacement))
                self.require(replacement)
                self.changed = True

        if "Type annotation for attribute" in message or diagnostic.rule == "reportUnannotatedClassAttribute":
            class_node = containing(self.tree, diagnostic.line, (ast.ClassDef,))
            source_class = classes(self.source).get(class_node.name) if isinstance(class_node, ast.ClassDef) and self.source else None
            if isinstance(class_node, ast.ClassDef) and source_class:
                attr_match = re.search(r"attribute [`\"']?([A-Za-z_]\w*)", message)
                attr_name = attr_match.group(1) if attr_match else None
                source_init = functions(source_class).get("__init__")
                stub_init = functions(class_node).get("__init__")
                env = {
                    arg.arg: text(arg.annotation) or ""
                    for arg in [*stub_init.args.posonlyargs, *stub_init.args.args, *stub_init.args.kwonlyargs]
                    if stub_init and arg.annotation is not None
                } if stub_init else {}
                if attr_name and source_init:
                    inferred = None
                    for node in ast.walk(source_init):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self" and target.attr == attr_name:
                                    inferred = infer_assignment(node.value, env)
                        elif isinstance(node, ast.AnnAssign):
                            target = node.target
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self" and target.attr == attr_name:
                                inferred = text(node.annotation) or infer_assignment(node.value, env)
                    if inferred:
                        class_node.body.insert(0, ast.AnnAssign(target=ast.Name(id=attr_name, ctx=ast.Store()), annotation=ann(inferred), value=None, simple=1))
                        self.require(inferred)
                        self.changed = True

        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and (
            "returning TypeVar should receive at least one argument" in message
            or "TypeVar" in message and diagnostic.rule in {"type-var", "reportInvalidTypeVarUse"}
        ):
            return_type = text(fn.returns) or ""
            variables = re.findall(r"\b_T[A-Za-z0-9_]*\b", return_type)
            argument_types = " ".join(text(arg.annotation) or "" for arg in [*fn.args.posonlyargs, *fn.args.args, *fn.args.kwonlyargs])
            for variable in variables:
                if variable in argument_types:
                    continue
                replacement = None
                if source_fn:
                    values = [node.value for node in ast.walk(source_fn) if isinstance(node, ast.Return)]
                    if values and all(isinstance(value, ast.Name) and value.id == "self" for value in values):
                        replacement = "Self"
                class_node = containing(self.tree, fn.lineno, (ast.ClassDef,))
                if not replacement and isinstance(class_node, ast.ClassDef):
                    replacement = class_node.name
                if replacement:
                    return_type = re.sub(rf"\b{re.escape(variable)}\b", replacement, return_type)
                    self.require(replacement)
                    self.changed = True
            if self.changed and return_type:
                fn.returns = ann(return_type)

        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and (
            "incompatible with supertype" in message
            or "overrides class" in message
            or diagnostic.rule in {"override", "reportIncompatibleMethodOverride"}
        ):
            class_node = containing(self.tree, fn.lineno, (ast.ClassDef,))
            if isinstance(class_node, ast.ClassDef):
                for base in class_node.bases:
                    base_name = (text(base) or "").split("[", 1)[0].rsplit(".", 1)[-1]
                    candidates = []
                    for path in STUB_ROOT.rglob("*.pyi"):
                        base_tree = parse(path)
                        if base_tree:
                            candidates.extend(node for node in base_tree.body if isinstance(node, ast.ClassDef) and node.name == base_name)
                    if len(candidates) != 1:
                        continue
                    base_fn = functions(candidates[0]).get(fn.name)
                    if not base_fn:
                        continue
                    sub_args = [*fn.args.posonlyargs, *fn.args.args]
                    base_args = [*base_fn.args.posonlyargs, *base_fn.args.args]
                    if sub_args and sub_args[0].arg in {"self", "cls"}:
                        sub_args = sub_args[1:]
                    if base_args and base_args[0].arg in {"self", "cls"}:
                        base_args = base_args[1:]
                    for sub_arg, base_arg in zip(sub_args, base_args):
                        sub_type = text(sub_arg.annotation)
                        base_type = text(base_arg.annotation)
                        if sub_type and base_type and sub_type != base_type and "object" not in base_type and "Any" not in base_type:
                            merged = merge_types(sub_type, base_type)
                            sub_arg.annotation = ann(merged)
                            self.require(merged)
                            self.changed = True
                    break

        if isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)) and (
            "not valid as a type" in message or diagnostic.rule == "reportInvalidTypeForm"
        ):
            class_node = containing(self.tree, fn.lineno, (ast.ClassDef,))
            if isinstance(class_node, ast.ClassDef):
                shadowed = set(functions(class_node)) & set(SHADOW_ALIASES)
                if shadowed:
                    for node in ast.walk(class_node):
                        annotation_node = None
                        if isinstance(node, ast.arg):
                            annotation_node = node.annotation
                        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                            annotation_node = node.returns
                        elif isinstance(node, ast.AnnAssign):
                            annotation_node = node.annotation
                        if annotation_node is None:
                            continue
                        rendered = text(annotation_node) or ""
                        updated = rendered
                        for builtin in shadowed:
                            if re.search(rf"\b{builtin}\b", updated):
                                alias = SHADOW_ALIASES[builtin]
                                updated = re.sub(rf"\b{builtin}\b", alias, updated)
                                self.aliases[alias] = builtin
                        if updated != rendered:
                            replacement = ann(updated)
                            if isinstance(node, ast.arg):
                                node.annotation = replacement
                            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                                node.returns = replacement
                            else:
                                node.annotation = replacement
                            self.changed = True

    def install_support(self) -> None:
        assert self.tree is not None
        existing: set[str] = set()
        imports: dict[tuple[str, int], ast.ImportFrom] = {}
        for node in self.tree.body:
            if isinstance(node, ast.ImportFrom) and node.module:
                imports[(node.module, node.level)] = node
                existing.update(alias.asname or alias.name for alias in node.names)
            elif isinstance(node, ast.Import):
                existing.update(alias.asname or alias.name.split(".", 1)[0] for alias in node.names)
            elif isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                existing.add(node.name)
            elif isinstance(node, ast.Assign):
                existing.update(target.id for target in node.targets if isinstance(target, ast.Name))
        position = 0
        if self.tree.body and isinstance(self.tree.body[0], ast.Expr) and isinstance(self.tree.body[0].value, ast.Constant) and isinstance(self.tree.body[0].value.value, str):
            position = 1
        while position < len(self.tree.body) and isinstance(self.tree.body[position], ast.ImportFrom) and self.tree.body[position].module == "__future__":
            position += 1
        additions: list[ast.stmt] = []
        for local, (module, original) in sorted(self.required.items()):
            if local in existing:
                continue
            key = (module, 0)
            alias = ast.alias(name=original, asname=local if local != original else None)
            if key in imports:
                imports[key].names.append(alias)
            else:
                import_node = ast.ImportFrom(module=module, names=[alias], level=0)
                imports[key] = import_node
                additions.append(import_node)
            existing.add(local)
        for alias, builtin in sorted(self.aliases.items()):
            if alias not in existing:
                additions.append(ast.Assign(targets=[ast.Name(id=alias, ctx=ast.Store())], value=ast.Name(id=builtin)))
                existing.add(alias)
        if additions:
            self.tree.body[position:position] = additions
            self.changed = True

    def run(self) -> bool:
        if self.tree is None:
            return False
        for diagnostic in self.diagnostics:
            self.repair_line(diagnostic)
        # Receiver annotations are invalid independently of a diagnostic and
        # inexpensive to normalize source-wide.
        for fn in [node for node in ast.walk(self.tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]:
            self.align_receiver(fn, source_function(self.source, self.tree, fn))
        self.install_support()
        if not self.changed:
            return False
        ast.fix_missing_locations(self.tree)
        self.path.write_text(ast.unparse(self.tree).rstrip() + "\n", encoding="utf-8")
        return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mypy", type=Path, required=True)
    parser.add_argument("--pyright", type=Path, required=True)
    args = parser.parse_args()
    diagnostics = [*parse_mypy(args.mypy), *parse_pyright(args.pyright)]
    by_path: dict[Path, list[Diagnostic]] = defaultdict(list)
    for diagnostic in diagnostics:
        by_path[diagnostic.path].append(diagnostic)
    changed: list[Path] = []
    for path, items in sorted(by_path.items()):
        if FileEditor(path, items).run():
            changed.append(path)
    print(f"analyzer-semantic repair: {len(changed)} file(s) changed from {len(diagnostics)} diagnostic(s)")
    for path in changed[:500]:
        print(path.relative_to(ROOT))
    if len(changed) > 500:
        print(f"... {len(changed) - 500} additional file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
