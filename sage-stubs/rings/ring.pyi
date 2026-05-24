from collections.abc import Iterator
from typing import NoReturn, TypeAlias, overload

from sage.categories.category import Category
from sage.rings.ideal import Ideal_generic as Ideal
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.number_field.number_field_ideal import NumberFieldIdeal
from sage.rings.number_field.order import Order as NumberFieldOrder
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.category_object import NameSpec
from sage.structure.parent import Parent
from sage.structure.element import Element

_ExtensionKeyword: TypeAlias = None | list[None]
_RingInitArg: TypeAlias = Parent | NameSpec | bool | Category | None
_IdealGenerator: TypeAlias = Element | int | Integer
_IdealInput: TypeAlias = (
    _IdealGenerator
    | Ideal
    | tuple[_IdealGenerator, ...]
    | list[_IdealGenerator]
)
_IdealKeyword: TypeAlias = bool | str | type[Ideal]
_QuotientInput: TypeAlias = Ideal | _IdealGenerator | tuple[_IdealGenerator, ...]

class Ring(Parent):
    def __init__(
        self,
        base: Parent,
        names: NameSpec = None,
        normalize: bool = True,
        category: Category | None = None,
    ) -> None: ...
    def __iter__(self) -> Iterator[Element]: ...
    def __len__(self) -> int: ...
    def __xor__(self, n: int | Integer | tuple[int | Integer, int | Integer]) -> NoReturn: ...
    def base_extend(self, X: Parent) -> Parent: ...
    def category(self) -> Category: ...
    def __mul__(self, x: _IdealInput) -> Ideal: ...
    def zero(self) -> Element: ...
    def one(self) -> Element: ...
    def order(self) -> int | Integer | PlusInfinity | NumberFieldOrder: ...
    
    def characteristic(self) -> int | Integer: ...
    def is_commutative(self) -> bool: ...
    def is_field(self) -> bool: ...
    def is_finite(self) -> bool: ...
    def is_integral_domain(self) -> bool: ...
    def is_noetherian(self) -> bool: ...
    def is_zero(self) -> bool: ...
    def base_ring(self) -> Ring: ...
    def fraction_field(self) -> Field: ...
    def ideal(self, *args: _IdealInput, **kwds: _IdealKeyword) -> Ideal | NumberFieldIdeal: ...
    def quotient(self, I: _QuotientInput, names: NameSpec = None, **kwds: _IdealKeyword) -> Ring: ...

class CommutativeRing(Ring):
    def __init__(self, *args: _RingInitArg, **kwds: _RingInitArg) -> None: ...
    def extension(
        self,
        poly: Polynomial,
        name: str | None = ...,
        names: str | tuple[str, ...] | None = ...,
        *,
        structure: _ExtensionKeyword = ...,
        implementation: _ExtensionKeyword = ...,
        prec: _ExtensionKeyword = ...,
        embedding: _ExtensionKeyword = ...,
        latex_name: _ExtensionKeyword = ...,
        latex_names: _ExtensionKeyword = ...,
    ) -> Ring: ...
    def krull_dimension(self) -> int: ...
    def _pseudo_fraction_field(self) -> Ring: ...

class IntegralDomain(Ring):
    def __init__(self, *args: _RingInitArg, **kwds: _RingInitArg) -> None: ...

class NoetherianRing(Ring):
    def __init__(self, *args: _RingInitArg, **kwds: _RingInitArg) -> None: ...

class DedekindDomain(Ring):
    def __init__(self, *args: _RingInitArg, **kwds: _RingInitArg) -> None: ...

class PrincipalIdealDomain(Ring):
    def __init__(self, *args: _RingInitArg, **kwds: _RingInitArg) -> None: ...

def _is_Field(x: Parent | int | Integer) -> bool: ...

class Field(CommutativeRing):
    def algebraic_closure(self) -> Field: ...
    @overload
    def extension(
        self,
        poly: Polynomial,
        name: str | None = ...,
        names: str | tuple[str, ...] | None = ...,
        *,
        structure: _ExtensionKeyword = ...,
        implementation: _ExtensionKeyword = ...,
        prec: _ExtensionKeyword = ...,
        embedding: _ExtensionKeyword = ...,
        latex_name: _ExtensionKeyword = ...,
        latex_names: _ExtensionKeyword = ...,
    ) -> Field: ...
    @overload
    def extension(
        self,
        poly: Polynomial | NumberFieldElement,
        name: str | None = ...,
        names: str | tuple[str, ...] | None = ...,
        latex_name: str | None = ...,
        latex_names: str | tuple[str, ...] | None = ...,
        *args: str,
        **kwds: str,
    ) -> Field: ...

class Algebra(Ring):
    def __init__(
        self, base_ring: Parent, *args: _RingInitArg, **kwds: _RingInitArg
    ) -> None: ...

class CommutativeAlgebra(Ring):
    def __init__(
        self, base_ring: Parent, *args: _RingInitArg, **kwds: _RingInitArg
    ) -> None: ...
