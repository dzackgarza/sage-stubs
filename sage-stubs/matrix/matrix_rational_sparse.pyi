from collections.abc import Mapping, Sequence
from typing import Literal, Self

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_integer_sparse import Matrix_integer_sparse
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.matrix.matrix_sparse import Matrix_sparse
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import RingElement

type RationalSparseKernelAlgorithm = Literal[
    "default",
    "padic",
    "linbox",
]
type RationalSparseKernelTag = Literal[
    "computed-iml-rational",
    "computed-linbox-rational",
]


class Matrix_rational_sparse(Matrix_sparse[Rational]):
    def __init__(
        self,
        parent: MatrixSpace[Rational],
        entries: MatrixData[Rational] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def add_to_entry(
        self,
        i: int,
        j: int,
        elt: int | Integer | Rational,
    ) -> None: ...
    def _matrix_times_matrix_dense(
        self,
        right: Self,
    ) -> Matrix_rational_dense: ...
    def _dict(self) -> dict[tuple[int, int], Rational]: ...
    def _nonzero_positions_by_row(
        self,
        copy: bool = ...,
    ) -> list[tuple[int, int]]: ...

    # Height and denominator control
    def height(self) -> Integer: ...
    def denominator(self) -> Integer: ...
    def _clear_denom(
        self,
    ) -> tuple[Matrix_integer_sparse, Integer]: ...

    # Exact sparse echelonization
    def echelonize(
        self,
        height_guess: int | Integer | None = ...,
        proof: bool = ...,
        **kwds: object,
    ) -> None: ...
    def echelon_form(
        self,
        algorithm: str = ...,
        height_guess: int | Integer | None = ...,
        proof: bool = ...,
        **kwds: object,
    ) -> Self: ...
    def _echelonize_multimodular(
        self,
        height_guess: int | Integer | None = ...,
        proof: bool = ...,
        **kwds: object,
    ) -> tuple[int, ...]: ...
    def _echelon_form_multimodular(
        self,
        height_guess: int | Integer | None = ...,
        proof: bool = ...,
    ) -> tuple[Self, tuple[int, ...]]: ...
    def set_row_to_multiple_of_row(
        self,
        i: int,
        j: int,
        s: int | Integer | Rational,
    ) -> None: ...
    def dense_matrix(self) -> Matrix_rational_dense: ...
    def _set_row_to_negative_of_row_of_A_using_subset_of_columns(
        self,
        i: int,
        A: Matrix[RingElement],
        r: int,
        cols: Sequence[int],
        cols_index: Mapping[int, int] | None = ...,
    ) -> None: ...

    # Rational kernel bases
    def _right_kernel_matrix(
        self,
        algorithm: RationalSparseKernelAlgorithm = ...,
        proof: bool | None = ...,
    ) -> tuple[
        RationalSparseKernelTag,
        Matrix_rational_dense | Matrix_rational_sparse,
    ]: ...
    def _right_kernel_matrix_linbox(
        self,
    ) -> tuple[
        Literal["computed-linbox-rational"],
        Matrix_rational_sparse,
    ]: ...
