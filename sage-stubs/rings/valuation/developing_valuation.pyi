from collections.abc import Callable

from sage.calculus.predefined import v
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput

class DevelopingValuation(DiscretePseudoValuation):
    def __init__(
        self, parent: DiscretePseudoValuation, phi: Map | Morphism
    ) -> None: ...
    def phi(self) -> RingElement: ...
    def effective_degree(
        self, f: Polynomial | MPolynomial, valuations: ElementConstructorInput = ...
    ) -> int | Integer: ...
    def coefficients(self, f: Polynomial | MPolynomial) -> list[RingElement]: ...
    def newton_polygon(
        self, f: Polynomial | MPolynomial, valuations: ElementConstructorInput = ...
    ) -> RingElement: ...
    def valuations(
        self, f: Polynomial | MPolynomial
    ) -> list[Integer | Rational | PlusInfinity | MinusInfinity]: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> v | PlusInfinity: ...
