from collections.abc import Sequence

from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.valuation.value_group import ValuationValue
from sage.structure.element import RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import ElementConstructorInput

type ValuationPrecision = int | Integer | Rational | PlusInfinity | MinusInfinity | None

class DiscretePseudoValuation(Morphism[RingElement, ValuationValue]):
    def __init__(
        self,
        parent: Homset[Map[RingElement, ValuationValue], RingElement, ValuationValue],
    ) -> None: ...
    def is_equivalent(
        self,
        f: ElementConstructorInput,
        g: ElementConstructorInput,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    def _hash_(self) -> int: ...
    def _richcmp_(self, other: DiscretePseudoValuation, op: int) -> bool: ...
    def _eq_(self, other: DiscretePseudoValuation) -> bool: ...
    def _le_(self, other: DiscretePseudoValuation) -> bool: ...
    def _ge_(self, other: DiscretePseudoValuation) -> bool: ...
    def _test_valuation_inheritance(
        self,
        **options: bool | int | str | None,
    ) -> None: ...

class InfiniteDiscretePseudoValuation(DiscretePseudoValuation):
    def is_discrete_valuation(self) -> bool: ...

class NegativeInfiniteDiscretePseudoValuation(InfiniteDiscretePseudoValuation):
    def is_negative_pseudo_valuation(self) -> bool: ...

class DiscreteValuation(DiscretePseudoValuation):
    def is_discrete_valuation(self) -> bool: ...
    def mac_lane_approximants(
        self,
        G: Polynomial,
        assume_squarefree: bool = ...,
        require_final_EF: bool = ...,
        required_precision: ValuationPrecision = ...,
        require_incomparability: bool = ...,
        require_maximal_degree: bool = ...,
        algorithm: str = ...,
    ) -> list[DiscretePseudoValuation]: ...
    def mac_lane_approximant(
        self,
        G: Polynomial,
        valuation: DiscretePseudoValuation,
        approximants: Sequence[DiscretePseudoValuation] | None = ...,
    ) -> DiscretePseudoValuation: ...
    def montes_factorization(
        self,
        G: Polynomial,
        assume_squarefree: bool = ...,
        required_precision: ValuationPrecision = ...,
    ) -> Factorization: ...
    def _ge_(self, other: DiscretePseudoValuation) -> bool: ...

class MacLaneApproximantNode:
    valuation: DiscretePseudoValuation
    parent: MacLaneApproximantNode | None
    ef: bool
    principal_part_bound: ValuationValue | None
    coefficients: list[RingElement] | None
    valuations: list[ValuationValue] | None
    forced_leaf: bool
    __hash__: None
    def __init__(
        self,
        valuation: DiscretePseudoValuation,
        parent: MacLaneApproximantNode | None,
        ef: bool,
        principal_part_bound: ValuationValue | None,
        coefficients: list[RingElement] | None,
        valuations: list[ValuationValue] | None,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
