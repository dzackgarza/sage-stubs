"""Shared source-surface and conservative type inference for Sage stub generation."""
from __future__ import annotations

import ast
from pathlib import Path

EXCLUDED = {"__init__.py", "all.py", "all_cmdline.py", "all_test.py", "tests.py"}
HEADER = """# Generated from the pinned Sage 10.7 source tree.\nfrom collections.abc import AsyncIterator, Iterator\nfrom typing import Self\n\nclass _SageObject: ...\n\n"""
SAFE = {"None", "bool", "int", "float", "complex", "str", "bytes", "bytearray", "memoryview", "slice", "range", "type", "object", "Self", "Iterator", "AsyncIterator"}
GENERIC = {"list", "tuple", "dict", "set", "frozenset", "type", "Iterator", "AsyncIterator"}
INT_NAMES = {"i", "j", "k", "m", "n", "p", "q", "r", "degree", "dimension", "length", "rank", "size", "start", "stop", "step", "prec", "precision"}
BOOL_NAMES = {"check", "coerce", "copy", "exact", "immutable", "normalize", "proof", "recurse", "reduce", "sparse", "strict", "validate", "verify"}
STR_NAMES = {"algorithm", "implementation", "label", "name", "prefix", "style", "variable_name"}
COMPARE = {"__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"}
ARITH = {"__add__", "__radd__", "__sub__", "__rsub__", "__mul__", "__rmul__", "__matmul__", "__rmatmul__", "__truediv__", "__rtruediv__", "__floordiv__", "__rfloordiv__", "__mod__", "__rmod__", "__pow__", "__rpow__", "__and__", "__rand__", "__or__", "__ror__", "__xor__", "__rxor__", "__lshift__", "__rlshift__", "__rshift__", "__rrshift__", "__pos__", "__neg__", "__abs__", "__invert__", "__copy__", "__deepcopy__"}
INPLACE = {"__iadd__", "__isub__", "__imul__", "__imatmul__", "__itruediv__", "__ifloordiv__", "__imod__", "__ipow__", "__iand__", "__ior__", "__ixor__", "__ilshift__", "__irshift__"}
NONE_RET = {"__init__", "__setitem__", "__delitem__", "__setattr__", "__delattr__", "__set_name__", "__init_subclass__"}


def in_scope(path: Path) -> bool:
    name = path.name
    return name.endswith((".py", ".pyx")) and name not in EXCLUDED and not name.startswith("test_") and not name.endswith("_test.py")


def public(name: str, method: bool = False) -> bool:
    return name.isidentifier() and (not name.startswith("_") or method and name.startswith("__") and name.endswith("__"))


def union(types: list[str]) -> str:
    out: list[str] = []
    for typ in types:
        for part in typ.split(" | "):
            if part not in out:
                out.append(part)
    return " | ".join(out) if out else "_SageObject"


def simple_annotation(node: ast.expr | None, local: set[str]) -> str | None:
    if node is None:
        return None
    if isinstance(node, ast.Constant):
        if node.value is None:
            return "None"
        if isinstance(node.value, str):
            try:
                return simple_annotation(ast.parse(node.value, mode="eval").body, local)
            except SyntaxError:
                return None
    if isinstance(node, ast.Name):
        return node.id if node.id in SAFE or node.id in local else None
    if isinstance(node, ast.Attribute):
        return node.attr if node.attr in SAFE or node.attr in local else None
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        left, right = simple_annotation(node.left, local), simple_annotation(node.right, local)
        return union([left, right]) if left and right else None
    if isinstance(node, ast.Subscript):
        base = node.value.id if isinstance(node.value, ast.Name) else node.value.attr if isinstance(node.value, ast.Attribute) else ""
        if base not in GENERIC:
            return None
        parts = node.slice.elts if isinstance(node.slice, ast.Tuple) else [node.slice]
        args = [simple_annotation(part, local) for part in parts]
        return f"{base}[{', '.join(args)}]" if all(args) else None
    return None


def literal_type(node: ast.expr | None) -> str | None:
    if node is None:
        return None
    if isinstance(node, ast.Constant):
        value = node.value
        if value is None: return "None"
        if isinstance(value, bool): return "bool"
        if isinstance(value, int): return "int"
        if isinstance(value, float): return "float"
        if isinstance(value, complex): return "complex"
        if isinstance(value, str): return "str"
        if isinstance(value, bytes): return "bytes"
    if isinstance(node, ast.List): return "list[_SageObject]"
    if isinstance(node, ast.Tuple): return "tuple[_SageObject, ...]"
    if isinstance(node, ast.Set): return "set[_SageObject]"
    if isinstance(node, ast.Dict): return "dict[_SageObject, _SageObject]"
    return None


def return_from_name(name: str) -> str:
    if name in NONE_RET: return "None"
    if name in COMPARE or name in {"__bool__", "__contains__"} or name.startswith(("is_", "has_", "can_")): return "bool"
    if name in {"__len__", "__hash__", "__index__", "__int__"}: return "int"
    if name == "__float__": return "float"
    if name == "__complex__": return "complex"
    if name in {"__str__", "__repr__", "__format__"}: return "str"
    if name == "__bytes__": return "bytes"
    if name in {"__iter__", "__reversed__"}: return "Iterator[_SageObject]"
    if name == "__aiter__": return "AsyncIterator[_SageObject]"
    if name in {"__enter__", "__new__"} or name in ARITH or name in INPLACE: return "Self"
    if name == "__exit__": return "bool | None"
    return "_SageObject"
