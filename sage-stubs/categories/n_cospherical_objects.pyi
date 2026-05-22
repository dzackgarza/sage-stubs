from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.category_singleton import Category_singleton
else:
    Category_singleton = object

class nCosphericalObjects(Category_singleton): ...
