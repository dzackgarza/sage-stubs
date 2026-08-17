#!/usr/bin/env python3
"""Verify the mathematical generic relationships of the category kernel."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUBS = ROOT / "sage-stubs"


def parse(relative: str) -> ast.Module:
    path = STUBS / relative
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def dotted(node: ast.expr | None) -> str:
    if node is None:
        return ""
    try:
        return ast.unparse(node)
    except Exception:
        return ""


def class_named(tree: ast.Module, name: str) -> ast.ClassDef:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    raise AssertionError(f"missing class {name}")


def method(node: ast.ClassDef, name: str) -> ast.FunctionDef | ast.AsyncFunctionDef:
    for child in node.body:
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name == name:
            return child
    raise AssertionError(f"missing method {node.name}.{name}")


def generic_parameters(node: ast.ClassDef) -> list[str]:
    for base in node.bases:
        if not isinstance(base, ast.Subscript) or dotted(base.value) != "Generic":
            continue
        values = base.slice.elts if isinstance(base.slice, ast.Tuple) else [base.slice]
        return [dotted(value) for value in values]
    raise AssertionError(f"{node.name} is not generic")


def argument_annotation(
    function: ast.FunctionDef | ast.AsyncFunctionDef, name: str
) -> str:
    arguments = [
        *function.args.posonlyargs,
        *function.args.args,
        *function.args.kwonlyargs,
    ]
    if function.args.vararg:
        arguments.append(function.args.vararg)
    if function.args.kwarg:
        arguments.append(function.args.kwarg)
    for argument in arguments:
        if argument.arg == name:
            return dotted(argument.annotation)
    raise AssertionError(f"missing parameter {function.name}.{name}")


def check_parent() -> None:
    parent = class_named(parse("structure/parent.pyi"), "Parent")
    (element_type,) = generic_parameters(parent)
    expected = {
        "__call__": element_type,
        "_element_constructor_": element_type,
        "an_element": element_type,
        "gen": element_type,
        "gens": f"tuple[{element_type}, ...]",
        "_first_ngens": f"tuple[{element_type}, ...]",
        "some_elements": f"list[{element_type}]",
        "__iter__": f"Iterator[{element_type}]",
    }
    for name, annotation in expected.items():
        try:
            actual = dotted(method(parent, name).returns)
        except AssertionError:
            # Optional algebraic methods need not occur on the bare Parent API.
            if name in {"gen", "gens", "_first_ngens", "some_elements", "__iter__"}:
                continue
            raise
        assert actual == annotation, f"Parent.{name}: {actual} != {annotation}"


def check_element() -> None:
    element = class_named(parse("structure/element.pyi"), "Element")
    parent = method(element, "parent")
    self_type = argument_annotation(parent, "self")
    assert self_type and self_type != "Element"
    assert dotted(parent.returns) == f"Parent[{self_type}]"


def check_map() -> None:
    map_class = class_named(parse("categories/map.pyi"), "Map")
    domain_type, codomain_type = generic_parameters(map_class)
    assert dotted(method(map_class, "domain").returns) == f"Parent[{domain_type}]"
    assert dotted(method(map_class, "codomain").returns) == f"Parent[{codomain_type}]"
    call = method(map_class, "__call__")
    assert argument_annotation(call, "x") == domain_type
    assert dotted(call.returns) == codomain_type


def check_morphism() -> None:
    tree = parse("categories/morphism.pyi")
    morphism = class_named(tree, "Morphism")
    domain_type, codomain_type = generic_parameters(morphism)
    assert any(
        dotted(base) == f"Map[{domain_type}, {codomain_type}]"
        for base in morphism.bases
    )
    set_morphism = class_named(tree, "SetMorphism")
    set_domain, set_codomain = generic_parameters(set_morphism)
    assert any(
        dotted(base) == f"Morphism[{set_domain}, {set_codomain}]"
        for base in set_morphism.bases
    )


def check_homset() -> None:
    homset = class_named(parse("categories/homset.pyi"), "Homset")
    morphism_type, domain_type, codomain_type = generic_parameters(homset)
    assert dotted(method(homset, "domain").returns) == f"Parent[{domain_type}]"
    assert dotted(method(homset, "codomain").returns) == f"Parent[{codomain_type}]"
    assert dotted(method(homset, "an_element").returns) == morphism_type


def main() -> None:
    check_parent()
    check_element()
    check_map()
    check_morphism()
    check_homset()
    print("category kernel: generic mathematical contracts verified")


if __name__ == "__main__":
    main()
