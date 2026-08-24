from __future__ import annotations

from typing import Generic, Self, TypeVar

from sage.algebras.free_algebra_quotient import (
    FreeAlgebraQuotient,
    FreeAlgebraQuotientElementInput,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import AlgebraElement, RingElement

_Coefficient = TypeVar(
    "_Coefficient",
    bound=RingElement,
    default=RingElement,
)


class FreeAlgebraQuotientElement(
    AlgebraElement,
    Generic[_Coefficient],
):
    def __init__(
        self,
        A: FreeAlgebraQuotient[_Coefficient],
        x: FreeAlgebraQuotientElementInput[_Coefficient],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def vector(self) -> FreeModuleElement[_Coefficient]: ...
    def _richcmp_(self, other: Self, op: int) -> bool: ...
    def __neg__(self) -> Self: ...
    def _add_(self, y: Self) -> Self: ...
    def _sub_(self, y: Self) -> Self: ...
    def _mul_(self, y: Self) -> Self: ...
    def _rmul_(self, c: _Coefficient | int | Integer) -> Self: ...
    def _lmul_(self, c: _Coefficient | int | Integer) -> Self: ...
