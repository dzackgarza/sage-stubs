from collections.abc import Mapping, Sequence
from typing import Self, TypeVar

from sage.categories.category import Category
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

type DenominatorFactor = tuple[RingElement, Integer]
type MultiIndex = tuple[int | Integer, ...]
type DifferentialTable = dict[MultiIndex, RingElement]
type AsymptoticTriple = tuple[RingElement, RingElement, RingElement]
type CriticalCone = tuple[list[FreeModuleElement[RingElement]], Polyhedron_base]
_T = TypeVar("_T")

class FractionWithFactoredDenominator(RingElement):
    def __init__(
        self,
        parent: FractionWithFactoredDenominatorRing,
        numerator: ElementConstructorInput,
        denominator_factored: Sequence[tuple[ElementConstructorInput, int | Integer]],
        reduce: bool = ...,
    ) -> None: ...
    def parent(self) -> FractionWithFactoredDenominatorRing: ...
    def numerator(self) -> RingElement: ...
    def denominator(self) -> RingElement: ...
    def denominator_factored(self) -> list[DenominatorFactor]: ...
    @property
    def denominator_ring(self) -> Parent[RingElement]: ...
    @property
    def numerator_ring(self) -> Parent[RingElement]: ...
    def dimension(self) -> int | Integer: ...
    def quotient(self) -> RingElement: ...
    def univariate_decomposition(self) -> FractionWithFactoredDenominatorSum: ...
    def nullstellensatz_certificate(self) -> RingElement | None: ...
    def nullstellensatz_decomposition(self) -> FractionWithFactoredDenominatorSum: ...
    def algebraic_dependence_certificate(self) -> Ideal_generic: ...
    def algebraic_dependence_decomposition(
        self,
        whole_and_parts: bool = ...,
    ) -> FractionWithFactoredDenominatorSum: ...
    def leinartas_decomposition(self) -> FractionWithFactoredDenominatorSum: ...
    def cohomology_decomposition(self) -> FractionWithFactoredDenominatorSum: ...
    def asymptotic_decomposition(
        self,
        alpha: Sequence[RingElement],
        asy_var: str | None = ...,
    ) -> FractionWithFactoredDenominatorSum: ...
    def asymptotics(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
        alpha: Sequence[RingElement],
        N: int | Integer,
        asy_var: str | None = ...,
        numerical: int | Integer = ...,
        verbose: bool = ...,
    ) -> AsymptoticTriple: ...
    def asymptotics_smooth(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
        alpha: Sequence[RingElement],
        N: int | Integer,
        asy_var: str,
        coordinate: int | Integer | None = ...,
        numerical: int | Integer = ...,
        verbose: bool = ...,
    ) -> AsymptoticTriple: ...
    def asymptotics_multiple(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
        alpha: Sequence[RingElement],
        N: int | Integer,
        asy_var: str,
        coordinate: int | Integer | None = ...,
        numerical: int | Integer = ...,
        verbose: bool = ...,
    ) -> AsymptoticTriple: ...
    def grads(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
    ) -> list[tuple[RingElement, ...]]: ...
    def log_grads(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
    ) -> list[tuple[RingElement, ...]]: ...
    def critical_cone(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
        coordinate: int | Integer | None = ...,
    ) -> CriticalCone: ...
    def is_convenient_multiple_point(
        self,
        p: Mapping[RingElement, RingElement] | Sequence[RingElement],
    ) -> tuple[bool, str]: ...
    def singular_ideal(self) -> Ideal_generic: ...
    def smooth_critical_ideal(self, alpha: Sequence[RingElement]) -> Ideal_generic: ...
    def maclaurin_coefficients(
        self,
        multi_indices: Sequence[MultiIndex],
        numerical: int | Integer = ...,
    ) -> dict[MultiIndex, RingElement]: ...
    def relative_error(
        self,
        approx: AsymptoticExpansion | RingElement,
        alpha: Sequence[RingElement],
        interval: Sequence[int | Integer],
        exp_scale: RingElement | int | Integer = ...,
        digits: int | Integer = ...,
    ) -> list[tuple[int | Integer, RingElement, RingElement]]: ...
    def _repr_(self) -> str: ...

class FractionWithFactoredDenominatorRing(
    UniqueRepresentation,
    Parent[FractionWithFactoredDenominator],
):
    Element: type[FractionWithFactoredDenominator]
    @staticmethod
    def __classcall_private__(
        class_: type[FractionWithFactoredDenominatorRing],
        denominator_ring: Parent[RingElement],
        numerator_ring: Parent[RingElement] | None = ...,
        category: Category | None = ...,
    ) -> FractionWithFactoredDenominatorRing: ...
    def __init__(
        self,
        denominator_ring: Parent[RingElement],
        numerator_ring: Parent[RingElement] | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[RingElement]: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        numerator: ElementConstructorInput,
        denominator_factored: Sequence[tuple[ElementConstructorInput, int | Integer]] = ...,
        reduce: bool = ...,
    ) -> FractionWithFactoredDenominator: ...
    def _coerce_map_from_(self, P: Parent) -> bool | None: ...
    def _an_element_(self) -> FractionWithFactoredDenominator: ...

class FractionWithFactoredDenominatorSum(list[FractionWithFactoredDenominator]):
    def __repr__(self) -> str: ...
    def __eq__(self, other: object) -> bool: ....
    def __ne__(self, other: object) -> bool: ...
    @property
    def denominator_ring(self) -> Parent[RingElement] | None: ...
    def whole_and_parts(self) -> FractionWithFactoredDenominatorSum: ...
    def sum(
        self,
    ) -> FractionWithFactoredDenominator | FractionWithFactoredDenominatorSum: ...

def diff_prod(
    f_derivs: DifferentialTable,
    u: RingElement,
    g: RingElement,
    X: Sequence[RingElement],
    interval: int | Integer,
    end: int | Integer,
    uderivs: DifferentialTable,
    atc: Mapping[RingElement, RingElement] | None,
) -> DifferentialTable: ...
def subs_all(
    f: _T,
    sub: Mapping[RingElement, RingElement],
    simplify: bool = ...,
) -> _T: ...
def diff_all(
    f: RingElement,
    V: Sequence[RingElement],
    n: int | Integer,
    ending: Sequence[MultiIndex] = ...,
    sub: Mapping[RingElement, RingElement] | None = ...,
    sub_final: Mapping[RingElement, RingElement] | None = ...,
    zero_order: int | Integer = ...,
    rekey: Mapping[MultiIndex, MultiIndex] | None = ...,
) -> DifferentialTable: ...
def diff_op(
    A: RingElement,
    B: RingElement,
    AB_derivs: DifferentialTable,
    V: Sequence[RingElement],
    M: int | Integer,
    r: int | Integer,
    N: int | Integer,
) -> DifferentialTable: ...
def diff_seq(V: Sequence[_T], s: Sequence[MultiIndex]) -> tuple[_T, ...]: ...
def diff_op_simple(
    A: RingElement,
    B: RingElement,
    AB_derivs: DifferentialTable,
    x: RingElement,
    v: RingElement,
    a: RingElement,
    N: int | Integer,
) -> DifferentialTable: ...
def direction(
    v: Sequence[RingElement],
    coordinate: int | Integer | None = ...,
) -> tuple[RingElement, ...]: ...
def coerce_point(
    R: Parent[RingElement],
    p: Mapping[RingElement, RingElement] | Sequence[RingElement],
) -> Mapping[RingElement, RingElement] | Sequence[RingElement]: ...
