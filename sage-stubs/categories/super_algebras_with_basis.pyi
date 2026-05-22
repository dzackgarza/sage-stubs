from sage.categories.category import Category
from sage.categories.signed_tensor import SignedTensorProductsCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.structure.element import Element
from sage.structure.parent import Parent

class SuperAlgebrasWithBasis(SuperModulesCategory):
    def extra_super_categories(self) -> list[Category]: ...
    class ParentMethods:
        def graded_algebra(self) -> Parent: ...
    class ElementMethods:
        def supercommutator(self, x: Element) -> Element: ...
    class SignedTensorProducts(SignedTensorProductsCategory):
        def extra_super_categories(self) -> list[Category]: ...
