from collections.abc import Iterator
from typing import Self

from sage.calculus.predefined import g, s
from sage.categories.homset import hom
from sage.categories.morphism import Morphism
from sage.groups.galois_group_perm import GaloisGroup_perm, GaloisSubgroup_perm
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.misc.c3_controlled import identity
from sage.misc.functional import order
from sage.rings.function_field.place import FunctionFieldPlace
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.number_field.number_field_ideal import NumberFieldIdeal
from sage.rings.padics.misc import min
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Field
from sage.rings.valuation.valuation import DiscretePseudoValuation
from sage.sets.set import Set
from sage.structure.parent import ElementConstructorInput

class GaloisGroupElement(PermutationGroupElement):

    def as_hom(self) -> hom: ...
    def __call__(self, x: NumberFieldElement | ElementConstructorInput) -> Self: ...
    def ramification_degree(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
    ) -> min: ...

class GaloisGroup_v2(GaloisGroup_perm):
    def order(self, algorithm: str | None = ..., recompute: bool = ...) -> Integer: ...
    def gens(self) -> tuple[GaloisGroupElement, ...]: ...
    def fixed_field(
        self,
        name: str | None = ...,
        polred: bool | None = ...,
        threshold: int | None = ...,
    ) -> NumberField_generic: ...
    def __init__(
        self,
        number_field: ElementConstructorInput,
        algorithm: str | None = ...,
        names: str | tuple[str, ...] | None = ...,
        gc_numbering: ElementConstructorInput | None = ...,
        _type: ElementConstructorInput | None = ...,
    ) -> None: ...
    def easy_order(self, algorithm: str | None = ...) -> NumberFieldElement | order: ...
    def transitive_number(
        self, algorithm: str | None = ..., recompute: Polynomial | MPolynomial = ...
    ) -> ZZ | NumberFieldElement: ...
    def pari_label(self) -> NumberFieldElement: ...
    def signature(self) -> tuple[int, int]: ...
    def _element_constructor_(
        self, x: NumberFieldElement | ElementConstructorInput, check: bool = ...
    ) -> NumberFieldElement | identity | g: ...
    def is_galois(self) -> bool: ...
    def _repr_(self) -> str: ...
    def number_field(self) -> NumberField_generic: ...
    def list(self) -> list[Self]: ...
    def unrank(self, i: int | Integer) -> NumberFieldElement: ...
    def __iter__(self) -> Iterator[NumberFieldElement]: ...
    def decomposition_group(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
    ) -> NumberFieldElement: ...
    def complex_conjugation(
        self,
        P: NumberFieldIdeal
        | FunctionFieldPlace
        | Polynomial
        | DiscretePseudoValuation
        | None = ...,
    ) -> s: ...
    def ramification_group(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
        v: ElementConstructorInput,
    ) -> NumberFieldElement: ...
    def inertia_group(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
    ) -> NumberFieldElement: ...
    def ramification_breaks(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
    ) -> Set: ...
    def artin_symbol(
        self,
        P: NumberFieldIdeal | FunctionFieldPlace | Polynomial | DiscretePseudoValuation,
    ) -> NumberFieldElement: ...

class GaloisGroup_subgroup(GaloisSubgroup_perm):
    def fixed_field(
        self,
        name: str | None = ...,
        polred: Polynomial | MPolynomial | None = ...,
        threshold: Polynomial | MPolynomial | None = ...,
    ) -> (
        NumberField_generic
        | tuple[NumberField_generic, Morphism]
        | tuple[Field, NumberFieldElement]
        | tuple[NumberFieldElement, NumberFieldElement]
    ): ...
