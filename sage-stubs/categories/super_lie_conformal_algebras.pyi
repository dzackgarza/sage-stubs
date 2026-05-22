from sage.categories.category import Category
from sage.categories.graded_modules import GradedModulesCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.structure.parent import Parent

class SuperLieConformalAlgebras(SuperModulesCategory):
    def extra_super_categories(self) -> list[Category]: ...
    def example(self) -> Parent: ...

    class ParentMethods:
        def _test_jacobi(self, **options: object) -> None: ...

    class ElementMethods:
        def is_even_odd(self) -> int: ...

    class Graded(GradedModulesCategory):
        def _repr_object_names(self) -> str: ...
