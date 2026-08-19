from collections.abc import Mapping, Sequence
from typing import Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput


type _MatrixEntries = (
    ElementConstructorInput
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | None
)


class Matrix_modn_dense_double(Matrix_dense[IntegerMod_abstract]):
    def __init__(
        self,
        parent: MatrixSpace[IntegerMod_abstract],
        entries: _MatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def _list(self) -> list[IntegerMod_abstract]: ...
    def list(self) -> list[IntegerMod_abstract]: ...
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
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _lmul_(self, right: IntegerMod_abstract) -> Self: ...
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str = ...,
    ) -> Polynomial: ...
    characteristic_polynomial = charpoly
    def minpoly(
        self,
        var: str = ...,
        algorithm: str = ...,
        proof: bool | None = ...,
    ) -> Polynomial: ...
    minimal_polynomial = minpoly
    def determinant(self, algorithm: str = ...) -> IntegerMod_abstract: ...
    det = determinant
    def rank(self, algorithm: str = ...) -> int: ...
    def trace(self) -> IntegerMod_abstract: ...
    def echelonize(
        self,
        algorithm: str = ...,
        **kwds: object,
    ) -> None: ...
    def echelon_form(
        self,
        algorithm: str = ...,
        **kwds: object,
    ) -> Self: ...
    def _pivots(self) -> list[int]: ...
    def transpose(self) -> Self: ...
    def augment(
        self,
        right: Self | FreeModuleElement[IntegerMod_abstract],
        subdivide: bool = ...,
    ) -> Self: ...
    def submatrix(
        self,
        row: int = ...,
        col: int = ...,
        nrows: int = ...,
        ncols: int = ...,
    ) -> Self: ...
    def __invert__(self) -> Self: ...
    inverse = __invert__
    def solve_right(
        self,
        B: Self | FreeModuleElement[IntegerMod_abstract],
    ) -> Self | FreeModuleElement[IntegerMod_abstract]: ...
