from collections.abc import Sequence
from typing import Generic, Literal, Self, TypeVar

from sage.matrix.matrix_space import MatrixData
from sage.matrix.matrix_sparse import Matrix_sparse
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix_generic_sparse(
    Matrix_sparse[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: Parent[Self],
        entries: MatrixData[_Scalar] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __bool__(self) -> bool: ...
    def _pickle(
        self,
    ) -> tuple[dict[tuple[int, int], _Scalar], Literal[0]]: ...
    def _unpickle(
        self,
        data: dict[tuple[int, int], _Scalar],
        version: int,
    ) -> None: ...
    def _add_(
        self,
        other: Matrix_generic_sparse[_Scalar],
    ) -> Self: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[_Scalar]: ...
    def _dict(self) -> dict[tuple[int, int], _Scalar]: ...
    def _nonzero_positions_by_row(
        self,
        copy: bool = ...,
    ) -> list[tuple[int, int]]: ...
    def _nonzero_positions_by_column(
        self,
        copy: bool = ...,
    ) -> list[tuple[int, int]]: ...


def Matrix_sparse_from_rows(
    X: Sequence[FreeModuleElement[_Scalar]],
) -> Matrix_sparse[_Scalar]: ...
