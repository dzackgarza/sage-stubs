from sage.categories.covariant_functorial_construction import (
    CovariantConstructionCategory,
    CovariantFunctorialConstruction,
)

class DualFunctor(CovariantFunctorialConstruction):
    _functor_name: str
    _functor_category: str
    symbol: str

class DualObjectsCategory(CovariantConstructionCategory):
    _functor_category: str
    def _repr_object_names(self) -> str: ...
