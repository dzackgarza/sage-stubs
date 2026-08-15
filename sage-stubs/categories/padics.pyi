from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton

class pAdics(Category_singleton):
    def super_categories(self) -> list[Category]: ...
