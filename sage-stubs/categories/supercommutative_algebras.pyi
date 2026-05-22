from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.signed_tensor import SignedTensorProductsCategory

class SupercommutativeAlgebras(CategoryWithAxiom_over_base_ring):
    class SignedTensorProducts(SignedTensorProductsCategory):
        def extra_super_categories(self) -> list[Category]: ...

    class WithBasis(CategoryWithAxiom_over_base_ring):
        class ParentMethods:
            def _test_supercommutativity(self, **options: object) -> None: ...
