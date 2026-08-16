from collections.abc import Callable, Hashable, Iterator
from typing import Generic, Protocol, TypeVar

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.sets_cat import Sets
from sage.rings.integer import Integer
from sage.sets.set import Set_add_sub_operators, Set_base, Set_boolean_operators
from sage.structure.element import Element
from sage.structure.parent import Parent

type _ImageElement = Element | Hashable | list[Hashable]
_DomainElement = TypeVar("_DomainElement")
_CodomainElement = TypeVar("_CodomainElement")

class SympySet(Protocol):
    def _sage_(self) -> Parent: ...

class ImageSubobject(
    Sets.ParentMethods[_CodomainElement], Generic[_DomainElement, _CodomainElement]
):
    def __init__(
        self,
        map: Map[_DomainElement, _CodomainElement]
        | Callable[[_DomainElement], _CodomainElement],
        domain_subset: Parent[_DomainElement],
        *,
        category: Category | None = ...,
        is_injective: bool | str | None = ...,
        inverse: Map[_CodomainElement, _DomainElement]
        | Callable[[_CodomainElement], _DomainElement]
        | None = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def _element_constructor_(self, x: _ImageElement) -> _ImageElement: ...
    def ambient(self) -> Parent[ImageSubobject] | None: ...
    def lift(self, x: _CodomainElement) -> _CodomainElement: ...
    def retract(self, x: _CodomainElement) -> _CodomainElement: ...
    def cardinality(self) -> Integer: ...
    def __iter__(self) -> Iterator[Element]: ...
    def __contains__(self, x: object) -> bool: ...
    def _an_element_(self) -> _ImageElement: ...
    def _sympy_(self) -> SympySet: ...

class ImageSet(
    ImageSubobject[_DomainElement, _CodomainElement],
    Set_base,
    Set_add_sub_operators,
    Set_boolean_operators,
): ...
