from sage.categories.category import Category
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory

class QuotientsCategory(RegressiveCovariantConstructionCategory):
    _functor_category: str
    @classmethod
    def default_super_categories(cls, category: Category) -> Category: ...
