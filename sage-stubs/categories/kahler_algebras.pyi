from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.structure.element import Element, RingElement


class KahlerAlgebras(Category_over_base_ring[RingElement]):
    def super_categories(self) -> list[Category]: ...

    class ParentMethods:
        def poincare_pairing(
            self,
            a: Element,
            b: Element,
        ) -> RingElement: ...
        def lefschetz_element(self) -> Element: ...
        def hodge_riemann_relations(
            self,
            k: int,
        ) -> QuadraticForm: ...
