from typing import Generic, Self, TypeVar

from numpy import ndarray

from sage.modules.free_module_element import FreeModuleElement_generic_dense
from sage.structure.element import RingElement

_DoubleScalar = TypeVar(
    "_DoubleScalar",
    bound=RingElement,
    default=RingElement,
)


class Vector_double_dense(
    FreeModuleElement_generic_dense[_DoubleScalar],
    Generic[_DoubleScalar],
):
    def numpy(self) -> ndarray: ...
    def norm(self, p: int | float | str = ...) -> float: ...
    def dot_product(
        self,
        right: Vector_double_dense[_DoubleScalar],
    ) -> _DoubleScalar: ...
    inner_product = dot_product
    def pairwise_product(
        self,
        right: Vector_double_dense[_DoubleScalar],
    ) -> Self: ...
