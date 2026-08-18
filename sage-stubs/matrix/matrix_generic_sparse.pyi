from collections.abc import Mapping, Sequence
from typing import Generic, Self, TypeVar

from sage.matrix.matrix_sparse import Matrix_sparse
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_generic_sparse(Matrix_sparse[_Scalar], Generic[_Scalar]):
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
    def dict(self, copy: bool = ...) -> dict[tuple[int, int], _Scalar]: ...
    def get_unsafe(self, i: int, j: int) -> _Scalar: ...
    def set_unsafe(self, i: int, j: int, value: _Scalar) -> None: ...


def Matrix_sparse_from_rows(
    rows: Sequence[Mapping[int, _Scalar]],
) -> Matrix_generic_sparse[_Scalar]: ...
