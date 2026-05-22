from sage.categories.category_types import Category_ideal
from sage.categories.category import Category
from sage.structure.parent import Parent

class CommutativeRingIdeals(Category_ideal):
    def __init__(self, R: Parent) -> None: ...
    def super_categories(self) -> list[Category]: ...
