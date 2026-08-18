from collections.abc import Mapping, Sequence
from typing import Generic, Self, TypeVar

from sage.matrix.matrix_dense import Matrix_dense
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_generic_dense(Matrix_dense[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        parent: Parent[Self],
        entries: Sequence[ElementConstructorInput]
        | Mapping[tuple[int, int], ElementConstructorInput]
        | ElementConstructorInput = ...,
        copy: bool = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def list(self) -> list[_Scalar]: ...
    def get_unsafe(self, i: int, j: int) -> _Scalar: ...
    def set_unsafe(self, i: int, j: int, value: _Scalar) -> None: ...
