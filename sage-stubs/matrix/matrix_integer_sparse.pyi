from collections.abc import Sequence
from typing import Literal, Self, overload

from sage.matrix.matrix import Matrix
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
type IntegerSparseKernelTag = Literal[
    "computed-flint-int",
    "computed-pari-int",
    "computed-iml-int",
]
type LinboxSolveAlgorithm = Literal[
    "default",
    "dense_elimination",
    "sparse_elimination",
    "blackbox",
    "wiedemann",
] | None
type IntegerSparseSolveAlgorithm = (
    LinboxSolveAlgorithm
    | Literal[
        "linbox",
        "linbox_default",
        "linbox_dense_elimination",
        "linbox_sparse_elimination",
        "linbox_blackbox",
        "linbox_wiedemann",
        "generic",
    ]
)


class Matrix_integer_sparse(Matrix_sparse[Integer]):
    def __init__(
        self,
        parent: MatrixSpace[Integer],
        entries: MatrixData[Integer] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _lmul_(self, right: Integer) -> Self: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _dict(self) -> dict[tuple[int, int], Integer]: ...
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
        **kwds: object,
    ) -> tuple[IntegerSparseKernelTag, Matrix_integer_dense]: ...
    hermite_form = Matrix.echelon_form

    def elementary_divisors(
        self,
        algorithm: Literal["pari", "linbox"] = ...,
    ) -> list[Integer]: ...

    @overload
    def smith_form(
        self,
        transformation: Literal[True] = ...,
        integral: Parent[Integer] | Literal[True] | None = ...,
    ) -> tuple[
        Matrix_integer_dense,
        Matrix_integer_dense,
        Matrix_integer_dense,
    ]: ...
    @overload
    def smith_form(
        self,
        transformation: Literal[False],
        integral: Parent[Integer] | Literal[True] | None = ...,
    ) -> Matrix_integer_dense: ...
    @overload
    def smith_form(
        self,
        transformation: bool = ...,
        integral: Parent[Integer] | Literal[True] | None = ...,
    ) -> (
        Matrix_integer_dense
        | tuple[
            Matrix_integer_dense,
            Matrix_integer_dense,
            Matrix_integer_dense,
        ]
    ): ...

    def rank(
        self,
        algorithm: IntegerSparseRankAlgorithm = ...,
    ) -> int: ...
    def _rank_linbox(self) -> int: ...
    def _det_linbox(self) -> Integer: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial_integer_dense_flint: ...
    def _charpoly_linbox(
        self,
        var: str = ...,
    ) -> Polynomial_integer_dense_flint: ...
    def minpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial_integer_dense_flint: ...
    def _minpoly_linbox(
        self,
        var: str = ...,
    ) -> Polynomial_integer_dense_flint: ...

    # LinBox solving over the rational field
    @overload
    def _solve_right_nonsingular_square(
        self,
        B: Matrix[Integer],
        algorithm: IntegerSparseSolveAlgorithm = ...,
        check_rank: bool = ...,
    ) -> Matrix_rational_dense: ...
    @overload
    def _solve_right_nonsingular_square(
        self,
        B: FreeModuleElement[Integer],
        algorithm: IntegerSparseSolveAlgorithm = ...,
        check_rank: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    def _solve_vector_linbox(
        self,
        v: FreeModuleElement[Integer],
        algorithm: LinboxSolveAlgorithm = ...,
    ) -> tuple[Vector_integer_dense, Integer]: ...
    def _solve_matrix_linbox(
        self,
        mat: Matrix[Integer] | Sequence[Sequence[int | Integer]],
        algorithm: LinboxSolveAlgorithm = ...,
    ) -> tuple[Matrix_integer_dense, Vector_integer_dense]: ...
