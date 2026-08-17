from collections.abc import Callable
from typing import Self

from sage.categories.map import Map
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.rings.ring import Ring
from sage.rings.valuation.valuation import (
    DiscretePseudoValuation,
    InfiniteDiscretePseudoValuation,
)
from sage.rings.valuation.value_group import DiscreteValueSemigroup
from sage.structure.element import Element, RingElement
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput

class LimitValuationFactory(UniqueFactory):
    def create_key(
        self, base_valuation: ElementConstructorInput, G: Polynomial | MPolynomial
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self, version: int | tuple[int, ...], key: tuple[ElementConstructorInput, ...]
    ) -> LimitValuationFactory: ...

LimitValuation: UniqueFactory

class LimitValuation_generic(DiscretePseudoValuation):
    def __init__(
        self, parent: DiscretePseudoValuation, approximation: ElementConstructorInput
    ) -> None: ...
    def reduce(self, f: Polynomial | MPolynomial, check: bool = ...) -> RingElement: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> RingElement: ...
    def _repr_(self) -> str: ...

class MacLaneLimitValuation(LimitValuation_generic, InfiniteDiscretePseudoValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        approximation: ElementConstructorInput,
        G: Polynomial | MPolynomial,
    ) -> None: ...
    def extensions(self, ring: Ring) -> list[DiscretePseudoValuation]: ...
    def lift(self, F: Polynomial | MPolynomial) -> RingElement: ...
    def uniformizer(self) -> RingElement: ...
    def residue_ring(self) -> Ring: ...
    def restriction(self, ring: Ring) -> Self: ...
    def value_semigroup(self) -> DiscreteValueSemigroup: ...
    def element_with_valuation(
        self, s: RingElement | ElementConstructorInput
    ) -> RingElement: ...
    def simplify(
        self,
        f: Polynomial | MPolynomial,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
    ) -> Self: ...
    def lower_bound(
        self, f: Polynomial | MPolynomial
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def upper_bound(
        self, f: Polynomial | MPolynomial
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def is_negative_pseudo_valuation(self) -> bool: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> RingElement | PlusInfinity: ...
