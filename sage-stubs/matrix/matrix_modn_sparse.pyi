from collections.abc import Iterable, Mapping
from typing import Literal, Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.matrix.matrix_sparse import Matrix_sparse
from sage.rings.finite_rings.integer_mod import IntegerMod_int
from sage.rings.rational import Rational

MAX_MODULUS: int

type ModularSparseAlgorithm = Literal["linbox", "generic"] | None
type _SparseEntries = Mapping[tuple[int, int], IntegerMod_int]


class Matrix_modn_sparse(Matrix_sparse[IntegerMod_int]):
    def __init__(
        self,
        parent: MatrixSpace[IntegerMod_int],
        entries: MatrixData[IntegerMod_int] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _dict(self) -> dict[tuple[int, int], IntegerMod_int]: ...
    def _pickle(
        self,
    ) -> tuple[dict[tuple[int, int], IntegerMod_int], Literal[1]]: ...
    def _unpickle(
        self,
        data: _SparseEntries,
        version: int,
    ) -> None: ...
    def _matrix_times_matrix_dense(
        self,
        right: Self,
    ) -> Matrix_dense[IntegerMod_int]: ...
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
    ) -> tuple[int, IntegerMod_int]: ...
    def rank(
        self,
        algorithm: ModularSparseAlgorithm = ...,
    ) -> int: ...
    def determinant(
        self,
        algorithm: ModularSparseAlgorithm = ...,
    ) -> IntegerMod_int: ...
