from sage.categories.category import Category
from collections.abc import Sequence
from typing import TypeAlias

NameSpec: TypeAlias = str | Sequence[str] | None

class CategoryObject:
    def category(self) -> Category: ...
    def _init_category_(self, category: Category) -> None: ...
