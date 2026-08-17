#!/usr/bin/env python3
"""Verify scalar and module-element relationships in the free-module kernel."""

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


def require_return(node: ast.ClassDef, name: str, expected: str) -> None:
    function = method(node, name)
    if function is not None:
        actual = render(function.returns)
        assert actual == expected, f"{node.name}.{name}: {actual} != {expected}"


def check_module_parents() -> None:
    tree = parse("modules/module.pyi")
    module = class_named(tree, "Module")
    scalar_type, element_type = generic_parameters(module)
    assert has_base(module, f"Parent[{element_type}]")
    require_return(module, "base_ring", f"Ring[{scalar_type}]")
    require_return(module, "an_element", element_type)

    free = class_named(tree, "Module_free")
    free_scalar, free_element = generic_parameters(free)
    assert has_base(free, f"Module[{free_scalar}, {free_element}]")
    require_return(free, "base_ring", f"Ring[{free_scalar}]")
    require_return(free, "an_element", free_element)
    require_return(free, "gen", free_element)
    require_return(free, "gens", f"tuple[{free_element}, ...]")


def check_vector() -> None:
    vector = class_named(parse("modules/free_module_element.pyi"), "FreeModuleElement")
    (scalar_type,) = generic_parameters(vector)
    require_return(vector, "base_ring", f"Ring[{scalar_type}]")
    require_return(vector, "list", f"list[{scalar_type}]")
    require_return(vector, "__iter__", f"Iterator[{scalar_type}]")
    for name in ("dot_product", "inner_product", "hermitian_inner_product"):
        require_return(vector, name, scalar_type)


def check_free_module_parent() -> None:
    parent = class_named(parse("modules/free_module.pyi"), "FreeModule_generic")
    scalar_type, vector_type = generic_parameters(parent)
    acceptable = {
        f"Module_free[{scalar_type}, {vector_type}]",
        f"Module_free_ambient[{scalar_type}, {vector_type}]",
    }
    actual = {render(base) for base in parent.bases}
    assert actual & acceptable, (actual, acceptable)
    require_return(parent, "base_ring", f"Ring[{scalar_type}]")
    require_return(parent, "an_element", vector_type)
    require_return(parent, "gen", vector_type)
    require_return(parent, "gens", f"tuple[{vector_type}, ...]")


def main() -> None:
    check_module_parents()
    check_vector()
    check_free_module_parent()
    print("free-module kernel: scalar and vector contracts verified")


if __name__ == "__main__":
    main()
