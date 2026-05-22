from sage.categories.category import Category
from sage.categories.covariant_functorial_construction import RegressiveCovariantConstructionCategory

class SubobjectsCategory(RegressiveCovariantConstructionCategory):
    @classmethod
    def default_super_categories(cls, category: Category) -> Category: ...

class Subobjects(SubobjectsCategory): ...
