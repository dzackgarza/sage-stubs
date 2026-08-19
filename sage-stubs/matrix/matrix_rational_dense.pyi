from collections.abc import Callable, Mapping, Sequence
from typing import Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.parent import ElementConstructorInput


type _RationalMatrixEntries = (
    int
    | Integer
    | Rational
    | Sequence[int | Integer | Rational | ElementConstructorInput]
    | Sequence[Sequence[int | Integer | Rational | ElementConstructorInput]]
    | Mapping[tuple[int, int], int | Integer | Rational | ElementConstructorInput]
    | Callable[[int, int], int | Integer | Rational | ElementConstructorInput]
    | ElementConstructorInput
    | None
)


class Matrix_rational_dense(Matrix_dense[Rational]):
    def __init__(
        self,
        parent: MatrixSpace[Rational],
        entries: _RationalMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[Rational]: ...
    def list(self) -> list[Rational]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[Rational]: ...
    def transpose(self) -> Self: ...
    def antitranspose(self) -> Self: ...
    def determinant(self, algorithm: str = ...) -> Rational: ...
    det = determinant
    def rank(self, algorithm: str = ...) -> int: ...
    def trace(self) -> Rational: ...
    def denominator(self) -> Integer: ...
    def height(self) -> Integer: ...
    def characteristic_polynomial(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def minimal_polynomial(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    minpoly = minimal_polynomial
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
    def inverse(self) -> Self: ...
    __invert__ = inverse
    def solve_right(
        self,
        B: Self | FreeModuleElement[Rational],
    ) -> Self | FreeModuleElement[Rational]: ...
    def solve_left(
        self,
        B: Self | FreeModuleElement[Rational],
    ) -> Self | FreeModuleElement[Rational]: ...
    def clear_denominators(self) -> Matrix_integer_dense: ...
    def integer_matrix(self) -> tuple[Matrix_integer_dense, Integer]: ...
    def rational_reconstruction(
        self,
        modulus: int | Integer,
    ) -> Self: ...
