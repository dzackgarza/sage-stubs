from collections.abc import Callable
from typing import Self

from sage.categories.map import Map
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.rings.valuation.valuation import DiscretePseudoValuation, DiscreteValuation
from sage.rings.valuation.value_group import DiscreteValueSemigroup
from sage.structure.element import Element, RingElement
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput

class ScaledValuationFactory(UniqueFactory):
    def create_key(
        self, base: ElementConstructorInput, s: RingElement | ElementConstructorInput
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self, version: int | tuple[int, ...], key: tuple[ElementConstructorInput, ...]
    ) -> ScaledValuationFactory: ...

ScaledValuation: UniqueFactory

class ScaledValuation_generic(DiscreteValuation):
    def __init__(
        self,
        parent: DiscretePseudoValuation,
        base_valuation: Ring,
        s: RingElement | ElementConstructorInput,
    ) -> None: ...
    def residue_ring(self) -> Ring: ...
    def uniformizer(self) -> RingElement: ...
    def reduce(self, f: Polynomial | MPolynomial) -> RingElement: ...
    def lift(self, F: Polynomial | MPolynomial) -> RingElement: ...
    def extensions(self, ring: Ring) -> list[DiscretePseudoValuation]: ...
    def restriction(self, ring: Ring) -> Self: ...
    def value_semigroup(self) -> DiscreteValueSemigroup: ...
    def _repr_(self) -> str: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> RingElement: ...
