from sage.categories.category import Category
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.signed_tensor import SignedTensorProductsCategory
from sage.structure.parent import Parent

class GradedAlgebras(GradedModulesCategory):
    class ParentMethods:
        def graded_algebra(self) -> Parent: ...
    class ElementMethods:
        ...
    class SubcategoryMethods:
        def SignedTensorProducts(self) -> Category: ...
    class SignedTensorProducts(SignedTensorProductsCategory):
        def extra_super_categories(self) -> list[Category]: ...
