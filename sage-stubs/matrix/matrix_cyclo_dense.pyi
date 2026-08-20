from collections.abc import Callable, Mapping, Sequence
from typing import Literal, Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.parent import ElementConstructorInput


type CyclotomicCharpolyAlgorithm = Literal[
    "multimodular",
    "pari",
    "hessenberg",
]
type CyclotomicEchelonAlgorithm = Literal[
    "multimodular",
    "classical",
]
type CyclotomicRandomDistribution = Literal["1/n"] | None
type CyclotomicMatrixEntries = (
    MatrixData[NumberFieldElement]
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | ElementConstructorInput
    | None
)


class Matrix_cyclo_dense(Matrix_dense[NumberFieldElement]):
    def __init__(
        self,
        parent: MatrixSpace[NumberFieldElement],
        entries: CyclotomicMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __bool__(self) -> bool: ...
    def __neg__(self) -> Self: ...
    def _list(self) -> list[NumberFieldElement]: ...
    def list(self) -> list[NumberFieldElement]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[NumberFieldElement]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[NumberFieldElement]: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _lmul_(self, right: NumberFieldElement) -> Self: ...
    def _multiply_classical(self, right: Self) -> Self: ...
    def transpose(self) -> Self: ...
    T = transpose
    def set_immutable(self) -> None: ...

    def _rational_matrix(self) -> Matrix_rational_dense: ...
    def denominator(self) -> Integer: ...
    def coefficient_bound(self) -> Rational: ...
    def height(self) -> RealNumber: ...
    def randomize(
        self,
        density: float = ...,
        num_bound: int | Integer = ...,
        den_bound: int | Integer = ...,
        distribution: CyclotomicRandomDistribution = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...

    def _charpoly_bound(self) -> Integer: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: CyclotomicCharpolyAlgorithm = ...,
        proof: bool | None = ...,
    ) -> Polynomial: ...
    characteristic_polynomial = charpoly
    def minpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    minimal_polynomial = minpoly
    def echelonize(
        self,
        algorithm: CyclotomicEchelonAlgorithm = ...,
        height_guess: int | Integer | Rational | RealNumber | None = ...,
    ) -> None: ...
    def echelon_form(
        self,
        algorithm: CyclotomicEchelonAlgorithm = ...,
        height_guess: int | Integer | Rational | RealNumber | None = ...,
    ) -> Self: ...
    def _echelon_form_multimodular(
        self,
        num_primes: int | Integer = ...,
        height_guess: int | Integer | Rational | RealNumber | None = ...,
    ) -> Self: ...
    def pivots(self) -> tuple[int, ...]: ...
    def rank(self) -> int: ...
    def determinant(
        self,
        algorithm: str = ...,
        proof: bool | None = ...,
    ) -> NumberFieldElement: ...
    det = determinant
    def trace(self) -> NumberFieldElement: ...
    def is_invertible(self) -> bool: ...
    def inverse(self) -> Self: ...
    __invert__ = inverse
    def solve_right(
        self,
        B: Self | FreeModuleElement[NumberFieldElement],
    ) -> Self | FreeModuleElement[NumberFieldElement]: ...
    def solve_left(
        self,
        B: Self | FreeModuleElement[NumberFieldElement],
    ) -> Self | FreeModuleElement[NumberFieldElement]: ...
