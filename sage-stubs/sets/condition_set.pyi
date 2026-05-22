from collections.abc import Callable
from typing import Any

from sage.categories.category import Category

from sage.structure.parent import Parent

class ConditionSet(Parent):
    def __init__(
        self,
        ambient: Parent,
        predicate: Callable[[Any], bool],
        *,
        category: Category | None = ...,
        names: str | tuple[str, ...] | None = ...,
    ) -> None: ...
    def ambient(self) -> Parent: ...
