from sage.categories.category import Category
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.function_field import FunctionField
from sage.rings.function_field.ideal import FunctionFieldIdeal, IdealMonoid
from sage.rings.number_field.number_field_ideal import NumberFieldIdeal
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import (
    CachedRepresentation,
    UniqueRepresentation,
)

class FunctionFieldOrder_base(CachedRepresentation, Parent):

    def __init__(
        self,
        field: FunctionField,
        ideal_class: ElementConstructorInput = ...,
        category: Category | None = ...,
    ) -> None: ...
    def is_field(self, proof: bool = ...) -> bool: ...
    def is_noetherian(self) -> bool: ...
    def function_field(self) -> FunctionFieldElement: ...
    def is_subring(
        self, other: FunctionFieldElement | ElementConstructorInput
    ) -> bool: ...
    def ideal_monoid(self) -> IdealMonoid: ...

class FunctionFieldOrder(FunctionFieldOrder_base):

    def _repr_(self) -> str: ...

class FunctionFieldOrderInfinite(FunctionFieldOrder_base):

    def _repr_(self) -> str: ...

class FunctionFieldMaximalOrder(UniqueRepresentation, FunctionFieldOrder):
    def _repr_(self) -> str: ...
    def unit_ideal(self) -> NumberFieldIdeal | FunctionFieldIdeal: ...

class FunctionFieldMaximalOrderInfinite(
    FunctionFieldMaximalOrder, FunctionFieldOrderInfinite
):
    def _repr_(self) -> str: ...
