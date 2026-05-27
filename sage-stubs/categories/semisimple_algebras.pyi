from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.structure.element import Element

class SemisimpleAlgebras(Category_over_base_ring):
    class ParentMethods:
        def radical_basis(self) -> tuple[Element, ...]: ...
    class FiniteDimensional:
        ...
