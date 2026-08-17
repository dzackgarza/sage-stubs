#!/usr/bin/env python3
"""Reconstruct scalar and element types for Sage modules and free modules.

A module has two different mathematical parameters:

* the scalar elements of its base ring; and
* the elements of the module itself.

The generated stubs conflated or erased these.  This pass preserves both
parameters through ``Module``, ``Module_free``, ``FreeModule_generic``, and
``FreeModuleElement``.  Inheritance is checked against the pinned Sage source.
"""

from __future__ import annotations

import ast

from refine_category_kernel import (
    SOURCE_ROOT,
    STUB_ROOT,
    add_generic_base,
    dotted_name,
    ensure_assignment,
    ensure_import_from,
    find_class,
    parameterize_base,
    set_parameter,
    set_return,
    source_class_bases,
    write_tree,
)
from refine_category_kernel_v2 import generic_parameters


def pinned_source(stem: str) -> str:
    candidates = (f"{stem}.pyx", f"{stem}.py")
    existing = [candidate for candidate in candidates if (SOURCE_ROOT / candidate).is_file()]
    if len(existing) != 1:
        raise RuntimeError(f"expected one pinned source for {stem}; found {existing}")
    return existing[0]


def source_base(relative: str, class_name: str, allowed: set[str]) -> str:
    bases = {base.split(".")[-1] for base in source_class_bases(relative, class_name)}
    matches = bases & allowed
    if len(matches) != 1:
        raise RuntimeError(
            f"expected one of {sorted(allowed)} for {relative}:{class_name}; "
            f"found {sorted(bases)}"
        )
    return matches.pop()


def generic_base(node: ast.ClassDef) -> ast.Subscript | None:
    for base in node.bases:
        if dotted_name(base) == "Generic" and isinstance(base, ast.Subscript):
            return base
    return None


def module_parameters(
    tree: ast.Module,
    node: ast.ClassDef,
    *,
    scalar_name: str,
    element_name: str,
) -> tuple[str, str]:
    """Return `(scalar, module_element)` parameters, preserving a known element type."""
    current = generic_parameters(node)
    if len(current) == 2:
        return current[0], current[1]
    if len(current) > 2:
        raise RuntimeError(f"unexpected generic arity for {node.name}: {current}")

    ensure_import_from(tree, "typing", ("Generic", "TypeVar"))
    ensure_assignment(
        tree,
        scalar_name,
        f'TypeVar("{scalar_name}", bound=RingElement, default=RingElement)',
    )
    if len(current) == 1:
        element_type = current[0]
    else:
        ensure_assignment(
            tree,
            element_name,
            f'TypeVar("{element_name}", bound=ModuleElement, default=ModuleElement)',
        )
        element_type = element_name
    scalar_type = scalar_name
    base = generic_base(node)
    replacement = ast.parse(
        f"Generic[{scalar_type}, {element_type}]", mode="eval"
    ).body
    if base is None:
        node.bases.append(replacement)
    else:
        node.bases[node.bases.index(base)] = replacement
    return scalar_type, element_type


def scalar_parameter(
    tree: ast.Module,
    node: ast.ClassDef,
    *,
    name: str,
) -> str:
    current = generic_parameters(node)
    if len(current) == 1:
        return current[0]
    if current:
        raise RuntimeError(f"unexpected generic arity for {node.name}: {current}")
    ensure_import_from(tree, "typing", ("Generic", "TypeVar"))
    ensure_assignment(
        tree,
        name,
        f'TypeVar("{name}", bound=RingElement, default=RingElement)',
    )
    add_generic_base(node, name)
    return name


def refine_module_parents() -> None:
    source = pinned_source("modules/module")
    module_base = source_base(source, "Module", {"Parent"})
    free_base = source_base(source, "Module_free", {"Module"})

    path = STUB_ROOT / "modules" / "module.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "sage.structure.element", ("Element", "ModuleElement", "RingElement"))
    ensure_import_from(tree, "sage.rings.ring", ("Ring",))

    module = find_class(tree, "Module")
    scalar_type, element_type = module_parameters(
        tree,
        module,
        scalar_name="_ModuleScalarT",
        element_name="_ModuleElementT",
    )
    parameterize_base(module, module_base, element_type)
    set_return(module, "base_ring", f"Ring[{scalar_type}]")
    for name in ("__call__", "an_element", "zero"):
        set_return(module, name, element_type)

    module_free = find_class(tree, "Module_free")
    free_scalar, free_element = module_parameters(
        tree,
        module_free,
        scalar_name="_FreeModuleScalarT",
        element_name="_FreeModuleElementT",
    )
    parameterize_base(module_free, free_base, f"{free_scalar}, {free_element}")
    set_return(module_free, "base_ring", f"Ring[{free_scalar}]")
    for name in ("__call__", "an_element", "zero", "gen"):
        set_return(module_free, name, free_element)
    set_return(module_free, "gens", f"tuple[{free_element}, ...]")
    write_tree(path, tree)


def refine_free_module_element() -> None:
    source = pinned_source("modules/free_module_element")
    actual_base = source_base(source, "FreeModuleElement", {"Vector", "ModuleElement"})

    path = STUB_ROOT / "modules" / "free_module_element.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "collections.abc", ("Iterator",))
    ensure_import_from(tree, "sage.structure.element", ("RingElement",))
    ensure_import_from(tree, "sage.rings.ring", ("Ring",))

    vector = find_class(tree, "FreeModuleElement")
    scalar_type = scalar_parameter(tree, vector, name="_VectorScalarT")
    parameterize_base(vector, actual_base, scalar_type) if any(
        dotted_name(base) == actual_base and isinstance(base, ast.Subscript)
        for base in vector.bases
    ) else None
    set_return(vector, "base_ring", f"Ring[{scalar_type}]")
    set_return(vector, "list", f"list[{scalar_type}]")
    set_return(vector, "__iter__", f"Iterator[{scalar_type}]")
    for name in ("dot_product", "inner_product", "hermitian_inner_product"):
        set_parameter(vector, name, "right", f"FreeModuleElement[{scalar_type}]")
        set_return(vector, name, scalar_type)
    write_tree(path, tree)


def refine_free_module_parent() -> None:
    source = pinned_source("modules/free_module")
    actual_base = source_base(
        source,
        "FreeModule_generic",
        {"Module_free", "Module_free_ambient"},
    )

    path = STUB_ROOT / "modules" / "free_module.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "sage.structure.element", ("ModuleElement", "RingElement"))
    ensure_import_from(tree, "sage.rings.ring", ("Ring",))
    ensure_import_from(tree, "sage.modules.free_module_element", ("FreeModuleElement",))

    parent = find_class(tree, "FreeModule_generic")
    scalar_type, vector_type = module_parameters(
        tree,
        parent,
        scalar_name="_FreeModuleCoefficientT",
        element_name="_FreeModuleVectorT",
    )
    parameterize_base(parent, actual_base, f"{scalar_type}, {vector_type}")
    set_return(parent, "base_ring", f"Ring[{scalar_type}]")
    for name in ("__call__", "an_element", "zero", "gen"):
        set_return(parent, name, vector_type)
    set_return(parent, "gens", f"tuple[{vector_type}, ...]")
    write_tree(path, tree)


def main() -> None:
    refine_module_parents()
    refine_free_module_element()
    refine_free_module_parent()


if __name__ == "__main__":
    main()
