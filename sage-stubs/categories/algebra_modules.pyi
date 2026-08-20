from typing import Self

from sage.categories.category import Category
from sage.categories.category_types import Category_module
from sage.structure.element import RingElement
from sage.structure.parent import Parent


class AlgebraModules(Category_module[RingElement]):
    def __init__(self, A: Parent[RingElement]) -> None: ...
    @classmethod
    def an_instance(cls) -> Self: ...
    def algebra(self) -> Parent[RingElement]: ...
    def super_categories(self) -> list[Category]: ...
