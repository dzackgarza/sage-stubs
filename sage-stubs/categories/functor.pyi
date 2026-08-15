from typing import TYPE_CHECKING, Any

from sage.structure.parent import Parent
from sage.categories.category import Category
class Functor:
    def __call__(self, *args: Any, **kwargs: Any) -> Parent | Category: ...
