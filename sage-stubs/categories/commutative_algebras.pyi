from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.tensor import TensorProductsCategory
from sage.categories.category import Category

class CommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    def __contains__(self, x: object) -> bool: ...

    class TensorProducts(TensorProductsCategory):
        def extra_super_categories(self) -> list[Category]: ...
