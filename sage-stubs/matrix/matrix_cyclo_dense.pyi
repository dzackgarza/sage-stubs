from collections.abc import Sequence
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


class Matrix_cyclo_dense(Matrix_dense[NumberFieldElement]):
    def __init__(
        self,
        parent: MatrixSpace[NumberFieldElement],
        entries: MatrixData[NumberFieldElement] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _lmul_(self, right: NumberFieldElement) -> Self: ...
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
    def set_immutable(self) -> None: ...

    # Rational-coordinate representation and archimedean bounds
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

    # Multimodular characteristic polynomial and echelon form
    def _charpoly_bound(self) -> Integer: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: CyclotomicCharpolyAlgorithm = ...,
        proof: bool | None = ...,
    ) -> Polynomial: ...
    characteristic_polynomial = charpoly
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
