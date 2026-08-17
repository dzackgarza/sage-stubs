#!/usr/bin/env python3
"""Set the variance and bounds of the reviewed category-kernel TypeVars.

Sage parents may contain plain Python values, so parent and map value variables
are not bounded by ``Element``.  Parent/set values and map codomains are
covariant; map domains are contravariant.  This pass replaces stale generated
TypeVar declarations after the structural reconstruction.
"""

from __future__ import annotations

import ast
from pathlib import Path

from refine_category_kernel import STUB_ROOT, expression, find_class, write_tree
from refine_category_kernel_v2 import generic_parameters


def set_assignment(tree: ast.Module, name: str, value: str) -> None:
    replacement = expression(value)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
                node.value = replacement
                return
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                node.value = replacement
                return
    raise RuntimeError(f"missing TypeVar declaration for {name}")


def refine_parent() -> None:
    path = STUB_ROOT / "structure" / "parent.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    parent = find_class(tree, "Parent")
    (parent_element,) = generic_parameters(parent)
    set_assignment(
        tree,
        parent_element,
        f'TypeVar("{parent_element}", default=Element, covariant=True)',
    )

    set_generic = find_class(tree, "Set_generic")
    (set_element,) = generic_parameters(set_generic)
    set_assignment(
        tree,
        set_element,
        f'TypeVar("{set_element}", default=Element, covariant=True)',
    )
    write_tree(path, tree)


def refine_map() -> None:
    path = STUB_ROOT / "categories" / "map.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    map_class = find_class(tree, "Map")
    domain, codomain = generic_parameters(map_class)
    set_assignment(
        tree,
        domain,
        f'TypeVar("{domain}", default=Element, contravariant=True)',
    )
    set_assignment(
        tree,
        codomain,
        f'TypeVar("{codomain}", default=Element, covariant=True)',
    )
    write_tree(path, tree)


def refine_morphism() -> None:
    path = STUB_ROOT / "categories" / "morphism.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    morphism = find_class(tree, "Morphism")
    domain, codomain = generic_parameters(morphism)
    set_assignment(
        tree,
        domain,
        f'TypeVar("{domain}", default=Element, contravariant=True)',
    )
    set_assignment(
        tree,
        codomain,
        f'TypeVar("{codomain}", default=Element, covariant=True)',
    )

    set_morphism = find_class(tree, "SetMorphism")
    set_domain, set_codomain = generic_parameters(set_morphism)
    if set_domain != domain:
        set_assignment(
            tree,
            set_domain,
            f'TypeVar("{set_domain}", default=Element, contravariant=True)',
        )
    if set_codomain != codomain:
        set_assignment(
            tree,
            set_codomain,
            f'TypeVar("{set_codomain}", default=Element, covariant=True)',
        )
    write_tree(path, tree)


def main() -> None:
    refine_parent()
    refine_map()
    refine_morphism()


if __name__ == "__main__":
    main()
