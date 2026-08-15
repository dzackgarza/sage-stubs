"""AST-backed extraction of directly defined public Python surfaces."""
from __future__ import annotations

import ast
from pathlib import Path

from stubgen_common import BOOL_NAMES, HEADER, INT_NAMES, STR_NAMES, literal_type, public, return_from_name, simple_annotation


def param_type(arg: ast.arg, default: ast.expr | None, local: set[str]) -> str:
    annotation = simple_annotation(arg.annotation, local)
    if annotation:
        return annotation
    literal = literal_type(default)
    if literal and literal != "None":
        return literal
    name = arg.arg.lower()
    if name in INT_NAMES: return "int"
    if name in BOOL_NAMES: return "bool"
    if name in STR_NAMES or name.endswith("_name"): return "str"
    return "object"


def return_type(fn: ast.FunctionDef | ast.AsyncFunctionDef, local: set[str]) -> str:
    annotation = simple_annotation(fn.returns, local)
    return annotation if annotation and annotation != "object" else return_from_name(fn.name)


def signature(fn: ast.FunctionDef | ast.AsyncFunctionDef, local: set[str], *, method: bool = False) -> str:
    args = fn.args
    positional = [*args.posonlyargs, *args.args]
    defaults: list[ast.expr | None] = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)
    bits: list[str] = []
    for index, (arg, default) in enumerate(zip(positional, defaults)):
        if method and arg.arg == "self":
            text = "self: Self"
        elif method and arg.arg == "cls":
            text = "cls: type[Self]"
        else:
            text = f"{arg.arg}: {param_type(arg, default, local)}"
        if default is not None:
            text += " = ..."
        bits.append(text)
        if args.posonlyargs and index + 1 == len(args.posonlyargs):
            bits.append("/")
    if args.vararg:
        bits.append(f"*{args.vararg.arg}: object")
    elif args.kwonlyargs:
        bits.append("*")
    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        text = f"{arg.arg}: {param_type(arg, default, local)}"
        if default is not None:
            text += " = ..."
        bits.append(text)
    if args.kwarg:
        bits.append(f"**{args.kwarg.arg}: object")
    return f"({', '.join(bits)}) -> {return_type(fn, local)}"


def decorators(fn: ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    out: list[str] = []
    for decorator in fn.decorator_list:
        name = decorator.id if isinstance(decorator, ast.Name) else decorator.attr if isinstance(decorator, ast.Attribute) else ""
        if name in {"staticmethod", "classmethod", "property"}:
            out.append(f"@{name}")
    return out


def assigned_names(node: ast.stmt) -> list[str]:
    targets: list[ast.expr] = []
    if isinstance(node, ast.Assign):
        targets = list(node.targets)
    elif isinstance(node, ast.AnnAssign):
        targets = [node.target]
    out: list[str] = []
    for target in targets:
        if isinstance(target, ast.Name):
            out.append(target.id)
        elif isinstance(target, (ast.Tuple, ast.List)):
            out.extend(item.id for item in target.elts if isinstance(item, ast.Name))
    return out


def render_class(node: ast.ClassDef, local: set[str], indent: str = "") -> list[str]:
    base = "(Exception)" if node.name.endswith(("Error", "Exception")) else ""
    lines = [f"{indent}class {node.name}{base}:"]
    body: list[str] = []
    seen: set[str] = set()
    definitions = {item.name for item in node.body if isinstance(item, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))}
    for item in node.body:
        if isinstance(item, ast.ClassDef) and public(item.name) and item.name not in seen:
            seen.add(item.name)
            body.extend(render_class(item, local, indent + "    "))
        elif isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and public(item.name, True) and item.name not in seen:
            if any(isinstance(d, ast.Attribute) and d.attr in {"setter", "deleter"} for d in item.decorator_list):
                continue
            seen.add(item.name)
            for decorator in decorators(item):
                body.append(f"{indent}    {decorator}")
            prefix = "async def" if isinstance(item, ast.AsyncFunctionDef) else "def"
            body.append(f"{indent}    {prefix} {item.name}{signature(item, local, method=True)}: ...")
        else:
            for name in assigned_names(item):
                if public(name) and name not in definitions and name not in seen:
                    seen.add(name)
                    body.append(f"{indent}    {name}: _SageObject")
    return lines + (body or [f"{indent}    ..."])


def parse_python(path: Path) -> str:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    local = {node.name for node in tree.body if isinstance(node, ast.ClassDef) and public(node.name)}
    lines: list[str] = []
    seen: set[str] = set()
    definitions = {node.name for node in tree.body if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))}
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and public(node.name) and node.name not in seen:
            seen.add(node.name)
            lines.extend(render_class(node, local))
            lines.append("")
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and public(node.name) and node.name not in seen:
            seen.add(node.name)
            lines.extend(decorators(node))
            prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
            lines.append(f"{prefix} {node.name}{signature(node, local)}: ...\n")
        else:
            for name in assigned_names(node):
                if public(name) and name not in definitions and name not in seen and name != "__all__":
                    seen.add(name)
                    lines.append(f"{name}: _SageObject")
    return HEADER + ("\n".join(lines).rstrip() + "\n" if lines else "")
