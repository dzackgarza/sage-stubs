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
from sage.rings.valuation.valuation import DiscretePseudoValuation, DiscreteValuation
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput

class MappedValuation_base(DiscretePseudoValuation):
    def __init__(
        self, parent: DiscretePseudoValuation, base_valuation: Ring
    ) -> None: ...
    def residue_ring(self) -> Ring: ...
    def uniformizer(self) -> RingElement: ...
    def reduce(self, f: Polynomial | MPolynomial) -> RingElement: ...
    def lift(self, F: Polynomial | MPolynomial) -> RingElement: ...
    def simplify(
        self,
        x: RingElement | ElementConstructorInput,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
    ) -> Self: ...
    def element_with_valuation(
        self, s: RingElement | ElementConstructorInput
    ) -> RingElement: ...
    def _repr_(self) -> str: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> RingElement: ...

class FiniteExtensionFromInfiniteValuation(MappedValuation_base, DiscreteValuation):
    def __init__(
        self, parent: DiscretePseudoValuation, base_valuation: ElementConstructorInput
    ) -> None: ...
    def restriction(self, ring: Ring) -> Self: ...
    def simplify(
        self,
        x: RingElement | ElementConstructorInput,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
    ) -> Self: ...
    def lower_bound(
        self, x: RingElement | ElementConstructorInput
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...
    def upper_bound(
        self, x: RingElement | ElementConstructorInput
    ) -> Integer | Rational | PlusInfinity | MinusInfinity: ...

class FiniteExtensionFromLimitValuation(FiniteExtensionFromInfiniteValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        approximant: ElementConstructorInput,
        G: Polynomial | MPolynomial,
        approximants: ElementConstructorInput,
    ) -> None: ...
    def _repr_(self) -> str: ...
