from sage.categories.category import Category
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.signed_tensor import SignedTensorProductsCategory

class GradedCoalgebrasWithBasis(GradedModulesCategory):
    class SignedTensorProducts(SignedTensorProductsCategory):
        def extra_super_categories(self) -> list[Category]: ...
