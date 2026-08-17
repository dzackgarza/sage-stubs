from collections.abc import Sequence
from typing import Self

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.function_field.function_field import FunctionField
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.rings.ring import Ring
from sage.rings.valuation.inductive_valuation import (
    FinalInductiveValuation,
    FiniteInductiveValuation,
    InductiveValuation,
    InfiniteInductiveValuation,
    NonFinalInductiveValuation,
)
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.rings.valuation.value_group import DiscreteValueGroup, DiscreteValueSemigroup
from sage.structure.element import RingElement
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput

class AugmentedValuationFactory(UniqueFactory):
    def create_key(
        self,
        base_valuation: ElementConstructorInput,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
        check: bool = ...,
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self, version: int | tuple[int, ...], key: tuple[ElementConstructorInput, ...]
    ) -> AugmentedValuationFactory: ...

AugmentedValuation: UniqueFactory

class AugmentedValuation_base(InductiveValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...
    def equivalence_unit(
        self, s: RingElement | ElementConstructorInput, reciprocal: bool = ...
    ) -> RingElement: ...
    def element_with_valuation(
        self, s: RingElement | ElementConstructorInput
    ) -> RingElement: ...
    def augmentation_chain(self) -> list[DiscretePseudoValuation]: ...
    def psi(self) -> RingElement: ...
    def E(self) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def F(self) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def extensions(self, ring: Ring) -> list[DiscretePseudoValuation]: ...
    def restriction(self, ring: Ring) -> Self: ...
    def uniformizer(self) -> RingElement: ...
    def is_gauss_valuation(self) -> bool: ...
    def monic_integral_model(self, G: Polynomial | MPolynomial) -> Self: ...
    def is_trivial(self) -> bool: ...
    def scale(self, scalar: RingElement | int | Integer | Rational) -> Self: ...
    def is_negative_pseudo_valuation(self) -> bool: ...
    def change_domain(self, ring: Ring) -> Self: ...
    def _repr_(self) -> str: ...

class FinalAugmentedValuation(AugmentedValuation_base, FinalInductiveValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...
    def residue_ring(self) -> Ring: ...
    def reduce(
        self,
        f: Polynomial | MPolynomial,
        check: bool = ...,
        degree_bound: Ring = ...,
        coefficients: Sequence[RingElement] = ...,
        valuations: Ring = ...,
    ) -> RingElement: ...
    def lift(self, F: Polynomial | MPolynomial) -> RingElement: ...

class NonFinalAugmentedValuation(AugmentedValuation_base, NonFinalInductiveValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...
    def residue_ring(self) -> Ring: ...
    def reduce(
        self,
        f: Polynomial | MPolynomial,
        check: bool = ...,
        degree_bound: Ring = ...,
        coefficients: Sequence[RingElement] = ...,
        valuations: Ring = ...,
    ) -> RingElement: ...
    def lift(
        self,
        F: Polynomial | MPolynomial,
        report_coefficients: Polynomial | MPolynomial = ...,
    ) -> RingElement: ...
    def lift_to_key(
        self, F: Polynomial | MPolynomial, check: bool = ...
    ) -> RingElement: ...

class FiniteAugmentedValuation(AugmentedValuation_base, FiniteInductiveValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...
    def value_group(self) -> DiscreteValueGroup: ...
    def value_semigroup(self) -> DiscreteValueSemigroup: ...
    def valuations(
        self,
        f: Polynomial | MPolynomial,
        coefficients: Sequence[RingElement] = ...,
        call_error: Polynomial | MPolynomial = ...,
    ) -> list[Integer | Rational | PlusInfinity | MinusInfinity]: ...
    def simplify(
        self,
        f: Polynomial | MPolynomial,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
        effective_degree: FunctionField = ...,
        size_heuristic_bound: FunctionField = ...,
        phiadic: bool = ...,
    ) -> Self: ...
    def lower_bound(
        self, f: Polynomial | MPolynomial
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def upper_bound(
        self, f: Polynomial | MPolynomial
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...

class FinalFiniteAugmentedValuation(FiniteAugmentedValuation, FinalAugmentedValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...

class NonFinalFiniteAugmentedValuation(
    FiniteAugmentedValuation, NonFinalAugmentedValuation
):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...

class InfiniteAugmentedValuation(FinalAugmentedValuation, InfiniteInductiveValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        v: DiscretePseudoValuation,
        phi: Map | Morphism,
        mu: DiscretePseudoValuation,
    ) -> None: ...
    def value_group(self) -> DiscreteValueGroup: ...
    def value_semigroup(self) -> DiscreteValueSemigroup: ...
    def valuations(
        self,
        f: Polynomial | MPolynomial,
        coefficients: Sequence[RingElement] = ...,
        call_error: Polynomial | MPolynomial = ...,
    ) -> list[Integer | Rational | PlusInfinity | MinusInfinity]: ...
    def simplify(
        self,
        f: Polynomial | MPolynomial,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
        effective_degree: ElementConstructorInput = ...,
    ) -> Self: ...
    def lower_bound(
        self, f: Polynomial | MPolynomial
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def upper_bound(
        self, f: Polynomial | MPolynomial
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
