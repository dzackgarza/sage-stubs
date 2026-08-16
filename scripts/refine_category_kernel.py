#!/usr/bin/env python3
"""Reconstruct the generic Category/Parent/Element/Map/Morphism kernel.

This is deliberately narrow and source-specific. It does not infer types from
names or replace unknowns with a universal Sage element. Each transformation
encodes one invariant of Sage's categorical model:

* a ``Parent[E]`` constructs and contains elements of type ``E``;
* an element's parent is a ``Parent`` for that element type;
* a ``Map[D, C]`` has a parent-valued domain/codomain and sends ``D`` to ``C``;
* a ``Morphism[D, C]`` is a map with the same source and target element types;
* a ``Homset[M, D, C]`` is a parent for morphisms ``M`` from ``Parent[D]`` to
  ``Parent[C]``.

The script asserts the corresponding inheritance in the pinned Sage source
before changing a stub. It is safe to rerun and aborts rather than guessing
when the expected declaration is absent.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUB_ROOT = ROOT / "sage-stubs"
SOURCE_ROOT = ROOT / "sage-src" / "src" / "sage"


def expression(text: str) -> ast.expr:
    return ast.parse(text, mode="eval").body


def parse_statement(text: str) -> ast.stmt:
    module = ast.parse(text)
    if len(module.body) != 1:
        raise ValueError(text)
    return module.body[0]


def dotted_name(node: ast.expr) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    if isinstance(node, ast.Subscript):
        return dotted_name(node.value)
    return None


def source_class_bases(relative: str, class_name: str) -> set[str]:
    path = SOURCE_ROOT / relative
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".py":
        tree = ast.parse(text, filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                return {name for base in node.bases if (name := dotted_name(base))}
    else:
        # Cython class declarations are deliberately checked textually because
        # Python's AST does not parse ``cdef class``.
        import re

        match = re.search(
            rf"(?m)^\s*(?:cdef\s+)?class\s+{class_name}\s*(?:\(([^)]*)\))?\s*:",
            text,
        )
        if match:
            return {
                part.strip().split(".")[-1]
                for part in (match.group(1) or "").split(",")
                if part.strip()
            }
    raise RuntimeError(f"source class not found: {relative}:{class_name}")


def require_source_base(relative: str, class_name: str, base: str) -> None:
    bases = source_class_bases(relative, class_name)
    if base not in {name.split(".")[-1] for name in bases}:
        raise RuntimeError(
            f"pinned source no longer has {class_name}({base}, ...): {sorted(bases)}"
        )


def ensure_import_from(
    tree: ast.Module, module: str, names: tuple[str, ...]
) -> None:
    existing: ast.ImportFrom | None = None
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module == module and node.level == 0:
            existing = node
            break
    if existing is None:
        insertion = 1 if tree.body and isinstance(tree.body[0], ast.Expr) else 0
        tree.body.insert(
            insertion,
            ast.ImportFrom(
                module=module,
                names=[ast.alias(name=name) for name in names],
                level=0,
            ),
        )
        return
    present = {alias.name for alias in existing.names}
    existing.names.extend(ast.alias(name=name) for name in names if name not in present)


def ensure_assignment(tree: ast.Module, name: str, value: str) -> None:
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return
    assignment = parse_statement(f"{name} = {value}")
    insertion = 0
    while insertion < len(tree.body) and isinstance(
        tree.body[insertion], (ast.Expr, ast.Import, ast.ImportFrom)
    ):
        insertion += 1
    tree.body.insert(insertion, assignment)


def find_class(tree: ast.Module, name: str) -> ast.ClassDef:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
    raise RuntimeError(f"stub class not found: {name}")


def find_method(node: ast.ClassDef, name: str) -> ast.FunctionDef | ast.AsyncFunctionDef | None:
    for child in node.body:
        if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) and child.name == name:
            return child
    return None


def set_return(node: ast.ClassDef, method_name: str, annotation: str) -> None:
    method = find_method(node, method_name)
    if method is not None:
        method.returns = expression(annotation)


def set_parameter(
    node: ast.ClassDef, method_name: str, parameter_name: str, annotation: str
) -> None:
    method = find_method(node, method_name)
    if method is None:
        return
    arguments = [
        *method.args.posonlyargs,
        *method.args.args,
        *method.args.kwonlyargs,
    ]
    if method.args.vararg:
        arguments.append(method.args.vararg)
    if method.args.kwarg:
        arguments.append(method.args.kwarg)
    for argument in arguments:
        if argument.arg == parameter_name:
            argument.annotation = expression(annotation)
            return
    raise RuntimeError(f"{node.name}.{method_name} has no parameter {parameter_name}")


def add_generic_base(node: ast.ClassDef, parameters: str) -> None:
    for index, base in enumerate(node.bases):
        if dotted_name(base) == "Generic":
            node.bases[index] = expression(f"Generic[{parameters}]")
            return
    node.bases.append(expression(f"Generic[{parameters}]"))


def parameterize_base(node: ast.ClassDef, base_name: str, parameters: str) -> None:
    for index, base in enumerate(node.bases):
        if dotted_name(base) == base_name:
            node.bases[index] = expression(f"{base_name}[{parameters}]")
            return
    raise RuntimeError(f"{node.name} does not inherit from {base_name}")


def write_tree(path: Path, tree: ast.Module) -> None:
    ast.fix_missing_locations(tree)
    path.write_text(ast.unparse(tree) + "\n", encoding="utf-8")


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
    ensure_import_from(tree, "typing", ("Generic", "TypeVar"))
    ensure_assignment(
        tree,
        "_ParentElementT",
        'TypeVar("_ParentElementT", bound=Element, default=Element)',
    )
    parent = find_class(tree, "Parent")
    add_generic_base(parent, "_ParentElementT")
    for name in ("__call__", "_element_constructor_", "an_element", "gen", "zero", "one"):
        set_return(parent, name, "_ParentElementT")
    for name in ("gens", "_first_ngens"):
        set_return(parent, name, "tuple[_ParentElementT, ...]")
    set_return(parent, "some_elements", "list[_ParentElementT]")
    set_return(parent, "__iter__", "Iterator[_ParentElementT]")
    write_tree(path, tree)


def refine_map() -> None:
    require_source_base("categories/map.pyx", "Map", "Element")
    path = STUB_ROOT / "categories" / "map.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "typing", ("Generic", "TypeVar"))
    ensure_assignment(
        tree,
        "_MapDomainElementT",
        'TypeVar("_MapDomainElementT", bound=Element, default=Element)',
    )
    ensure_assignment(
        tree,
        "_MapCodomainElementT",
        'TypeVar("_MapCodomainElementT", bound=Element, default=Element)',
    )
    map_class = find_class(tree, "Map")
    add_generic_base(map_class, "_MapDomainElementT, _MapCodomainElementT")
    set_return(map_class, "domain", "Parent[_MapDomainElementT]")
    set_return(map_class, "codomain", "Parent[_MapCodomainElementT]")
    for name in ("__call__", "_call_", "_call_with_args"):
        set_parameter(map_class, name, "x", "_MapDomainElementT")
        set_return(map_class, name, "_MapCodomainElementT")
    set_return(map_class, "section", "Map[_MapCodomainElementT, _MapDomainElementT]")
    write_tree(path, tree)


def refine_morphism() -> None:
    require_source_base("categories/morphism.pyx", "Morphism", "Map")
    require_source_base("categories/morphism.pyx", "SetMorphism", "Morphism")
    path = STUB_ROOT / "categories" / "morphism.pyi"
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    ensure_import_from(tree, "typing", ("Generic", "TypeVar"))
    ensure_assignment(
        tree,
        "_MorphismDomainElementT",
        'TypeVar("_MorphismDomainElementT", bound=Element, default=Element)',
    )
    ensure_assignment(
        tree,
        "_MorphismCodomainElementT",
        'TypeVar("_MorphismCodomainElementT", bound=Element, default=Element)',
    )
    morphism = find_class(tree, "Morphism")
    parameterize_base(
        morphism,
        "Map",
        "_MorphismDomainElementT, _MorphismCodomainElementT",
    )
    add_generic_base(
        morphism, "_MorphismDomainElementT, _MorphismCodomainElementT"
    )
    set_morphism = find_class(tree, "SetMorphism")
    parameterize_base(
        set_morphism,
        "Morphism",
        "_MorphismDomainElementT, _MorphismCodomainElementT",
    )
    add_generic_base(
        set_morphism, "_MorphismDomainElementT, _MorphismCodomainElementT"
    )
    write_tree(path, tree)


def main() -> None:
    refine_element()
    refine_parent()
    refine_map()
    refine_morphism()


if __name__ == "__main__":
    main()
