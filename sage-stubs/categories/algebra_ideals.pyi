from sage.categories.category import Category
from sage.categories.category_types import Category_ideal
from sage.structure.element import RingElement
from sage.structure.parent import Parent


class AlgebraIdeals(Category_ideal):
    def __init__(self, A: Parent[RingElement]) -> None: ...
    def algebra(self) -> Parent[RingElement]: ...
    def super_categories(self) -> list[Category]: ...
