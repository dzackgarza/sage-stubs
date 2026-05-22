from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.category_types import Category_over_base_ring
from sage.algebras.lie_algebras.verma_module import VermaModule
from sage.algebras.lie_algebras.bgg_dual_module import SimpleModule
from sage.categories.category import Category
from sage.modules.module import Module
from sage.structure.element import Element
from sage.categories.morphism import Morphism

class TriangularKacMoodyAlgebras(Category_over_base_ring):
    def super_categories(self) -> list[Category]: ...

    class ParentMethods:
        def e(self, i: object | None = ...) -> Element: ...
        def f(self, i: object | None = ...) -> Element: ...
        def verma_module(self, la: object, basis_key: object | None = ..., **kwds: object) -> VermaModule: ...
        def simple_module(self, la: object, basis_key: object | None = ..., **kwds: object) -> SimpleModule | VermaModule: ...

    class ElementMethods:
        def part(self) -> int: ...

    class FiniteDimensional(CategoryWithAxiom_over_base_ring):
        class ParentMethods:
            def transpose(self) -> Morphism: ...

        class ElementMethods:
            def transpose(self) -> Element: ...
