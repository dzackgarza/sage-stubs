from collections.abc import Sequence
from typing import Self

from sage.combinat.regular_sequence import value
from sage.graphs.pq_trees import P
from sage.groups.abelian_gps.values import (
    AbelianGroupWithValues_class,
    AbelianGroupWithValuesElement,
)
from sage.rings.function_field.ideal import FunctionFieldIdeal
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.ring import Ring
from sage.structure.parent import ElementConstructorInput, Parent

from .number_field_base import NumberField
from .number_field_ideal import NumberFieldIdeal

class ClassGroup(AbelianGroupWithValues_class):
    def gens_ideals(self) -> list[NumberFieldIdeal]: ...
    def number_field(self) -> NumberField: ...
    def __init__(
        self,
        gens_orders: ElementConstructorInput,
        names: str | tuple[str, ...] | None,
        number_field: ElementConstructorInput,
        gens: Sequence[ElementConstructorInput],
        proof: bool = ...,
    ) -> None: ...
    def _element_constructor_(
        self, *args: ElementConstructorInput, **kwds: ElementConstructorInput
    ) -> NumberFieldElement: ...
    def __iter__(self) -> NumberFieldElement: ...
    def _repr_(self) -> str: ...

class FractionalIdealClass(AbelianGroupWithValuesElement):
    def __init__(
        self,
        parent: Parent,
        element: bool,
        ideal: NumberFieldIdeal | FunctionFieldIdeal | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __pow__(self, n: int | Integer) -> Self: ...
    def inverse(self) -> Self: ...
    def is_principal(self) -> bool: ...
    def reduce(self) -> Self: ...
    def ideal(self) -> NumberFieldIdeal | FunctionFieldIdeal: ...
    def representative_prime(self, norm_bound: int | Integer = ...) -> value | P: ...
    def gens(self) -> tuple: ...

class SFractionalIdealClass(FractionalIdealClass):
    def _repr_(self) -> str: ...

class SClassGroup(ClassGroup):
    def __init__(
        self,
        gens_orders: ElementConstructorInput,
        names: str | tuple[str, ...] | None,
        number_field: ElementConstructorInput,
        gens: Sequence[ElementConstructorInput],
        S: Ring | Parent,
        proof: bool = ...,
    ) -> None: ...
    def S(self) -> NumberFieldElement: ...
    def _element_constructor_(
        self, *args: ElementConstructorInput, **kwds: ElementConstructorInput
    ) -> NumberFieldElement: ...
    def _repr_(self) -> str: ...
