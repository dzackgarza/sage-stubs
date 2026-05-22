from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.tensor import TensorProductsCategory
from sage.structure.parent import Parent

class FiniteCrystals(CategoryWithAxiom):
    def extra_super_categories(self) -> list[Category]: ...
    def example(self, n: int = 3) -> Parent: ...

    class TensorProducts(TensorProductsCategory):
        def extra_super_categories(self) -> list[Category]: ...
