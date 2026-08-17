from collections.abc import Callable, Sequence

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.modules.free_module import FreeModule_generic
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.ideal import FunctionFieldIdeal
from sage.rings.function_field.order import (
    FunctionFieldOrder,
    FunctionFieldOrderInfinite,
)
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.sets.family import Family
from sage.structure.element import Element
from sage.structure.parent import ElementConstructorInput

class FunctionFieldOrder_basis(FunctionFieldOrder):
    def __init__(self, basis: ElementConstructorInput, check: bool = ...) -> None: ...
    def ideal_with_gens_over_base(
        self, gens: Sequence[ElementConstructorInput]
    ) -> FunctionFieldElement: ...
    def ideal(self, *gens: ElementConstructorInput) -> FunctionFieldIdeal: ...
    def polynomial(self) -> Polynomial: ...
    def basis(self) -> Family[FunctionFieldElement]: ...
    def free_module(
        self,
    ) -> FreeModule_generic | tuple[FreeModule_generic, Morphism, Morphism]: ...
    def coordinate_vector(
        self, e: int | Integer | Rational
    ) -> FunctionFieldElement: ...
    def _element_constructor_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> FunctionFieldElement: ...

class FunctionFieldOrderInfinite_basis(FunctionFieldOrderInfinite):
    def __init__(self, basis: ElementConstructorInput, check: bool = ...) -> None: ...
    def ideal_with_gens_over_base(
        self, gens: Sequence[ElementConstructorInput]
    ) -> FunctionFieldElement: ...
    def ideal(self, *gens: ElementConstructorInput) -> FunctionFieldIdeal: ...
    def polynomial(self) -> Polynomial: ...
    def basis(self) -> Family[FunctionFieldElement]: ...
    def free_module(
        self,
    ) -> FreeModule_generic | tuple[FreeModule_generic, Morphism, Morphism]: ...
    def _element_constructor_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> FunctionFieldElement: ...
