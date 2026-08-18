from collections.abc import Mapping

from sage.geometry.polyhedral_complex import PolyhedralComplex
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.plot.plot3d.base import Graphics3d
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.multi_polynomial_element import MPolynomial_polydict
from sage.rings.polynomial.term_order import TermOrder
from sage.rings.semirings.tropical_semiring import TropicalSemiring
from sage.rings.semirings.tropical_variety import (
    TropicalCurve,
    TropicalSurface,
    TropicalVariety,
)
from sage.structure.element import ModuleElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

type _TropicalExponent = tuple[int, ...]
type _TropicalMPolynomialInput = (
    TropicalMPolynomial
    | MPolynomial
    | Mapping[_TropicalExponent, ElementConstructorInput]
    | ElementConstructorInput
)

class TropicalMPolynomial(MPolynomial_polydict):
    def parent(self) -> TropicalMPolynomialSemiring: ...
    def subs(
        self,
        fixed: Mapping[TropicalMPolynomial | int, ElementConstructorInput] | None = ...,
        **kwds: ElementConstructorInput,
    ) -> TropicalMPolynomial: ...
    def plot3d(self, color: str = ...) -> Graphics3d: ...
    def tropical_variety(self) -> TropicalCurve | TropicalSurface | TropicalVariety: ...
    def newton_polytope(self) -> Polyhedron_base: ...
    def dual_subdivision(self) -> PolyhedralComplex: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

class TropicalMPolynomialSemiring(
    UniqueRepresentation,
    Parent[TropicalMPolynomial],
):
    Element: type[TropicalMPolynomial]
    def __init__(
        self,
        base_semiring: TropicalSemiring[ModuleElement],
        n: int | Integer,
        names: str | tuple[str, ...],
        order: TermOrder,
    ) -> None: ...
    def base(self) -> TropicalSemiring[ModuleElement]: ...
    def base_ring(self) -> TropicalSemiring[ModuleElement]: ...
    def term_order(self) -> TermOrder: ...
    def one(self) -> TropicalMPolynomial: ...
    def zero(self) -> TropicalMPolynomial: ...
    def random_element(
        self,
        degree: int | Integer = ...,
        terms: int | Integer | None = ...,
        choose_degree: bool = ...,
        *args: ElementConstructorInput,
        **kwargs: ElementConstructorInput,
    ) -> TropicalMPolynomial: ...
    def gen(self, n: int | Integer = ...) -> TropicalMPolynomial: ...
    def gens(self) -> tuple[TropicalMPolynomial, ...]: ...
    def ngens(self) -> Integer: ...
    def _element_constructor_(self, x: _TropicalMPolynomialInput) -> TropicalMPolynomial: ...
    def _repr_(self) -> str: ...
