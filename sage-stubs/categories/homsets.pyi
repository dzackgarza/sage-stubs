from sage.categories.covariant_functorial_construction import FunctorialConstructionCategory
from sage.categories.category_with_parameters import CategoryWithParameters
from sage.categories.category import Category, Category_singleton
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.structure.parent import Parent

class HomsetsCategory(FunctorialConstructionCategory, CategoryWithParameters):
    @classmethod
    def default_super_categories(cls, category: Category) -> Category: ...
    def base(self) -> Parent: ...

class HomsetsOf(HomsetsCategory): ...

class Homsets(Category_singleton):
    def super_categories(self) -> list[Category]: ...

    class Endset(CategoryWithAxiom):
        def extra_super_categories(self) -> list[Category]: ...

    class ParentMethods:
        def is_endomorphism_set(self) -> bool: ...
