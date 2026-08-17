from typing import Self

from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_ideal import NumberFieldIdeal
from sage.rings.padics.padic_generic import pAdicGeneric
from sage.rings.padics.padic_generic_element import pAdicGenericElement
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.rings.ring import Ring
from sage.rings.valuation.mapped_valuation import FiniteExtensionFromLimitValuation
from sage.rings.valuation.valuation import DiscretePseudoValuation, DiscreteValuation
from sage.rings.valuation.value_group import DiscreteValueSemigroup
from sage.schemes.elliptic_curves.sha_tate import valuation
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput

class PadicValuationFactory(UniqueFactory):
    def create_key_and_extra_args(
        self,
        R: Ring,
        prime: int | Integer = ...,
        approximants: ElementConstructorInput = ...,
    ) -> pAdicGeneric: ...
    def create_key_for_integers(
        self, R: Ring, prime: int | Integer
    ) -> pAdicGeneric: ...
    def create_key_for_local_ring(
        self, R: Ring, prime: int | Integer
    ) -> pAdicGeneric: ...
    def create_key_and_extra_args_for_number_field(
        self, R: Ring, prime: int | Integer, approximants: ElementConstructorInput
    ) -> pAdicGeneric: ...
    def create_key_and_extra_args_for_number_field_from_valuation(
        self,
        R: Ring,
        v: DiscretePseudoValuation,
        prime: int | Integer,
        approximants: ElementConstructorInput,
    ) -> pAdicGeneric: ...
    def create_key_and_extra_args_for_number_field_from_ideal(
        self, R: Ring, I: int | Integer, prime: int | Integer
    ) -> pAdicGeneric: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        key: tuple[ElementConstructorInput, ...],
        **extra_args: ElementConstructorInput,
    ) -> PadicValuationFactory: ...

pAdicValuation: pAdicGenericElement

class pAdicValuation_base(DiscreteValuation):
    def __init__(self, parent: pAdicGeneric, p: int | Integer) -> None: ...
    def p(self) -> pAdicGenericElement: ...
    def reduce(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...
    def lift(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...
    def is_unramified(
        self,
        G: Polynomial | MPolynomial,
        include_steps: Polynomial | MPolynomial = ...,
        assume_squarefree: bool = ...,
    ) -> bool: ...
    def is_totally_ramified(
        self,
        G: Polynomial | MPolynomial,
        include_steps: Polynomial | MPolynomial = ...,
        assume_squarefree: bool = ...,
    ) -> bool: ...
    def change_domain(self, ring: Ring) -> Self: ...
    def extensions(self, ring: Ring) -> list[NumberFieldIdeal]: ...
    def restriction(self, ring: Ring) -> Self: ...
    def value_semigroup(self) -> DiscreteValueSemigroup: ...

class pAdicValuation_padic(pAdicValuation_base):
    def __init__(self, parent: pAdicGeneric) -> None: ...
    def reduce(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...
    def lift(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...
    def uniformizer(self) -> pAdicGenericElement: ...
    def element_with_valuation(
        self, v: DiscretePseudoValuation
    ) -> pAdicGenericElement: ...
    def residue_ring(self) -> Ring: ...
    def shift(
        self,
        x: pAdicGenericElement | ElementConstructorInput,
        s: pAdicGenericElement | ElementConstructorInput,
    ) -> Self: ...
    def simplify(
        self,
        x: pAdicGenericElement | ElementConstructorInput,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
    ) -> Self: ...
    def _repr_(self) -> str: ...
    def _call_(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> pAdicGenericElement: ...

class pAdicValuation_int(pAdicValuation_base):
    def uniformizer(self) -> pAdicGenericElement: ...
    def residue_ring(self) -> Ring: ...
    def simplify(
        self,
        x: pAdicGenericElement | ElementConstructorInput,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
        size_heuristic_bound: ElementConstructorInput = ...,
    ) -> Self: ...
    def inverse(
        self, x: pAdicGenericElement | ElementConstructorInput, precision: int | Integer
    ) -> pAdicGenericElement: ...
    def _repr_(self) -> str: ...
    def _call_(
        self, x: pAdicGenericElement | ElementConstructorInput
    ) -> valuation | PlusInfinity: ...

class pAdicFromLimitValuation(FiniteExtensionFromLimitValuation, pAdicValuation_base):
    def __init__(
        self,
        parent: pAdicGeneric,
        approximant: ElementConstructorInput,
        G: ElementConstructorInput,
        approximants: ElementConstructorInput,
    ) -> None: ...
    def extensions(self, ring: Ring) -> list[NumberFieldIdeal]: ...
