from collections.abc import Iterator, Sequence
from typing import Self, TypeAlias

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.groups.additive_abelian.additive_abelian_wrapper import AdditiveAbelianGroupWrapper
from sage.graphs.digraph import DiGraph
from sage.graphs.graph import Graph
from sage.rings.integer import Integer
from sage.rings.laurent_series_ring_element import LaurentSeries
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.factorization import Factorization
from ..curves.projective_curve import ProjectivePlaneCurve_field
from .ell_generic import EllipticCurve_generic
from .ell_point import EllipticCurvePoint_field
from .hom import EllipticCurveHom
from .period_lattice import PeriodLattice_ell

_AInvariant: TypeAlias = RingElement | int | Integer
_TwistParameter: TypeAlias = _AInvariant | None
_DivisionFieldKeyword: TypeAlias = bool | str | int | Integer
_TorsionKeyword: TypeAlias = bool | str | None


class EllipticCurve_field(EllipticCurve_generic, ProjectivePlaneCurve_field):
    def __init__(self, R: Ring, data: Sequence[_AInvariant], category: Category | None = ...) -> None: ...
    def genus(self) -> Integer: ...
    def quadratic_twist(self, D: _TwistParameter = ...) -> Self: ...
    def two_torsion_rank(self) -> Integer: ...
    def quartic_twist(self, D: _AInvariant) -> Self: ...
    def sextic_twist(self, D: _AInvariant) -> Self: ...
    def is_quadratic_twist(self, other: EllipticCurve_generic) -> RingElement | Integer: ...
    def is_quartic_twist(self, other: EllipticCurve_generic) -> RingElement | Integer: ...
    def is_sextic_twist(self, other: EllipticCurve_generic) -> RingElement | Integer: ...
    def descend_to(self, K: Ring, f: Map | None = ...) -> Self | list[Self]: ...
    def division_field(
        self, n: int | Integer, names: str = ..., map: bool = False, **kwds: _DivisionFieldKeyword
    ) -> Ring | tuple[Ring, Map]:
        ...
    def torsion_subgroup(
        self,
        n: int | Integer,
        *,
        extend: bool = False,
        algorithm: str | None = None,
    ) -> AdditiveAbelianGroupWrapper:
        ...
    def torsion_gens(
        self, n: int | Integer, *args: _TorsionKeyword, **kwds: _TorsionKeyword
    ) -> tuple[EllipticCurvePoint_field, ...]: ...
    def torsion_basis(
        self, n: int | Integer, *args: _TorsionKeyword, **kwds: _TorsionKeyword
    ) -> tuple[EllipticCurvePoint_field, EllipticCurvePoint_field]: ...
    def _Hom_(self, other: EllipticCurve_generic, category: Category | None = ...) -> Homset[Self, EllipticCurve_generic]: ...
    def isogeny(
        self,
        kernel: EllipticCurvePoint_field | list[EllipticCurvePoint_field] | tuple[EllipticCurvePoint_field, ...] | Polynomial | list[RingElement] | tuple[RingElement, ...] | None,
        codomain: Self | None = ...,
        degree: int | Integer | None = ...,
        model: str | None = ...,
        check: bool = True,
        algorithm: str | None = None,
        velu_sqrt_bound: int | None = None,
    ) -> EllipticCurveHom: ...
    def isogeny_codomain(
        self,
        kernel: EllipticCurvePoint_field | list[EllipticCurvePoint_field] | tuple[EllipticCurvePoint_field, ...] | Polynomial | list[RingElement] | tuple[RingElement, ...],
    ) -> Self: ...
    def period_lattice(self) -> PeriodLattice_ell: ...
    def kernel_polynomial_from_point(
        self,
        P: EllipticCurvePoint_field,
        *,
        algorithm: str | None = ...,
    ) -> Polynomial: ...
    def kernel_polynomial_from_divisor(
        self,
        f: Polynomial,
        l: int | Integer,
        *,
        check: bool = True,
    ) -> Polynomial: ...
    def isogenies_prime_degree(
        self,
        l: int | Integer | list[int | Integer] | tuple[int | Integer, ...] | None = ...,
        max_l: int | Integer = 31,
    ) -> list[EllipticCurveHom]: ...
    def isogenies_degree(self, n: int | Integer | Factorization, *, _intermediate: bool = False) -> Iterator[EllipticCurveHom]: ...
    def is_isogenous(self, other: EllipticCurve_generic, field: Ring | None = None) -> bool: ...
    def weierstrass_p(self, prec: int = 20, algorithm: str | None = None) -> LaurentSeries: ...
    def hasse_invariant(self) -> RingElement: ...
    def isogeny_ell_graph(self, l: int | Integer, directed: bool = True, label_by_j: bool = False) -> Graph | DiGraph: ...
    def endomorphism_ring_is_commutative(self) -> bool: ...


def compute_model(E: EllipticCurve_generic, name: str) -> EllipticCurve_generic: ...

def point_of_order(E: EllipticCurve_generic, n: int | Integer) -> EllipticCurvePoint_field: ...
