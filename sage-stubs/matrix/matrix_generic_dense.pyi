from typing import Generic, Literal, Self, TypeVar

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixData
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_generic_dense(
    Matrix_dense[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: Parent[Self],
        entries: MatrixData[_Scalar] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _reverse_unsafe(self) -> None: ...
    def _pickle(self) -> tuple[list[_Scalar], Literal[0]]: ...
    def _unpickle(
        self,
        data: list[_Scalar],
        version: int,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _add_(
        self,
        right: Matrix_generic_dense[_Scalar],
    ) -> Self: ...
    def _sub_(
        self,
        right: Matrix_generic_dense[_Scalar],
    ) -> Self: ...
    def _multiply_classical(
        self,
        right: Matrix[_Scalar],
    ) -> Self: ...
    def _list(self) -> list[_Scalar]: ...
