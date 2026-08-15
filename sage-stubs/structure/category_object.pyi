from sage.categories.category import Category
from collections.abc import Sequence
from typing import TypeAlias
from sage.structure.sage_object import SageObject

NameSpec: TypeAlias = str | Sequence[str] | None

class CategoryObject(SageObject):
    def category(self) -> Category: ...
    def _init_category_(self, category: Category) -> None: ...
