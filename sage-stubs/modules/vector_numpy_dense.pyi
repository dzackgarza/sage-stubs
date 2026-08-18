from collections.abc import Sequence
from typing import Generic, Self, TypeVar

from numpy import ndarray

from sage.modules.free_module_element import FreeModuleElement_generic_dense
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Vector_numpy_dense(
    FreeModuleElement_generic_dense[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: object,
        entries: ndarray | Sequence[ElementConstructorInput] = ...,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def numpy(self, copy: bool = ...) -> ndarray: ...
    def list(self, copy: bool = ...) -> list[_Scalar]: ...
    def dot_product(self, right: Vector_numpy_dense[_Scalar]) -> _Scalar: ...
    inner_product = dot_product
    def pairwise_product(self, right: Vector_numpy_dense[_Scalar]) -> Self: ...
