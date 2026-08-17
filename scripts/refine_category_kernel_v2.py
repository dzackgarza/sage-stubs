#!/usr/bin/env python3
"""Apply the reviewed category-kernel relationships without replacing extant generics."""

from __future__ import annotations

import ast

from refine_category_kernel import (
    SOURCE_ROOT,
    STUB_ROOT,
    add_generic_base,
    dotted_name,
    ensure_assignment,
    ensure_import_from,
    expression,
    find_class,
    parameterize_base,
    require_source_base,
    set_parameter,
    set_return,
    write_tree,
)


def generic_parameters(node: ast.ClassDef) -> list[str]:
    for base in node.bases:
        if dotted_name(base) != "Generic" or not isinstance(base, ast.Subscript):
            continue
        values = base.slice.elts if isinstance(base.slice, ast.Tuple) else [base.slice]
        names: list[str] = []
        for value in values:
            if not isinstance(value, ast.Name):
                raise RuntimeError(f"non-name Generic parameter on {node.name}")
            names.append(value.id)
        return names
    return []


def ensure_generic_parameters(
    tree: ast.Module,
    node: ast.ClassDef,
    declarations: tuple[tuple[str, str], ...],
) -> list[str]:
    current = generic_parameters(node)
    if current:
        if len(current) != len(declarations):
            raise RuntimeError(
                f"{node.name} has {len(current)} generic parameters; expected {len(declarations)}"
            )
        return current
    ensure_import_from(tree, "typing", ("Generic", "TypeVar"))
    for name, declaration in declarations:
        ensure_assignment(tree, name, declaration)
    add_generic_base(node, ", ".join(name for name, _ in declarations))
    return [name for name, _ in declarations]


def refine_element() -> None:
    path = STUB_ROOT / "structure" / "element.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "typing", ("TypeVar",))
    ensure_assignment(tree, "_ElementSelfT", 'TypeVar("_ElementSelfT", bound="Element")')
    element = find_class(tree, "Element")
    set_parameter(element, "parent", "self", "_ElementSelfT")
    set_return(element, "parent", "Parent[_ElementSelfT]")
    write_tree(path, tree)


def refine_parent() -> None:
    require_source_base("structure/parent.pyx", "Parent", "CategoryObject")
    path = STUB_ROOT / "structure" / "parent.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "collections.abc", ("Iterator",))
    parent = find_class(tree, "Parent")
    element_type = ensure_generic_parameters(
        tree,
        parent,
        ((
            "_ParentElementT",
            'TypeVar("_ParentElementT", bound=Element, default=Element)',
        ),),
    )[0]
    for name in ("__call__", "_element_constructor_", "an_element", "gen", "zero", "one"):
        set_return(parent, name, element_type)
    for name in ("gens", "_first_ngens"):
        set_return(parent, name, f"tuple[{element_type}, ...]")
    set_return(parent, "some_elements", f"list[{element_type}]")
    set_return(parent, "__iter__", f"Iterator[{element_type}]")
    write_tree(path, tree)


def refine_map() -> tuple[str, str]:
    require_source_base("categories/map.pyx", "Map", "Element")
    path = STUB_ROOT / "categories" / "map.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    map_class = find_class(tree, "Map")
    domain_type, codomain_type = ensure_generic_parameters(
        tree,
        map_class,
        (
            (
                "_MapDomainElementT",
                'TypeVar("_MapDomainElementT", bound=Element, default=Element)',
            ),
            (
                "_MapCodomainElementT",
                'TypeVar("_MapCodomainElementT", bound=Element, default=Element)',
            ),
        ),
    )
    set_return(map_class, "domain", f"Parent[{domain_type}]")
    set_return(map_class, "codomain", f"Parent[{codomain_type}]")
    for name in ("__call__", "_call_", "_call_with_args"):
        set_parameter(map_class, name, "x", domain_type)
        set_return(map_class, name, codomain_type)
    set_return(map_class, "section", f"Map[{codomain_type}, {domain_type}]")
    write_tree(path, tree)
    return domain_type, codomain_type


def refine_morphism() -> tuple[str, str]:
    require_source_base("categories/morphism.pyx", "Morphism", "Map")
    require_source_base("categories/morphism.pyx", "SetMorphism", "Morphism")
    path = STUB_ROOT / "categories" / "morphism.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    morphism = find_class(tree, "Morphism")
    domain_type, codomain_type = ensure_generic_parameters(
        tree,
        morphism,
        (
            (
                "_MorphismDomainElementT",
                'TypeVar("_MorphismDomainElementT", bound=Element, default=Element)',
            ),
            (
                "_MorphismCodomainElementT",
                'TypeVar("_MorphismCodomainElementT", bound=Element, default=Element)',
            ),
        ),
    )
    parameterize_base(morphism, "Map", f"{domain_type}, {codomain_type}")

    set_morphism = find_class(tree, "SetMorphism")
    set_parameters = generic_parameters(set_morphism)
    if set_parameters and set_parameters != [domain_type, codomain_type]:
        # A subclass may name the variables differently; preserve those names.
        set_domain, set_codomain = set_parameters
    else:
        if not set_parameters:
            add_generic_base(set_morphism, f"{domain_type}, {codomain_type}")
        set_domain, set_codomain = domain_type, codomain_type
    parameterize_base(set_morphism, "Morphism", f"{set_domain}, {set_codomain}")
    write_tree(path, tree)
    return domain_type, codomain_type


def refine_homset() -> None:
    path = STUB_ROOT / "categories" / "homset.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    # The reviewed homset stub uses these names explicitly.  Abort if a future
    # edit changes the declaration rather than attempting a heuristic rewrite.
    homset = find_class(tree, "Homset")
    parameters = generic_parameters(homset)
    if parameters != ["_MorphismT", "_DomainElementT", "_CodomainElementT"]:
        raise RuntimeError(f"unexpected Homset generic parameters: {parameters}")

    for node in tree.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name == "Hom":
            text = ast.unparse(node.returns) if node.returns else ""
            if text.startswith("Homset[Morphism,"):
                node.returns = expression(
                    "Homset[Morphism[_DomainElementT, _CodomainElementT], "
                    "_DomainElementT, _CodomainElementT]"
                )
        elif node.name == "End":
            node.returns = expression(
                "Homset[Morphism[_DomainElementT, _DomainElementT], "
                "_DomainElementT, _DomainElementT]"
            )
        elif node.name in {"hom", "end"}:
            node.returns = expression(
                "Morphism[_DomainElementT, _CodomainElementT]"
                if node.name == "hom"
                else "Morphism[_DomainElementT, _DomainElementT]"
            )
    write_tree(path, tree)


def main() -> None:
    refine_element()
    refine_parent()
    refine_map()
    refine_morphism()
    refine_homset()


if __name__ == "__main__":
    main()
