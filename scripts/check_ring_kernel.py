#!/usr/bin/env python3
"""Verify coefficient-element preservation through the core ring hierarchy."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUBS = ROOT / "sage-stubs"


def parse(relative: str) -> ast.Module:
    path = STUBS / relative
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def render(node: ast.expr | None) -> str:
    return ast.unparse(node) if node is not None else ""


def class_named(tree: ast.Module, name: str) -> ast.ClassDef:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    raise AssertionError(f"missing class {name}")


def method(node: ast.ClassDef, name: str) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    for child in node.body:
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name == name:
            return child
    return None


def generic_parameters(node: ast.ClassDef) -> list[str]:
    for base in node.bases:
        if isinstance(base, ast.Subscript) and render(base.value) == "Generic":
            values = base.slice.elts if isinstance(base.slice, ast.Tuple) else [base.slice]
            return [render(value) for value in values]
    raise AssertionError(f"{node.name} is not generic")


def has_base(node: ast.ClassDef, expected: str) -> bool:
    return any(render(base) == expected for base in node.bases)


def check_parent_class(relative: str, class_name: str, base_name: str) -> None:
    cls = class_named(parse(relative), class_name)
    (element_type,) = generic_parameters(cls)
    assert has_base(cls, f"{base_name}[{element_type}]"), (
        class_name,
        [render(base) for base in cls.bases],
    )


def check_hierarchy() -> None:
    check_parent_class("rings/ring.pyi", "Ring", "Parent")
    check_parent_class("rings/commutative_ring.pyi", "CommutativeRing", "Ring")
    check_parent_class("rings/integral_domain.pyi", "IntegralDomain", "CommutativeRing")
    check_parent_class(
        "rings/principal_ideal_domain.pyi", "PrincipalIdealDomain", "IntegralDomain"
    )
    check_parent_class("rings/field.pyi", "Field", "PrincipalIdealDomain")


def check_morphisms() -> None:
    tree = parse("rings/morphism.pyi")
    ring_hom = class_named(tree, "RingHomomorphism")
    domain_type, codomain_type = generic_parameters(ring_hom)
    assert any(
        render(base)
        in {
            f"Morphism[{domain_type}, {codomain_type}]",
            f"RingMap[{domain_type}, {codomain_type}]",
        }
        for base in ring_hom.bases
    )


def check_homset() -> None:
    ring_homset = class_named(parse("rings/homset.pyi"), "RingHomset_generic")
    domain_type, codomain_type = generic_parameters(ring_homset)
    expected_morphism = f"RingHomomorphism[{domain_type}, {codomain_type}]"
    assert has_base(
        ring_homset,
        f"Homset[{expected_morphism}, {domain_type}, {codomain_type}]",
    )
    an_element = method(ring_homset, "an_element")
    if an_element is not None:
        assert render(an_element.returns) == expected_morphism


def main() -> None:
    check_hierarchy()
    check_morphisms()
    check_homset()
    print("ring kernel: coefficient and homomorphism contracts verified")


if __name__ == "__main__":
    main()
