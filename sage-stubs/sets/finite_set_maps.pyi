from collections.abc import Iterator
from typing import Self

from sage.categories.category import Category
from sage.rings.integer import Integer
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from .finite_enumerated_set import FiniteEnumeratedSet
from .finite_set_map_cy import (
    FiniteSetEndoMap_N,
    FiniteSetEndoMap_Set,
    FiniteSetMap_MN,
    FiniteSetMap_Set,
)
from .integer_range import IntegerRange

class FiniteSetMaps(UniqueRepresentation, Parent):
    def __classcall_private__(
        cls,
        domain: Parent | list[object] | tuple[object, ...] | Integer | int,
        codomain: Parent | list[object] | tuple[object, ...] | Integer | int | None = ...,
        action: str = ...,
        category: Category | None = ...,
    ) -> FiniteSetMaps_MN | FiniteSetMaps_Set | FiniteSetEndoMaps_N | FiniteSetEndoMaps_Set: ...
    def cardinality(self) -> Integer: ...

class FiniteSetMaps_MN(FiniteSetMaps):
    def __init__(
        self,
        m: Integer | int,
        n: Integer | int,
        category: Category | None = ...,
    ) -> None: ...
    def domain(self) -> IntegerRange: ...
    def codomain(self) -> IntegerRange: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: FiniteSetMap_MN) -> bool: ...
    def an_element(self) -> FiniteSetMap_MN: ...
    def __iter__(self) -> Iterator[FiniteSetMap_MN]: ...
    def _from_list_(self, lst: list[int]) -> FiniteSetMap_MN: ...
    def _element_constructor_(self, *args: object, **kwargs: object) -> FiniteSetMap_MN: ...

class FiniteSetMaps_Set(FiniteSetMaps_MN):
    def __init__(
        self,
        domain: Parent | FiniteEnumeratedSet,
        codomain: Parent | FiniteEnumeratedSet,
        category: Category | None = ...,
    ) -> None: ...
    def from_dict(self, d: dict[object, object]) -> FiniteSetMap_Set: ...

class FiniteSetEndoMaps_N(FiniteSetMaps_MN):
    def __init__(
        self,
        n: Integer | int,
        action: str = ...,
        category: Category | None = ...,
    ) -> None: ...
    def one(self) -> FiniteSetEndoMap_N: ...
    def an_element(self) -> FiniteSetEndoMap_N: ...
    def _repr_(self) -> str: ...

class FiniteSetEndoMaps_Set(FiniteSetMaps_Set, FiniteSetEndoMaps_N):
    def __init__(
        self,
        domain: Parent | FiniteEnumeratedSet,
        action: str = ...,
        category: Category | None = ...,
    ) -> None: ...
