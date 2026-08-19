from collections.abc import Iterable
from typing import Literal, Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.matrix.matrix_sparse import Matrix_sparse
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.rational import Rational

type ModularSparseAlgorithm = Literal["linbox", "generic"] | None


class Matrix_modn_sparse(Matrix_sparse[IntegerMod_abstract]):
    def __init__(
        self,
        parent: MatrixSpace[IntegerMod_abstract],
        entries: MatrixData[IntegerMod_abstract] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _dict(
        self,
    ) -> dict[tuple[int, int], IntegerMod_abstract]: ...
    def dict(
        self,
        copy: bool = ...,
    ) -> dict[tuple[int, int], IntegerMod_abstract]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[IntegerMod_abstract]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[IntegerMod_abstract]: ...
    def _pickle(
        self,
    ) -> tuple[
        dict[tuple[int, int], IntegerMod_abstract],
        Literal[1],
    ]: ...
    def _unpickle(
        self,
        data: dict[tuple[int, int], IntegerMod_abstract],
        version: Literal[1],
    ) -> None: ...
    def _matrix_times_matrix_dense(
        self,
        right: Self,
    ) -> Matrix_dense[IntegerMod_abstract]: ...
    def swap_rows(
        self,
        r1: int,
        r2: int,
    ) -> None: ...
    def _echelon_in_place(
        self,
        algorithm: str,
    ) -> None: ...
    def _nonzero_positions_by_row(
        self,
        copy: bool = ...,
    ) -> list[tuple[int, int]]: ...
    def density(self) -> Rational: ...
    def transpose(self) -> Self: ...
    def matrix_from_rows(
        self,
        rows: Iterable[int],
    ) -> Self: ...
    def matrix_from_columns(
        self,
        cols: Iterable[int],
    ) -> Self: ...
    def _rank_det_linbox(
        self,
    ) -> tuple[int, IntegerMod_abstract]: ...
    def rank(
        self,
        algorithm: ModularSparseAlgorithm = ...,
    ) -> int: ...
    def determinant(
        self,
        algorithm: ModularSparseAlgorithm = ...,
    ) -> IntegerMod_abstract: ...
    det = determinant
