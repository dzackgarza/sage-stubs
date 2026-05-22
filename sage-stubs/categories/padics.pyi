from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage.categories.category_singleton import Category_singleton
else:
    Category = object
    Category_singleton = object

class pAdics(Category_singleton):
    def super_categories(self) -> list['Category']: ...
