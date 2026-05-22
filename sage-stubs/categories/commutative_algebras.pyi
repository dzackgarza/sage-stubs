from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.tensor import TensorProductsCategory
from sage.categories.category import Category

class CommutativeAlgebras(CategoryWithAxiom_over_base_ring): # type: ignore[misc]
    def __contains__(self, A: object) -> bool: ...

    class TensorProducts(TensorProductsCategory): # type: ignore[misc]
        def extra_super_categories(self) -> list[Category]: ...
