from collections.abc import Iterable
from typing import Generic, Self, TypeVar

from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

type GradedPieceElement = (
    FreeModuleElement[RingElement]
    | FGP_Element[RingElement]
)

class FPElement(
    IndexedFreeModuleElement[GeneratorIndex, _AlgebraElement],
    Generic[_AlgebraElement],
):
    def parent(self) -> FPModule[_AlgebraElement]: ...
    def lift_to_free(
        self,
    ) -> FreeGradedModuleElement[_AlgebraElement]: ...
    def degree(self) -> int | Integer: ...
    def dense_coefficient_list(
        self,
        order: Iterable[GeneratorIndex] | None = ...,
    ) -> list[_AlgebraElement]: ...
    def _lmul_(self, a: _AlgebraElement) -> Self: ...
    def vector_presentation(self) -> GradedPieceElement | None: ...
    def is_zero(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def normalize(self) -> Self: ...

from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import GeneratorIndex
from sage.modules.fp_graded.module import FPModule
