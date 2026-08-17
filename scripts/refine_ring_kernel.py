#!/usr/bin/env python3
"""Reconstruct the generic ring-parent and ring-morphism tower.

The transformations preserve one coefficient-element parameter through the
algebraic parent hierarchy and two coefficient-element parameters through ring
homomorphisms. They are guarded by the inheritance graph in the pinned Sage
source and do not infer a type from a parameter name.
"""

from __future__ import annotations

import ast
from pathlib import Path

from refine_category_kernel import (
    STUB_ROOT,
    dotted_name,
    ensure_import_from,
    expression,
    find_class,
    find_method,
    parameterize_base,
    require_source_base,
    set_return,
    write_tree,
)
from refine_category_kernel_v2 import ensure_generic_parameters, generic_parameters


def import_element_type(tree: ast.Module, name: str) -> None:
    ensure_import_from(tree, "sage.structure.element", (name,))


def refine_parent_class(
    *,
    relative: str,
    source_relative: str,
    class_name: str,
    source_base: str,
    stub_base: str,
    typevar_name: str,
    element_bound: str,
) -> None:
    require_source_base(source_relative, class_name, source_base)
    path = STUB_ROOT / relative
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    import_element_type(tree, element_bound)
    cls = find_class(tree, class_name)
    element_type = ensure_generic_parameters(
        tree,
        cls,
        ((
            typevar_name,
            f'TypeVar("{typevar_name}", bound={element_bound}, default={element_bound})',
        ),),
    )[0]
    parameterize_base(cls, stub_base, element_type)
    write_tree(path, tree)


def refine_ring_hierarchy() -> None:
    refine_parent_class(
        relative="rings/ring.pyi",
        source_relative="rings/ring.pyx",
        class_name="Ring",
        source_base="Parent",
        stub_base="Parent",
        typevar_name="_RingElementT",
        element_bound="RingElement",
    )
    refine_parent_class(
        relative="rings/commutative_ring.pyi",
        source_relative="rings/commutative_ring.pyx",
        class_name="CommutativeRing",
        source_base="Ring",
        stub_base="Ring",
        typevar_name="_CommutativeRingElementT",
        element_bound="CommutativeRingElement",
    )
    refine_parent_class(
        relative="rings/integral_domain.pyi",
        source_relative="rings/integral_domain.pyx",
        class_name="IntegralDomain",
        source_base="CommutativeRing",
        stub_base="CommutativeRing",
        typevar_name="_IntegralDomainElementT",
        element_bound="CommutativeRingElement",
    )
    refine_parent_class(
        relative="rings/principal_ideal_domain.pyi",
        source_relative="rings/principal_ideal_domain.pyx",
        class_name="PrincipalIdealDomain",
        source_base="IntegralDomain",
        stub_base="IntegralDomain",
        typevar_name="_PrincipalIdealDomainElementT",
        element_bound="CommutativeRingElement",
    )
    refine_parent_class(
        relative="rings/field.pyi",
        source_relative="rings/field.pyx",
        class_name="Field",
        source_base="PrincipalIdealDomain",
        stub_base="PrincipalIdealDomain",
        typevar_name="_FieldElementT",
        element_bound="FieldElement",
    )


def class_if_present(tree: ast.Module, name: str) -> ast.ClassDef | None:
    try:
        return find_class(tree, name)
    except RuntimeError:
        return None


def refine_ring_morphisms() -> None:
    path = STUB_ROOT / "rings" / "morphism.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    import_element_type(tree, "RingElement")

    ring_map = class_if_present(tree, "RingMap")
    if ring_map is not None:
        require_source_base("rings/morphism.pyx", "RingMap", "Morphism")
        domain_type, codomain_type = ensure_generic_parameters(
            tree,
            ring_map,
            (
                (
                    "_RingMapDomainElementT",
                    'TypeVar("_RingMapDomainElementT", bound=RingElement, default=RingElement)',
                ),
                (
                    "_RingMapCodomainElementT",
                    'TypeVar("_RingMapCodomainElementT", bound=RingElement, default=RingElement)',
                ),
            ),
        )
        parameterize_base(ring_map, "Morphism", f"{domain_type}, {codomain_type}")
        hom_base = "RingMap"
    else:
        domain_type = "_RingHomDomainElementT"
        codomain_type = "_RingHomCodomainElementT"
        hom_base = "Morphism"

    ring_hom = find_class(tree, "RingHomomorphism")
    hom_parameters = generic_parameters(ring_hom)
    if hom_parameters:
        if len(hom_parameters) != 2:
            raise RuntimeError("RingHomomorphism must have domain/codomain parameters")
        hom_domain, hom_codomain = hom_parameters
    else:
        hom_domain, hom_codomain = ensure_generic_parameters(
            tree,
            ring_hom,
            (
                (
                    "_RingHomDomainElementT",
                    'TypeVar("_RingHomDomainElementT", bound=RingElement, default=RingElement)',
                ),
                (
                    "_RingHomCodomainElementT",
                    'TypeVar("_RingHomCodomainElementT", bound=RingElement, default=RingElement)',
                ),
            ),
        )
    parameterize_base(ring_hom, hom_base, f"{hom_domain}, {hom_codomain}")
    write_tree(path, tree)


def refine_ring_homset() -> None:
    require_source_base("rings/homset.py", "RingHomset_generic", "Homset")
    path = STUB_ROOT / "rings" / "homset.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    import_element_type(tree, "RingElement")
    ring_homset = find_class(tree, "RingHomset_generic")
    domain_type, codomain_type = ensure_generic_parameters(
        tree,
        ring_homset,
        (
            (
                "_RingHomsetDomainElementT",
                'TypeVar("_RingHomsetDomainElementT", bound=RingElement, default=RingElement)',
            ),
            (
                "_RingHomsetCodomainElementT",
                'TypeVar("_RingHomsetCodomainElementT", bound=RingElement, default=RingElement)',
            ),
        ),
    )
    parameterize_base(
        ring_homset,
        "Homset",
        f"RingHomomorphism[{domain_type}, {codomain_type}], {domain_type}, {codomain_type}",
    )
    for name in ("__call__", "an_element", "natural_map", "identity", "one"):
        set_return(
            ring_homset,
            name,
            f"RingHomomorphism[{domain_type}, {codomain_type}]",
        )
    write_tree(path, tree)


def main() -> None:
    refine_ring_hierarchy()
    refine_ring_morphisms()
    refine_ring_homset()


if __name__ == "__main__":
    main()
