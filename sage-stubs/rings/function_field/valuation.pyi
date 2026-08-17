from collections.abc import Callable
from typing import Self

from sage.categories.map import Map
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.function_field import FunctionField
from sage.rings.function_field.place import FunctionFieldPlace
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.rings.ring import Ring
from sage.rings.valuation.mapped_valuation import (
    FiniteExtensionFromLimitValuation,
    MappedValuation_base,
)
from sage.rings.valuation.valuation import DiscretePseudoValuation, DiscreteValuation
from sage.structure.element import Element, RingElement
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput, Parent

class FunctionFieldValuationFactory(UniqueFactory):
    def create_key_and_extra_args(
        self, domain: Parent, prime: int | Integer | FunctionFieldPlace
    ) -> FunctionField: ...
    def create_key_and_extra_args_from_place(
        self, domain: Parent, generator: ElementConstructorInput
    ) -> FunctionField: ...
    def create_key_and_extra_args_from_valuation(
        self, domain: Parent, valuation: FunctionField
    ) -> FunctionField: ...
    def create_key_and_extra_args_from_valuation_on_isomorphic_field(
        self,
        domain: Parent,
        valuation: Ring,
        to_valuation_domain: Ring,
        from_valuation_domain: ElementConstructorInput,
    ) -> FunctionField: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        key: tuple[ElementConstructorInput, ...],
        **extra_args: ElementConstructorInput,
    ) -> FunctionFieldValuationFactory: ...

FunctionFieldValuation: FunctionFieldElement

class FunctionFieldValuation_base(DiscretePseudoValuation): ...

class DiscreteFunctionFieldValuation_base(DiscreteValuation):
    def extensions(self, L: FunctionField) -> list[FunctionFieldPlace]: ...

class RationalFunctionFieldValuation_base(FunctionFieldValuation_base):
    def element_with_valuation(
        self, s: FunctionFieldElement | ElementConstructorInput
    ) -> FunctionFieldElement: ...

class ClassicalFunctionFieldValuation_base(DiscreteFunctionFieldValuation_base): ...

class InducedRationalFunctionFieldValuation_base(FunctionFieldValuation_base):
    def __init__(
        self, parent: FunctionField, base_valuation: ElementConstructorInput
    ) -> None: ...
    def uniformizer(self) -> FunctionFieldElement: ...
    def lift(self, F: FunctionField) -> FunctionFieldElement: ...
    def value_group(self) -> FunctionFieldElement: ...
    def reduce(self, f: Polynomial | MPolynomial) -> FunctionFieldElement: ...
    def extensions(self, L: FunctionField) -> list[FunctionFieldPlace]: ...
    def residue_ring(self) -> Ring: ...
    def restriction(self, ring: Ring) -> Self: ...
    def simplify(
        self,
        f: Polynomial | MPolynomial,
        error: int | Integer | Rational | RealNumber = ...,
        force: bool = ...,
    ) -> Self: ...
    def _repr_(self) -> str: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> FunctionFieldElement: ...

class FiniteRationalFunctionFieldValuation(
    InducedRationalFunctionFieldValuation_base,
    ClassicalFunctionFieldValuation_base,
    RationalFunctionFieldValuation_base,
):
    def __init__(
        self, parent: FunctionField, base_valuation: ElementConstructorInput
    ) -> None: ...

class NonClassicalRationalFunctionFieldValuation(
    InducedRationalFunctionFieldValuation_base, RationalFunctionFieldValuation_base
):
    def __init__(
        self, parent: FunctionField, base_valuation: ElementConstructorInput
    ) -> None: ...
    def residue_ring(self) -> Ring: ...

class FunctionFieldFromLimitValuation(
    FiniteExtensionFromLimitValuation, DiscreteFunctionFieldValuation_base
):
    def __init__(
        self,
        parent: FunctionField,
        approximant: ElementConstructorInput,
        G: Polynomial | MPolynomial,
        approximants: ElementConstructorInput,
    ) -> None: ...
    def scale(self, scalar: RingElement | int | Integer | Rational) -> Self: ...

class FunctionFieldMappedValuation_base(
    FunctionFieldValuation_base, MappedValuation_base
):
    def __init__(
        self,
        parent: FunctionField,
        base_valuation: ElementConstructorInput,
        to_base_valuation_domain: ElementConstructorInput,
        from_base_valuation_domain: ElementConstructorInput,
    ) -> None: ...
    def scale(self, scalar: RingElement | int | Integer | Rational) -> Self: ...
    def is_discrete_valuation(self) -> bool: ...
    def _repr_(self) -> str: ...

class FunctionFieldMappedValuationRelative_base(FunctionFieldMappedValuation_base):
    def __init__(
        self,
        parent: FunctionField,
        base_valuation: ElementConstructorInput,
        to_base_valuation_domain: ElementConstructorInput,
        from_base_valuation_domain: ElementConstructorInput,
    ) -> None: ...
    def restriction(self, ring: Ring) -> Self: ...

class RationalFunctionFieldMappedValuation(
    FunctionFieldMappedValuationRelative_base, RationalFunctionFieldValuation_base
):
    def __init__(
        self,
        parent: FunctionField,
        base_valuation: ElementConstructorInput,
        to_base_valuation_doain: ElementConstructorInput,
        from_base_valuation_domain: ElementConstructorInput,
    ) -> None: ...

class InfiniteRationalFunctionFieldValuation(
    FunctionFieldMappedValuationRelative_base,
    RationalFunctionFieldValuation_base,
    ClassicalFunctionFieldValuation_base,
):
    def __init__(self, parent: FunctionField) -> None: ...
    def _repr_(self) -> str: ...

class FunctionFieldExtensionMappedValuation(FunctionFieldMappedValuationRelative_base):
    def restriction(self, ring: Ring) -> Self: ...
    def _repr_(self) -> str: ...
