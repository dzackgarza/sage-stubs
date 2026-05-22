from sage.categories.category import Category
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory

class IsomorphicObjectsCategory(RegressiveCovariantConstructionCategory):
    @classmethod
    def default_super_categories(cls, category: Category) -> Category: ...

class IsomorphicObjects(IsomorphicObjectsCategory): ...
