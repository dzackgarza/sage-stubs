from collections.abc import Hashable, Iterable
from typing import Generic, Self, TypeVar

from sage.modules.free_module_element import FreeModuleElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_Index = TypeVar("_Index", bound=Hashable, default=int)
_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

class FPElement(
    IndexedFreeModuleElement[_Index, _AlgebraElement],
    Generic[_Index, _AlgebraElement],
):
    def lift_to_free(self) -> FreeGradedModuleElement[_Index, _AlgebraElement]: ...
    def degree(self) -> int | Integer: ...
    def dense_coefficient_list(
        self,
        order: Iterable[_Index] | None = ...,
    ) -> list[_AlgebraElement]: ...
    def _lmul_(self, a: _AlgebraElement) -> Self: ...
    def vector_presentation(self) -> FreeModuleElement[RingElement] | None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def normalize(self) -> Self: ...
