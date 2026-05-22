from typing import Self
from sage.categories.covariant_functorial_construction import CovariantConstructionCategory, CovariantFunctorialConstruction

class TensorProductFunctor(CovariantFunctorialConstruction):
    symbol: str
    unicode_symbol: str

tensor: TensorProductFunctor

class TensorProductsCategory(CovariantConstructionCategory):
    def TensorProducts(self) -> Self: ...
    def base(self) -> CovariantConstructionCategory | object: ...

class TensorProducts(TensorProductsCategory): ...
