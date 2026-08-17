from collections.abc import Sequence
from typing import Self

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.ring import Ring
from sage.rings.valuation.developing_valuation import DevelopingValuation
from sage.rings.valuation.valuation import (
    DiscretePseudoValuation,
    DiscreteValuation,
    InfiniteDiscretePseudoValuation,
)
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

class InductiveValuation(DevelopingValuation):
    def is_equivalence_unit(
        self, f: Polynomial | MPolynomial, valuations: ElementConstructorInput = ...
    ) -> bool: ...
    def equivalence_reciprocal(
        self,
        f: Polynomial | MPolynomial,
        coefficients: Sequence[RingElement] = ...,
        valuations: Polynomial | MPolynomial = ...,
        check: bool = ...,
    ) -> RingElement: ...
    def mu(self) -> RingElement: ...
    def equivalence_unit(
        self, s: RingElement | ElementConstructorInput, reciprocal: bool = ...
    ) -> RingElement: ...
    def augmentation_chain(self) -> list[DiscretePseudoValuation]: ...
    def is_gauss_valuation(self) -> bool: ...
    def E(self) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def F(self) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def monic_integral_model(self, G: Polynomial | MPolynomial) -> Self: ...
    def element_with_valuation(
        self, s: RingElement | ElementConstructorInput
    ) -> RingElement: ...

class FiniteInductiveValuation(InductiveValuation, DiscreteValuation):
    def __init__(
        self, parent: DiscretePseudoValuation, phi: Map | Morphism
    ) -> None: ...
    def extensions(
        self, other: RingElement | ElementConstructorInput
    ) -> list[DiscretePseudoValuation]: ...

class NonFinalInductiveValuation(FiniteInductiveValuation, DiscreteValuation):
    def __init__(
        self, parent: DiscretePseudoValuation, phi: Map | Morphism
    ) -> None: ...
    def augmentation(
        self, phi: Map | Morphism, mu: DiscretePseudoValuation, check: bool = ...
    ) -> RingElement: ...
    def mac_lane_step(
        self,
        G: Polynomial | MPolynomial,
        principal_part_bound: int | Integer = ...,
        assume_squarefree: bool = ...,
        assume_equivalence_irreducible: int | Integer = ...,
        report_degree_bounds_and_caches: int | Integer = ...,
        coefficients: Sequence[RingElement] = ...,
        valuations: int | Integer = ...,
        check: bool = ...,
        allow_equivalent_key: int | Integer = ...,
    ) -> RingElement: ...
    def is_key(
        self,
        phi: Map | Morphism,
        explain: Polynomial | MPolynomial = ...,
        assume_equivalence_irreducible: ElementConstructorInput = ...,
    ) -> bool: ...
    def is_minimal(
        self,
        f: Polynomial | MPolynomial,
        assume_equivalence_irreducible: ElementConstructorInput = ...,
    ) -> bool: ...
    def is_equivalence_irreducible(
        self,
        f: Polynomial | MPolynomial,
        coefficients: Sequence[RingElement] = ...,
        valuations: ElementConstructorInput = ...,
    ) -> bool: ...
    def equivalence_decomposition(
        self,
        f: Polynomial | MPolynomial,
        assume_not_equivalence_unit: Polynomial | MPolynomial = ...,
        coefficients: Sequence[RingElement] = ...,
        valuations: Polynomial | MPolynomial = ...,
        compute_unit: Polynomial | MPolynomial = ...,
        degree_bound: Polynomial | MPolynomial = ...,
    ) -> RingElement: ...
    def minimal_representative(self, f: Polynomial | MPolynomial) -> RingElement: ...
    def lift_to_key(self, F: Polynomial | MPolynomial) -> RingElement: ...

class FinalInductiveValuation(InductiveValuation): ...

class InfiniteInductiveValuation(
    FinalInductiveValuation, InfiniteDiscretePseudoValuation
):
    def __init__(
        self, parent: DiscretePseudoValuation, base_valuation: ElementConstructorInput
    ) -> None: ...
    def change_domain(self, ring: Ring) -> Self: ...
