from typing import Self

from sage.categories.category import Category
from sage.combinat.posets.cartesian_product import CartesianProductPoset
from sage.rings.asymptotic.asymptotic_ring import AsymptoticRing
from sage.rings.asymptotic.growth_group import GenericGrowthElement, GenericGrowthGroup
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.rings.ring import Ring
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.sage_object import SageObject
from sage.symbolic.units import one

class CartesianProductFactory(UniqueFactory):
    def create_key_and_extra_args(
        self,
        growth_groups: ElementConstructorInput,
        category: Category,
        **kwds: ElementConstructorInput,
    ) -> AsymptoticRing: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        args: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> CartesianProductFactory: ...

CartesianProductGrowthGroups: GenericGrowthElement

class GenericProduct(CartesianProductPoset, GenericGrowthGroup):
    def __init__(
        self,
        sets: ElementConstructorInput,
        category: Category,
        **kwds: ElementConstructorInput,
    ) -> None: ...
    def some_elements(self) -> list[GenericGrowthElement]: ...
    def cartesian_injection(
        self, factor: Ring, element: GenericGrowthElement | ElementConstructorInput
    ) -> GenericGrowthElement: ...
    def gens_monomial(self) -> tuple[GenericGrowthElement, ...]: ...
    def variable_names(self) -> tuple[str, ...]: ...

    class Element(SageObject):
        is_lt_one: bool

        def __pow__(self, exponent: int | Integer | Rational) -> Self: ...
        def factors(
            self,
        ) -> tuple[GenericGrowthElement, ...] | list[GenericGrowthElement]: ...
        log: Self
        log_factor: Self
        rpow: Self

        def exp(self) -> Self: ...
        def __invert__(self) -> Self: ...
        def variable_names(self) -> tuple[str, ...]: ...

    CartesianProduct: GenericGrowthElement

    def _element_constructor_(
        self, data: ElementConstructorInput
    ) -> GenericGrowthElement | one | ElementConstructorInput: ...
    def _coerce_map_from_(self, S: Ring | Parent) -> bool: ...

class UnivariateProduct(GenericProduct):
    def __init__(
        self,
        sets: ElementConstructorInput,
        category: Category,
        **kwargs: ElementConstructorInput,
    ) -> None: ...
    CartesianProduct: GenericGrowthElement

class MultivariateProduct(GenericProduct):
    def __init__(
        self,
        sets: ElementConstructorInput,
        category: Category,
        **kwargs: ElementConstructorInput,
    ) -> None: ...
    CartesianProduct: GenericGrowthElement
