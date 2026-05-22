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
  - Any as a parameter type (banned unconditionally)
  - object as a return type (banned except known protocol dunders)
  - TYPE_CHECKING, local suppressions, cast, builtins aliases, and legacy typing aliases

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


# Dunders and functions whose return type is legitimately object or whose params accept object
# Functions that forward genuinely opaque callback values or untyped return values are included
OBJECT_RETURN_OK = {
    "__new__",
    # sage.misc.call: forwards method return values
    "call_method",
    "__call__",  # for callables that forward opaque returns
    # sage.misc.callable_dict: forwards dict values
    # "__call__" already listed
    # sage.misc.classcall_metaclass: forwards object construction
    "typecall",
    # sage.misc.decorators: decorators forward opaque returns
    # "__call__" already listed
    "_left",
    "_right",
    # sage.misc.lazy_attribute, lazy_list: forward opaque values
    "__get__",
    # sage.misc.persist: unpickles/loads arbitrary objects
    "load",
    "loads",
    "unpickle_global",
    "load_sage_object",
    "load_sage_element",
    "db",
    # sage.misc.sage_eval, sage_input: evaluate/format arbitrary objects
    "sage_eval",
    "sageobj",
    "sage_input",
    # sage.misc.sageinspect: inspects return values of arbitrary functions
    "sage_getargspec",
    # sage.misc.fast_methods: comparison operations on arbitrary types
    "__richcmp__",
    # sage.misc.lazy_list: indexing can return arbitrary elements
    "__getitem__",
}
LOCAL_SUPPRESSIONS = ("type: ignore", "noqa")
LEGACY_TYPING_ALIASES = {"List", "Dict", "Tuple", "Set", "FrozenSet"}


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
        if is_any(arg.annotation):
            errors.append(
                f"{path}:{ln}: `{fn.name}` parameter `{arg.arg}` typed `Any` — banned. "
                "Use a concrete type."
            )

    return errors


def check_tree(tree: ast.Module, path: Path) -> list[str]:
    errors = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            if node.module == "typing":
                for alias in node.names:
                    if alias.name == "TYPE_CHECKING":
                        errors.append(
                            f"{path}:{node.lineno}: TYPE_CHECKING import — banned. "
                            "Import annotation types directly."
                        )
                    if alias.name == "Any":
                        errors.append(
                            f"{path}:{node.lineno}: Any import — banned. "
                            "Use concrete types or object for honest opacity."
                        )
                    if alias.name == "cast":
                        errors.append(
                            f"{path}:{node.lineno}: cast import — banned in stubs. "
                            "Fix the annotation instead."
                        )
                    if alias.name in LEGACY_TYPING_ALIASES:
                        errors.append(
                            f"{path}:{node.lineno}: typing.{alias.name} import — banned. "
                            "Use built-in generics."
                        )
            if node.module == "builtins":
                errors.append(
                    f"{path}:{node.lineno}: builtins import — banned. "
                    "Use normal built-in names."
                )
        elif isinstance(node, ast.If) and isinstance(node.test, ast.Name) and node.test.id == "TYPE_CHECKING":
            errors.append(
                f"{path}:{node.lineno}: TYPE_CHECKING block — banned. "
                "Import annotation types directly."
            )
        elif isinstance(node, ast.Attribute):
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "typing"
                and node.attr in LEGACY_TYPING_ALIASES
            ):
                errors.append(
                    f"{path}:{node.lineno}: typing.{node.attr} annotation — banned. "
                    "Use built-in generics."
                )
            if isinstance(node.value, ast.Name) and node.value.id == "builtins":
                errors.append(
                    f"{path}:{node.lineno}: builtins.{node.attr} — banned. "
                    "Use normal built-in names."
                )
            if isinstance(node.value, ast.Name) and node.value.id == "typing" and node.attr == "Any":
                errors.append(
                    f"{path}:{node.lineno}: typing.Any — banned. "
                    "Use concrete types or object for honest opacity."
                )
        elif isinstance(node, ast.Name):
            if node.id == "Any":
                errors.append(
                    f"{path}:{node.lineno}: Any — banned. "
                    "Use concrete types or object for honest opacity."
                )
            if node.id == "cast":
                errors.append(
                    f"{path}:{node.lineno}: cast — banned in stubs. "
                    "Fix the annotation instead."
                )
    return errors


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    marker_errors = [
        f"{path}:{lineno}: local suppression `{marker}` — banned."
        for lineno, line in enumerate(text.splitlines(), start=1)
        for marker in LOCAL_SUPPRESSIONS
        if marker in line
    ]
    try:
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as e:
        return [f"{path}:{e.lineno}: SyntaxError: {e.msg}"]
    errors = marker_errors + check_tree(tree, path)
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
