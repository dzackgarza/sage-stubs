from typing import Self

from sage.categories.category import Category
from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion, AsymptoticRing
from sage.rings.function_field.place import FunctionFieldPlace
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_ideal import NumberFieldIdeal
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.ring import Ring
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

class FractionWithFactoredDenominator(RingElement):
    def __init__(
        self,
        parent: AsymptoticRing,
        numerator: ElementConstructorInput,
        denominator_factored: ElementConstructorInput,
        reduce: bool = ...,
    ) -> None: ...
    def numerator(self) -> Self: ...
    def denominator(self) -> Self: ...
    def denominator_factored(self) -> Self: ...
    @property
    def denominator_ring(self) -> Self: ...
    @property
    def numerator_ring(self) -> Self: ...
    def dimension(self) -> int | Integer: ...
    def quotient(self) -> Self: ...
    def univariate_decomposition(self) -> Self: ...
    def nullstellensatz_certificate(self) -> Self: ...
    def nullstellensatz_decomposition(self) -> Self: ...
    def algebraic_dependence_certificate(self) -> Self: ...
    def algebraic_dependence_decomposition(
        self, whole_and_parts: ElementConstructorInput = ...
    ) -> Self: ...
    def leinartas_decomposition(self) -> Self: ...
    def cohomology_decomposition(self) -> Self: ...
    def asymptotic_decomposition(
        self,
        alpha: RingElement | int | Integer | Rational,
        asy_var: int | Integer = ...,
    ) -> Self: ...
    def asymptotics(
        self,
        p: int | Integer,
        alpha: RingElement | int | Integer | Rational,
        N: int | Integer,
        asy_var: int | Integer = ...,
        numerical: int | Integer = ...,
        verbose: int | Integer = ...,
    ) -> Self: ...
    def asymptotics_smooth(
        self,
        p: int | Integer,
        alpha: RingElement | int | Integer | Rational,
        N: int | Integer,
        asy_var: int | Integer,
        coordinate: int | Integer = ...,
        numerical: int | Integer = ...,
        verbose: int | Integer = ...,
    ) -> Self: ...
    def asymptotics_multiple(
        self,
        p: int | Integer,
        alpha: RingElement | int | Integer | Rational,
        N: int | Integer,
        asy_var: int | Integer,
        coordinate: int | Integer = ...,
        numerical: int | Integer = ...,
        verbose: int | Integer = ...,
    ) -> Self: ...
    def grads(self, p: int | Integer) -> Self: ...
    def log_grads(self, p: int | Integer) -> Self: ...
    def critical_cone(
        self, p: int | Integer, coordinate: Polynomial | MPolynomial = ...
    ) -> Self: ...
    def is_convenient_multiple_point(self, p: int | Integer) -> bool: ...
    def singular_ideal(self) -> Self: ...
    def smooth_critical_ideal(
        self, alpha: RingElement | int | Integer | Rational
    ) -> Self: ...
    def maclaurin_coefficients(
        self, multi_indices: int | Integer, numerical: int | Integer = ...
    ) -> Self: ...
    def relative_error(
        self,
        approx: int | Integer,
        alpha: RingElement | int | Integer | Rational,
        interval: int | Integer,
        exp_scale: int | Integer = ...,
        digits: ElementConstructorInput = ...,
    ) -> Self: ...
    def _repr_(self) -> str: ...

class FractionWithFactoredDenominatorRing(UniqueRepresentation, Parent):
    @staticmethod
    def __classcall_private__(
        cls: type[FractionWithFactoredDenominatorRing],
        denominator_ring: ElementConstructorInput,
        numerator_ring: ElementConstructorInput = ...,
        category: Category = ...,
    ) -> FractionWithFactoredDenominatorRing: ...
    def __init__(
        self,
        denominator_ring: ElementConstructorInput,
        numerator_ring: ElementConstructorInput = ...,
        category: Category = ...,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self, *args: ElementConstructorInput, **kwargs: ElementConstructorInput
    ) -> Self: ...
    def _coerce_map_from_(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
    ) -> bool: ...
    def _an_element_(self) -> Self: ...

class FractionWithFactoredDenominatorSum(list):
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def denominator_ring(self) -> Self: ...
    def whole_and_parts(self) -> Self: ...
    def sum(self) -> Self: ...

def diff_prod(
    f_derivs: int | Integer,
    u: int | Integer,
    g: int | Integer,
    X: AsymptoticExpansion | ElementConstructorInput,
    interval: int | Integer,
    end: int | Integer,
    uderivs: int | Integer,
    atc: int | Integer,
) -> AsymptoticExpansion: ...
def subs_all(f: Ring, sub: Ring, simplify: Ring = ...) -> AsymptoticExpansion: ...
def diff_all(
    f: Ring,
    V: ElementConstructorInput,
    n: int | Integer,
    ending: Ring = ...,
    sub: Ring = ...,
    sub_final: Ring = ...,
    zero_order: Ring = ...,
    rekey: Ring = ...,
) -> AsymptoticExpansion: ...
def diff_op(
    A: AsymptoticExpansion | ElementConstructorInput,
    B: AsymptoticExpansion | ElementConstructorInput,
    AB_derivs: ElementConstructorInput,
    V: ElementConstructorInput,
    M: int | Integer,
    r: int | Integer,
    N: int | Integer,
) -> AsymptoticExpansion: ...
def diff_seq(
    V: ElementConstructorInput, s: AsymptoticExpansion | ElementConstructorInput
) -> AsymptoticExpansion: ...
def diff_op_simple(
    A: AsymptoticExpansion | ElementConstructorInput,
    B: AsymptoticExpansion | ElementConstructorInput,
    AB_derivs: ElementConstructorInput,
    x: AsymptoticExpansion | ElementConstructorInput,
    v: Ring,
    a: AsymptoticExpansion | ElementConstructorInput,
    N: int | Integer,
) -> AsymptoticExpansion: ...
def direction(v: Ring, coordinate: Ring = ...) -> AsymptoticExpansion: ...
def coerce_point(R: Ring, p: int | Integer) -> AsymptoticExpansion: ...
