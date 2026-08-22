from collections.abc import Callable, Mapping, Sequence
from typing import Literal, Self

from sage.matrix.matrix0 import Matrix as Matrix_base
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.element import RingElement
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
type CyclotomicPickleData = tuple[str, int]
type CyclotomicReductionMatrix = Matrix_base[IntegerMod_abstract]


class Matrix_cyclo_dense(Matrix_dense[NumberFieldElement]):
    def __init__(
        self,
        parent: MatrixSpace[NumberFieldElement],
        entries: CyclotomicMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _pickle(
        self,
    ) -> tuple[CyclotomicPickleData, Literal[0]]: ...
    def _unpickle(
        self,
        data: CyclotomicPickleData,
        version: int,
    ) -> None: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _lmul_(self, right: NumberFieldElement) -> Self: ..
    def _richcmp_(self, right: Self, op: int) -> bool: ...
    def __copy__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def set_immutable(self) -> None: ....

    def _rational_matrix(self) -> Matrix_rational_dense: ...
    def denominator(self) -> Integer: ...
    def coefficient_bound(self) -> Rational | int: ...
    def height(self) -> RealNumber | int: ...
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

    def _charpoly_bound(self) -> Integer | Rational: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: CyclotomicCharpolyAlgorithm = ...,
        proof: bool | None = ...,
    ) -> Polynomial: ...
    def _charpoly_mod(
        self,
        p: int | Integer,
    ) -> CyclotomicReductionMatrix: ...
    def _charpoly_multimodular(
        self,
        var: str = ...,
        proof: bool | None = ...,
    ) -> Polynomial: ...
    def _reductions(
        self,
        p: int | Integer,
    ) -> tuple[list[CyclotomicReductionMatrix], Integer]: ...
    def _reduction_matrix(
        self,
        p: int | Integer,
    ) -> tuple[
        CyclotomicReductionMatrix,
        CyclotomicReductionMatrix,
    ]: ...

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
    def _echelon_form_one_prime(
        self,
        p: int | Integer,
    ) -> tuple[
        Self | CyclotomicReductionMatrix,
        tuple[int, ...] | range,
    ]: ...
    def tensor_product(
        self,
        A: Matrix_base[RingElement],
        subdivide: bool = ...,
    ) -> Matrix_base[RingElement]: ...
