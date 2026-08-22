from collections.abc import Sequence
from typing import Literal, Self, overload

from sage.interfaces.expect import Expect
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element

MAX_MODULUS: int

type _CharpolyAlgorithm = Literal["linbox", "generic", "all"]
type _MinpolyAlgorithm = Literal["linbox", "generic"]
type _EchelonAlgorithm = Literal["linbox", "linbox_noefd", "gauss", "all"]
type _KernelBasis = Literal["echelon", "pivot", "computed"]
type _PicklePayload = tuple[int, bool, bytes]


class Matrix_modn_dense_template(Matrix_dense[IntegerMod_abstract]):
    def __init__(
        self,
        parent: MatrixSpace[IntegerMod_abstract],
        entries: MatrixData[IntegerMod_abstract] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _pickle(self) -> tuple[_PicklePayload, Literal[10]]: ...
    def _unpickle(self, data: object, version: int) -> None: ...
    def __neg__(self) -> Self: ...
    def _lmul_(self, left: Element) -> Self: ...
    def __copy__(self) -> Self: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _richcmp_(self, right: Self, op: int) -> bool: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: _CharpolyAlgorithm = ...,
    ) -> Polynomial: ...
    def minpoly(
        self,
        var: str = ...,
        algorithm: _MinpolyAlgorithm = ...,
        proof: bool | None = ...,
    ) -> Polynomial: ...
    def _charpoly_linbox(self, var: str = ...) -> Polynomial: ...
    def echelonize(
        self,
        algorithm: _EchelonAlgorithm = ...,
        **kwds: object,
    ) -> None: ...

    @overload
    def _echelonize_linbox(
        self,
        efd: Literal[True] = ...,
    ) -> None: ...
    @overload
    def _echelonize_linbox(
        self,
        efd: Literal[False],
    ) -> tuple[int, ...]: ...
    @overload
    def _echelonize_linbox(
        self,
        efd: bool,
    ) -> tuple[int, ...] | None: ...

    def _echelon_in_place_classical(self) -> None: ...
    def pivots(self) -> tuple[int, ...]: ...
    def pivot_rows(self) -> tuple[int, ...]: ...
    def right_kernel_matrix(
        self,
        algorithm: _EchelonAlgorithm = ...,
        basis: _KernelBasis = ...,
    ) -> Self: ...
    def hessenbergize(self) -> None: ...
    def _charpoly_hessenberg(self, var: str) -> Polynomial: ...
    def rank(self) -> int | Integer: ...
    def determinant(self) -> IntegerMod_abstract: ...
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
    ) -> None: ...
    def _magma_init_(self, magma: Expect) -> str: ...
    def _export_as_string(self) -> str: ...
    def _list(self) -> list[IntegerMod_abstract]: ...
    def lift(self) -> Matrix_integer_dense: ...
    def transpose(self) -> Self: ...
    def submatrix(
        self,
        row: int = ...,
        col: int = ...,
        nrows: int = ...,
        ncols: int = ...,
    ) -> Self: ...
    def _matrices_from_rows(
        self,
        nrows: int,
        ncols: int,
    ) -> list[Self]: ...
    def matrix_from_columns(
        self,
        columns: Sequence[int],
    ) -> Self: ...
    def matrix_from_rows(
        self,
        rows: Sequence[int],
    ) -> Self: ...
    def matrix_from_rows_and_columns(
        self,
        rows: Sequence[int],
        columns: Sequence[int],
    ) -> Self: ...
    def __bool__(self) -> bool: ...


class Matrix_modn_dense_double(
    Matrix_modn_dense_template,
): ...
