from sage.categories.category_types import Category_over_base_ring
from sage.categories.category import Category
from sage.structure.element import Element
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.tensor import TensorProductsCategory
from sage.categories.dual import DualObjectsCategory
from sage.categories.super_modules import SuperModulesCategory
from sage.categories.filtered_modules import FilteredModulesCategory
from sage.categories.with_realizations import WithRealizationsCategory
from sage.categories.realizations import RealizationsCategory

class Coalgebras(Category_over_base_ring): # type: ignore[misc]
    def super_categories(self) -> list[Category]: ...

    class ParentMethods:
        def counit(self, x: Element) -> Element: ...
        def coproduct(self, x: Element) -> Element: ...

    class ElementMethods:
        def coproduct(self) -> Element: ...
        def counit(self) -> Element: ...

    class SubcategoryMethods:
        def Cocommutative(self) -> Category: ...

    class Cocommutative(CategoryWithAxiom_over_base_ring): ... # type: ignore[misc]

    class TensorProducts(TensorProductsCategory): # type: ignore[misc]
        def extra_super_categories(self) -> list[Category]: ...

        class ParentMethods: ...
        class ElementMethods: ...

    class DualObjects(DualObjectsCategory): # type: ignore[misc]
        def extra_super_categories(self) -> list[Category]: ...

    class Super(SuperModulesCategory): # type: ignore[misc]
        def extra_super_categories(self) -> list[Category]: ...

        class SubcategoryMethods:
            def Supercocommutative(self) -> Category: ...

        class Supercocommutative(CategoryWithAxiom_over_base_ring): ... # type: ignore[misc]

    class Filtered(FilteredModulesCategory): ... # type: ignore[misc]

    class WithRealizations(WithRealizationsCategory): # type: ignore[misc]
        class ParentMethods:
            def coproduct(self, x: Element) -> Element: ...
            def counit(self, x: Element) -> Element: ...

    class Realizations(RealizationsCategory): # type: ignore[misc]
        class ParentMethods:
            def coproduct_by_coercion(self, x: Element) -> Element: ...
            def counit_by_coercion(self, x: Element) -> Element: ...
