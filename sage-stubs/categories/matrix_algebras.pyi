from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.structure.element import RingElement


class MatrixAlgebras(Category_over_base_ring[RingElement]):
    def super_categories(self) -> list[Category]: ...
