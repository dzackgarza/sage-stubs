from collections.abc import Iterable, Iterator, Sequence
from typing import Literal, TypeVar, overload

from sage.crypto.boolean_function import BooleanFunction
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import Element, RingElement
from sage.structure.sage_object import SageObject

_FiniteElement = TypeVar(
    "_FiniteElement",
    bound=FiniteRingElement,
)

type Bit = bool | int | Integer | IntegerMod_abstract
type BitSequence = Sequence[Bit]
type SBoxEntry = int | Integer | FiniteRingElement
type SBoxTable = Iterable[SBoxEntry]
type SBoxDirection = (
    int
    | Integer
    | BitSequence
    | FreeModuleElement[IntegerMod_abstract]
)
type LATScale = Literal[
    "absolute_bias",
    "bias",
    "correlation",
    "fourier_coefficient",
]
type CNFFormat = Literal[
    "symbolic",
    "dimacs",
    "dimacs_headless",
]


class SBox(SageObject):
    @overload
    def __init__(
        self,
        S: SBoxTable | Polynomial,
        *,
        big_endian: bool = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *S: SBoxEntry,
        big_endian: bool = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __len__(self) -> int: ...
    def __eq__(self, rhs: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def to_bits(
        self,
        x: int | Integer,
        n: int | Integer | None = ...,
    ) -> list[IntegerMod_abstract]: ...
    def from_bits(
        self,
        x: BitSequence,
        n: int | Integer | None = ...,
    ) -> Integer: ...

    @overload
    def __call__(self, X: int | Integer) -> int | Integer: ...
    @overload
    def __call__(self, X: Rational) -> Rational: ...
    @overload
    def __call__(self, X: _FiniteElement) -> _FiniteElement: ...
    @overload
    def __call__(
        self,
        X: FreeModuleElement[IntegerMod_abstract],
    ) -> FreeModuleElement[IntegerMod_abstract]: ...
    @overload
    def __call__(self, X: BitSequence) -> list[IntegerMod_abstract]: ...
    @overload
    def __call__(
        self,
        X: Element | BitSequence,
    ) -> Element | list[IntegerMod_abstract] | int | Integer: ...

    def __getitem__(self, X: int | Integer) -> int | Integer: ...
    def input_size(self) -> int: ...
    def output_size(self) -> int: ...
    def is_permutation(self) -> bool: ...
    def __iter__(self) -> Iterator[int | Integer]: ...
    def derivative(self, u: SBoxDirection) -> SBox: ...
    def difference_distribution_table(self) -> Matrix_integer_dense: ...
    def maximal_difference_probability_absolute(self) -> int | Integer: ...
    differential_uniformity = maximal_difference_probability_absolute
    def maximal_difference_probability(self) -> float: ...

    @overload
    def linear_approximation_table(
        self,
        scale: Literal["fourier_coefficient"],
    ) -> Matrix_integer_dense: ...
    @overload
    def linear_approximation_table(
        self,
        scale: Literal[
            "absolute_bias",
            "bias",
            "correlation",
            None,
        ] = ...,
    ) -> Matrix_rational_dense: ...
    @overload
    def linear_approximation_table(
        self,
        scale: LATScale | None = ...,
    ) -> Matrix_integer_dense | Matrix_rational_dense: ...

    def maximal_linear_bias_absolute(self) -> int | Integer | Rational: ...
    def maximal_linear_bias_relative(self) -> float: ...
    def ring(self) -> MPolynomialRing_base: ...
    def solutions(
        self,
        X: Sequence[MPolynomial] | None = ...,
        Y: Sequence[MPolynomial] | None = ...,
    ) -> list[dict[MPolynomial, IntegerMod_abstract]]: ...
    def polynomials(
        self,
        X: Sequence[MPolynomial] | None = ...,
        Y: Sequence[MPolynomial] | None = ...,
        degree: int | Integer = ...,
        groebner: bool = ...,
    ) -> list[MPolynomial]: ...
    def interpolation_polynomial(
        self,
        k: FiniteField | None = ...,
    ) -> Polynomial: ...

    @overload
    def cnf(
        self,
        xi: Sequence[int | Integer] | None = ...,
        yi: Sequence[int | Integer] | None = ...,
        format: None = ...,
    ) -> list[tuple[int, ...]]: ...
    @overload
    def cnf(
        self,
        xi: Sequence[int | Integer] | None,
        yi: Sequence[int | Integer] | None,
        format: CNFFormat,
    ) -> str: ...
    @overload
    def cnf(
        self,
        xi: Sequence[int | Integer] | None = ...,
        yi: Sequence[int | Integer] | None = ...,
        format: CNFFormat | None = ...,
    ) -> list[tuple[int, ...]] | str: ...

    def component_function(self, b: SBoxDirection) -> BooleanFunction: ...
    def nonlinearity(self) -> int | Integer: ...
    def linearity(self) -> int | Integer: ...
    def is_apn(self) -> bool: ...
    def differential_branch_number(self) -> int: ...
    def linear_branch_number(self) -> int: ...
    def autocorrelation_table(self) -> Matrix_integer_dense: ...
    def boomerang_connectivity_table(self) -> Matrix_integer_dense: ...
    def boomerang_uniformity(self) -> int | Integer: ...
    def linear_structures(self) -> list[tuple[int, int, int]]: ...
    def has_linear_structure(self) -> bool: ...
    def is_linear_structure(
        self,
        a: SBoxDirection,
        b: SBoxDirection,
    ) -> bool: ...
    def max_degree(self) -> int | Integer: ...
    def min_degree(self) -> int | Integer: ...
    def is_balanced(self) -> bool: ...
    def is_almost_bent(self) -> bool: ...
    def fixed_points(self) -> list[int]: ...
    def inverse(self) -> SBox: ...
    def is_monomial_function(self) -> bool: ...
    def is_plateaued(self) -> bool: ...
    def is_bent(self) -> bool: ...
    def is_involution(self) -> bool: ...


def feistel_construction(
    *args: SBox | Iterable[SBox],
) -> SBox: ...


def misty_construction(
    *args: SBox | Iterable[SBox],
) -> SBox: ...
