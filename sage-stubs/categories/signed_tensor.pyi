from typing import Self
from sage.categories.covariant_functorial_construction import CovariantFunctorialConstruction, CovariantConstructionCategory
from sage.rings.ring import Ring

class SignedTensorProductFunctor(CovariantFunctorialConstruction): ...

tensor_signed: SignedTensorProductFunctor

class SignedTensorProductsCategory(CovariantConstructionCategory):
    def SignedTensorProducts(self) -> Self: ...
    def base(self) -> Ring: ...
