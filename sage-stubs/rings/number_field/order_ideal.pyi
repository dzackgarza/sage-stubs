from collections.abc import Sequence
from typing import Self

from sage.categories.morphism import Morphism
from sage.modules.free_module import FreeModule_generic
from sage.rings.ideal import Ideal_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.number_field.order import Order as NumberFieldOrder
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput

def NumberFieldOrderIdeal(
    O: NumberFieldOrder, *args: ElementConstructorInput, **kwds: ElementConstructorInput
) -> NumberFieldElement: ...

class NumberFieldOrderIdeal_generic(Ideal_generic):
    def __init__(
        self,
        O: NumberFieldOrder,
        gens: Sequence[ElementConstructorInput],
        *,
        coerce: ElementConstructorInput = ...,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def free_module(
        self,
    ) -> FreeModule_generic | tuple[FreeModule_generic, Morphism, Morphism]: ...
    def norm(self) -> Self: ...
    def _richcmp_(
        self,
        other: NumberFieldElement | ElementConstructorInput,
        op: ElementConstructorInput,
    ) -> bool: ...

class NumberFieldOrderIdeal_quadratic(NumberFieldOrderIdeal_generic):
    def __init__(
        self,
        O: NumberFieldOrder,
        gens: Sequence[ElementConstructorInput],
        *,
        coerce: ElementConstructorInput = ...,
    ) -> None: ...
    def conjugate(self) -> Self: ...
    def gens_two(self) -> Self: ...
    def is_principal(self) -> bool: ...
    def gens_reduced(self) -> Self: ...
    def is_equivalent(
        self,
        other: NumberFieldElement | ElementConstructorInput,
        narrow: ElementConstructorInput = ...,
    ) -> bool: ...
    def quadratic_form(self, *, basis: Polynomial | MPolynomial = ...) -> Self: ...
