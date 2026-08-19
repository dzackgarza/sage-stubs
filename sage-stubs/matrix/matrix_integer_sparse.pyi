from typing import Literal, Self, overload

from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_modn_sparse import Matrix_modn_sparse
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.matrix.matrix_rational_sparse import Matrix_rational_sparse
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.matrix.matrix_sparse import Matrix_sparse
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_integer_dense_flint import (
    Polynomial_integer_dense_flint,
)
from sage.rings.rational import Rational
from sage.structure.parent import Parent

type IntegerSparseRankAlgorithm = Literal["linbox", "generic"] | None
type IntegerSparseKernelAlgorithm = Literal[
    "default",
    "flint",
    "pari",
    "padic",
    "iml",
]
type IntegerSparseKernelTag = Literal[
    "computed-flint-int",
    "computed-pari-int",
    "computed-iml-int",
]


class Matrix_integer_sparse(Matrix_sparse[Integer]):
    def __init__(
        self,
        parent: MatrixSpace[Integer],
        entries: MatrixData[Integer] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _dict(self) -> dict[tuple[int, int], Integer]: ...
    def dict(
        self,
        copy: bool = ...,
    ) -> dict[tuple[int, int], Integer]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def _lmul_(self, right: Integer) -> Self: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _nonzero_positions_by_row(
        self,
        copy: bool = ...,
    ) -> list[tuple[int, int]]: ...
    def _nonzero_positions_by_column(
        self,
        copy: bool = ...,
    ) -> list[tuple[int, int]]: ...

    # Modular reduction and rational reconstruction
    def _mod_int(
        self,
        modulus: int | Integer,
    ) -> Matrix_modn_sparse: ...
    def rational_reconstruction(
        self,
        N: int | Integer,
    ) -> Matrix_rational_sparse: ...

    # Integer normal forms and exact invariants
    def _right_kernel_matrix(
        self,
        algorithm: IntegerSparseKernelAlgorithm = ...,
        **kwds: object,
    ) -> tuple[IntegerSparseKernelTag, Matrix_integer_dense]: ...
    def elementary_divisors(
        self,
        algorithm: Literal["pari", "linbox"] = ...,
    ) -> list[Integer]: ...

    @overload
    def smith_form(
        self,
        transformation: Literal[False],
        integral: Parent | Literal[True] | None = ...,
    ) -> Matrix_integer_dense: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[True] = ...,
        integral: Parent | Literal[True] | None = ...,
    ) -> tuple[
        Matrix_integer_dense,
        Matrix_integer_dense,
        Matrix_integer_dense,
    ]: ...

    def rank(
        self,
        algorithm: IntegerSparseRankAlgorithm = ...,
    ) -> int: ...
    def _rank_linbox(self) -> int: ...
    def _det_linbox(self) -> Integer: ...
    def determinant(
        self,
        algorithm: str | None = ...,
    ) -> Integer: ...
    det = determinant
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial_integer_dense_flint: ...
    characteristic_polynomial = charpoly
    def minpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial_integer_dense_flint: ...
    minimal_polynomial = minpoly

    # LinBox solving over the rational field
    @overload
    def _solve_right_nonsingular_square(
        self,
        B: Matrix_integer_sparse | Matrix_integer_dense,
        algorithm: str | None = ...,
        check_rank: bool = ...,
    ) -> Matrix_rational_dense: ...
    @overload
    def _solve_right_nonsingular_square(
        self,
        B: FreeModuleElement[Integer],
        algorithm: str | None = ...,
        check_rank: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    def _solve_vector_linbox(
        self,
        v: FreeModuleElement[Integer],
        algorithm: str | None = ...,
    ) -> tuple[Vector_integer_dense, Integer]: ...
    def dense_matrix(self) -> Matrix_integer_dense: ...
