from collections.abc import Callable
from typing import TypeVar

from sage.structure.sage_object import SageObject

_T = TypeVar("_T")
_U = TypeVar("_U")
op_LT: int
op_LE: int
op_EQ: int
op_NE: int
op_GT: int
op_GE: int

def richcmp(x: _T, y: _U, op: int) -> bool: ...
def richcmp_item(x: object, y: object, op: int) -> bool: ...
def richcmp_method(cls) -> type[SageObject]: ...
def richcmp_by_eq_and_lt(
    eq_attr: str, lt_attr: str
) -> Callable[[object, int], bool]: ...
