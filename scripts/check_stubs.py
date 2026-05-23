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
  - quoted/string annotations (banned except string values inside Literal)
  - variadic *args / **kwds signatures (banned; model the finite surface)
  - TYPE_CHECKING, local suppressions, cast, builtins aliases, and legacy typing aliases

Exit 0 = clean. Exit 1 = violations.
"""

import argparse
import ast
import sys
from pathlib import Path


def is_any(node: ast.expr) -> bool:
    return (isinstance(node, ast.Name) and node.id == "Any") or (
        isinstance(node, ast.Attribute) and node.attr == "Any"
    )


def is_object(node: ast.expr) -> bool:
    return isinstance(node, ast.Name) and node.id == "object"


def is_literal_subscript(node: ast.AST) -> bool:
    if not isinstance(node, ast.Subscript):
        return False
    value = node.value
    return (
        isinstance(value, ast.Name) and value.id == "Literal"
    ) or (
        isinstance(value, ast.Attribute) and value.attr == "Literal"
    )


def is_inside_literal_subscript(node: ast.AST) -> bool:
    current = getattr(node, "_stub_parent", None)
    while current is not None:
        if is_literal_subscript(current):
            return True
        current = getattr(current, "_stub_parent", None)
    return False


def contains_quoted_annotation(node: ast.AST | None) -> bool:
    if node is None:
        return False
    return any(
        isinstance(child, ast.Constant)
        and isinstance(child.value, str)
        and not is_inside_literal_subscript(child)
        for child in ast.walk(node)
    )


def is_type_alias_annotation(node: ast.AST | None) -> bool:
    return (
        isinstance(node, ast.Name) and node.id == "TypeAlias"
    ) or (
        isinstance(node, ast.Attribute) and node.attr == "TypeAlias"
    )


def check_annotation_expr(
    annotation: ast.AST | None,
    path: Path,
    lineno: int,
    label: str,
) -> list[str]:
    if not contains_quoted_annotation(annotation):
        return []
    return [
        f"{path}:{lineno}: {label} contains quoted type annotation — banned. "
        "Import the annotation type directly or add the source-backed support stub; "
        "string forward references hide type-surface changes."
    ]


# Dunders whose return type is legitimately object or whose params accept object
OBJECT_RETURN_OK = {"__new__"}
LOCAL_SUPPRESSIONS = ("type: ignore", "noqa")
LEGACY_TYPING_ALIASES = {"List", "Dict", "Tuple", "Set", "FrozenSet"}
BUILTIN_COLLISION_NAMES = {"list", "dict", "tuple", "set", "type", "object"}


def annotate_parents(tree: ast.AST) -> None:
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            setattr(child, "_stub_parent", parent)


def enclosing_class(node: ast.AST) -> ast.ClassDef | None:
    current = getattr(node, "_stub_parent", None)
    while current is not None:
        if isinstance(current, ast.ClassDef):
            return current
        current = getattr(current, "_stub_parent", None)
    return None


def is_allowed_builtin_collision(node: ast.Attribute) -> bool:
    if node.attr not in BUILTIN_COLLISION_NAMES:
        return False
    cls = enclosing_class(node)
    if cls is None:
        return False
    return any(
        isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and item.name == node.attr
        for item in cls.body
    )


def check_function(fn: ast.FunctionDef | ast.AsyncFunctionDef, path: Path) -> list[str]:
    errors = []
    ln = fn.lineno

    # Return type
    ret = fn.returns
    errors.extend(check_annotation_expr(ret, path, ln, f"`{fn.name}` return annotation"))
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

    if fn.args.vararg:
        errors.append(
            f"{path}:{ln}: `{fn.name}` variadic `*{fn.args.vararg.arg}` — banned in stubs. "
            "Exhaust the source code paths into overloads, finite unions, or a "
            "source-audited argument container type that enumerates every accepted variable."
        )
    if fn.args.kwarg:
        errors.append(
            f"{path}:{ln}: `{fn.name}` variadic `**{fn.args.kwarg.arg}` — banned in stubs. "
            "Exhaust the source code paths into overloads, finite unions, or a "
            "source-audited keyword container type that enumerates every accepted variable."
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
        errors.extend(
            check_annotation_expr(
                arg.annotation,
                path,
                ln,
                f"`{fn.name}` parameter `{arg.arg}` annotation",
            )
        )
        if is_any(arg.annotation):
            errors.append(
                f"{path}:{ln}: `{fn.name}` parameter `{arg.arg}` typed `Any` — banned. "
                "Use a concrete type."
            )

    return errors


def check_tree(tree: ast.Module, path: Path) -> list[str]:
    errors = []
    annotate_parents(tree)
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
                            "Resolve the concrete type; do not substitute object."
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
        elif isinstance(node, ast.ClassDef):
            for base in node.bases:
                errors.extend(
                    check_annotation_expr(
                        base,
                        path,
                        node.lineno,
                        f"`{node.name}` class base",
                    )
                )
        elif isinstance(node, ast.AnnAssign):
            errors.extend(
                check_annotation_expr(
                    node.annotation,
                    path,
                    node.lineno,
                    "variable annotation",
                )
            )
            if is_type_alias_annotation(node.annotation):
                errors.extend(
                    check_annotation_expr(
                        node.value,
                        path,
                        node.lineno,
                        "type alias",
                    )
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
            if (
                isinstance(node.value, ast.Name)
                and node.value.id == "builtins"
                and not is_allowed_builtin_collision(node)
            ):
                errors.append(
                    f"{path}:{node.lineno}: builtins.{node.attr} — banned. "
                    "Use normal built-in names."
                )
            if isinstance(node.value, ast.Name) and node.value.id == "typing" and node.attr == "Any":
                errors.append(
                    f"{path}:{node.lineno}: typing.Any — banned. "
                    "Resolve the concrete type; do not substitute object."
                )
        elif isinstance(node, ast.Name):
            if node.id == "Any":
                errors.append(
                    f"{path}:{node.lineno}: Any — banned. "
                    "Resolve the concrete type; do not substitute object."
                )
            if node.id == "cast":
                errors.append(
                    f"{path}:{node.lineno}: cast — banned in stubs. "
                    "Fix the annotation instead."
            )
    return errors


def check_text(text: str, path: Path) -> list[str]:
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


def check_file(path: Path) -> list[str]:
    return check_text(path.read_text(encoding="utf-8"), path)


def run_self_test() -> int:
    cases = [
        (
            "quoted return",
            "class Foo: ...\ndef f() -> \"Foo\": ...\n",
            ["return annotation contains quoted type annotation"],
        ),
        (
            "nested quoted parameter",
            "class Foo: ...\ndef f(x: list[\"Foo\"]) -> None: ...\n",
            ["parameter `x` annotation contains quoted type annotation"],
        ),
        (
            "literal values",
            "from typing import Literal\n\ndef f() -> Literal[\"fast\", \"slow\"]: ...\n",
            [],
        ),
        (
            "quoted type alias",
            "from typing import TypeAlias\nAlias: TypeAlias = \"Foo\"\n",
            ["type alias contains quoted type annotation"],
        ),
        (
            "args variadic",
            "def f(*args: int) -> None: ...\n",
            ["variadic `*args`"],
        ),
        (
            "kwargs variadic",
            "def f(**kwds: int) -> None: ...\n",
            ["variadic `**kwds`"],
        ),
    ]
    failed = 0
    for name, text, expected_fragments in cases:
        errors = check_text(text, Path(f"<check_stubs:{name}>"))
        if not expected_fragments:
            if errors:
                print(f"FAIL: {name}: unexpected errors: {errors}", file=sys.stderr)
                failed += 1
            continue

        missing = [
            fragment
            for fragment in expected_fragments
            if not any(fragment in error for error in errors)
        ]
        if missing:
            print(f"FAIL: {name}: missing {missing}; errors: {errors}", file=sys.stderr)
            failed += 1
    if failed:
        return 1
    print("check_stubs self-test: ok.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="run built-in policy tests")
    parser.add_argument("paths", nargs="*", help=".pyi files to check")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()

    paths = [Path(p) for p in args.paths if p.endswith(".pyi")]
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
