from collections.abc import Iterable
from typing import Self

from .category import Category
from .covariant_functorial_construction import (
    CovariantConstructionCategory,
    CovariantFunctorialConstruction,
    _ConstructionKwarg,
)
from sage.rings.ring import Ring
from sage.sets.cartesian_product import CartesianProduct
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

class CartesianProductFunctor(CovariantFunctorialConstruction): ...

class CartesianProductsCategory(CovariantConstructionCategory):
    def CartesianProducts(self) -> Self: ...
    def base_ring(self) -> Ring: ...
    class ParentMethods:
        def __init_extra__(self) -> None: ...

class _CartesianProductCallable:
    def __call__(
        self, args: Iterable[SageObject], **kwargs: _ConstructionKwarg
    ) -> CartesianProduct: ...
    def category_from_parents(self, parents: Iterable[Parent]) -> Category: ...

cartesian_product: _CartesianProductCallable
