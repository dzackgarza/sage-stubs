from typing import TYPE_CHECKING

from sage.structure.parent import Parent
from sage.categories.category import Category

class Functor:
    def __call__(self, x: object) -> Parent | Category: ...
