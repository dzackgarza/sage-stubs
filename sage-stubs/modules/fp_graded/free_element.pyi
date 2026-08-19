from collections.abc import Iterable
from typing import Generic, Self, TypeVar

from sage.modules.free_module_element import FreeModuleElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

class FreeGradedModuleElement(
    IndexedFreeModuleElement[GeneratorIndex, _AlgebraElement],
    Generic[_AlgebraElement],
):
    def parent(self) -> FreeGradedModule[_AlgebraElement]: ...
    def dense_coefficient_list(
        self,
        order: Iterable[GeneratorIndex] | None = ...,
    ) -> list[_AlgebraElement]: ...
    def degree(self) -> int | Integer: ...
    def lift_to_free(self) -> Self: ...
    def _lmul_(self, a: _AlgebraElement) -> Self: ...
    def vector_presentation(
        self,
    ) -> FreeModuleElement[RingElement] | None: ...
    def is_zero(self) -> bool: ...

from sage.modules.fp_graded.free_module import FreeGradedModule, GeneratorIndex
