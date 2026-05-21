#!/usr/bin/env python3
"""
Bespoke stub enforcer: bans Any in positions ruff cannot reach.

ruff (ANN, UP, PYI) handles:
  - Missing annotations
  - Optional[X] → X | None
  - Union[X, Y] → X | Y
  - Deprecated typing imports

This script adds:
  - Any as a return type (banned unconditionally)
  - Any as a named parameter type (banned; *args/*kwargs excepted)
  - object as a return type (banned except known protocol dunders)

Exit 0 = clean. Exit 1 = violations.
"""

import ast
import sys
from pathlib import Path


def is_any(node: ast.expr) -> bool:
    return (isinstance(node, ast.Name) and node.id == "Any") or (
        isinstance(node, ast.Attribute) and node.attr == "Any"
    )


def is_object(node: ast.expr) -> bool:
    return isinstance(node, ast.Name) and node.id == "object"


# Dunders whose return type is legitimately object or whose params accept object
OBJECT_RETURN_OK = {"__new__"}
ANY_PARAM_OK_DUNDERS = {"__eq__", "__ne__", "__hash__", "__contains__", "__lt__",
                        "__le__", "__gt__", "__ge__"}


def check_function(fn: ast.FunctionDef | ast.AsyncFunctionDef, path: Path) -> list[str]:
    errors = []
    ln = fn.lineno

    # Return type
    ret = fn.returns
    if ret is not None:
        if is_any(ret):
            errors.append(
                f"{path}:{ln}: `{fn.name}` return type `Any` — banned. "
                "Use a concrete type, Self, Union, or overload."
            )
        if is_object(ret) and fn.name not in OBJECT_RETURN_OK:
            errors.append(
                f"{path}:{ln}: `{fn.name}` return type `object` — almost never correct. "
                "Use a concrete type."
            )

    # Parameters
    all_args = (
        fn.args.posonlyargs + fn.args.args + fn.args.kwonlyargs
        + ([fn.args.vararg] if fn.args.vararg else [])
        + ([fn.args.kwarg] if fn.args.kwarg else [])
    )
    for arg in all_args:
        if arg.arg in ("self", "cls") or arg.annotation is None:
            continue
        is_variadic = arg is fn.args.vararg or arg is fn.args.kwarg
        if is_any(arg.annotation):
            if is_variadic:
                continue  # *args: Any, **kwargs: Any are structurally necessary
            if fn.name in ANY_PARAM_OK_DUNDERS:
                continue  # protocol dunders accept object/Any by contract
            errors.append(
                f"{path}:{ln}: `{fn.name}` parameter `{arg.arg}` typed `Any` — banned. "
                "Use a concrete type."
            )

    return errors


def check_file(path: Path) -> list[str]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as e:
        return [f"{path}:{e.lineno}: SyntaxError: {e.msg}"]
    errors = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            errors.extend(check_function(node, path))
    return errors


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:] if p.endswith(".pyi")]
    if not paths:
        paths = list(Path(".").rglob("*.pyi"))
    if not paths:
        return 0

    errors = [e for p in sorted(paths) for e in check_file(p)]
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"\n{len(errors)} violation(s). Commit rejected.", file=sys.stderr)
        return 1

    print(f"check_stubs: {len(paths)} file(s) clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
