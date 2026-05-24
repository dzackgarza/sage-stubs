from collections.abc import Callable

from sage.categories.category import Category

from sage.structure.parent import Parent
from sage.structure.element import Element, Expression

class ConditionSet(Parent):
    def __init__(
        self,
        ambient: Parent,
        *predicates: Callable[..., bool] | Expression,
        category: Category | None = ...,
        names: str | tuple[str, ...] | None = ...,
    ) -> None: ...
    def ambient(self) -> Parent: ...
