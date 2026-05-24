from collections.abc import Callable
from typing import TypeAlias

from sage.categories.category import Category

from sage.structure.parent import Parent
from sage.structure.element import Element, Expression

_Names: TypeAlias = str | Expression | tuple[str | Expression, ...] | list[str | Expression] | None

class ConditionSet(Parent):
    def __init__(
        self,
        universe: Parent,
        *predicates: Callable[..., bool] | Expression,
        category: Category | None = ...,
        vars: _Names = ...,
        names: _Names = ...,
    ) -> None: ...
    def ambient(self) -> Parent: ...
