from collections.abc import Callable, Hashable, Iterable, Iterator, Sequence
from typing import TypeAlias

from sage.categories.category import Category
from sage.structure.category_object import CategoryObject
from sage.structure.element import Element, Expression
from sage.structure.parent import ParentCallInput, Set_generic
from sage.structure.unique_representation import UniqueRepresentation

from .set import Set_add_sub_operators, Set_base, Set_boolean_operators

_Predicate: TypeAlias = Callable[..., bool] | Expression
_Name: TypeAlias = str | Expression
_Names: TypeAlias = _Name | Iterable[_Name]
_SetElementInput: TypeAlias = Element | Hashable | list[Hashable]
_ConditionUniverse: TypeAlias = CategoryObject | Set_base | Iterable[_SetElementInput]

class ConditionSet(Set_generic, Set_base, Set_boolean_operators, Set_add_sub_operators, UniqueRepresentation):
    @staticmethod
    def __classcall_private__(
        cls: type[ConditionSet],
        universe: _ConditionUniverse,
        *predicates: _Predicate,
        vars: _Names | None = ...,
        names: _Names | None = ...,
        category: Category | None = ...,
    ) -> ConditionSet: ...
    def __init__(
        self,
        universe: _ConditionUniverse,
        *predicates: _Predicate,
        names: _Names | None = ...,
        category: Category | None = ...,
    ) -> None: ...
    def arguments(self) -> tuple[Expression, ...]: ...
    def _element_constructor_(self, *args: ParentCallInput, **kwds: ParentCallInput) -> Element: ...
    def _call_predicate(self, predicate: _Predicate, element: Element | Sequence[Element]) -> bool | Expression: ...
    def _an_element_(self) -> Element: ...
    def ambient(self) -> CategoryObject | Set_base | Iterable[_SetElementInput]: ...
    def __iter__(self) -> Iterator[Element]: ...
