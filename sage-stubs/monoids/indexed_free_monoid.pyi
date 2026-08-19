from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from typing import Generic, Self, TypeVar

from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import MonoidElement
from sage.structure.indexed_generators import IndexedGenerators
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
type MonomialFactor[_Index: Hashable] = tuple[_Index, int | Integer]
type FreeMonoidData[_Index: Hashable] = tuple[MonomialFactor[_Index], ...]
type FreeAbelianMonoidData[_Index: Hashable] = dict[_Index, int | Integer]
type IndexedMonoidInput[_Index: Hashable] = (
    _Index
    | Sequence[MonomialFactor[_Index]]
    | Mapping[_Index, int | Integer]
    | IndexedMonoidElement[_Index]
    | None
)

class IndexedMonoidElement(
    MonoidElement,
    Generic[_Index],
):
    def __init__(
        self,
        F: IndexedMonoid[_Index],
        x: object,
    ) -> None: ...
    def parent(self) -> IndexedMonoid[_Index]: ...
    def _sorted_items(
        self,
    ) -> Sequence[MonomialFactor[_Index]]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def __iter__(
        self,
    ) -> Iterator[tuple[IndexedMonoidElement[_Index], int | Integer]]: ...
    def _richcmp_(
        self,
        other: IndexedMonoidElement[_Index],
        op: int,
    ) -> bool: ...
    def support(self) -> list[_Index]: ...
    def leading_support(self) -> _Index | None: ...
    def trailing_support(self) -> _Index | None: ...
    def to_word_list(self) -> list[_Index]: ...
    def is_one(self) -> bool: ...

class IndexedFreeMonoidElement(
    IndexedMonoidElement[_Index],
    Generic[_Index],
):
    def __init__(
        self,
        F: IndexedFreeMonoid[_Index],
        x: Iterable[MonomialFactor[_Index]],
    ) -> None: ...
    def parent(self) -> IndexedFreeMonoid[_Index]: ...
    def _sorted_items(self) -> FreeMonoidData[_Index]: ...
    def _mul_(
        self,
        other: IndexedFreeMonoidElement[_Index],
    ) -> Self: ...
    def __len__(self) -> int | Integer: ...
    length = __len__

class IndexedFreeAbelianMonoidElement(
    IndexedMonoidElement[_Index],
    Generic[_Index],
):
    def __init__(
        self,
        F: IndexedFreeAbelianMonoid[_Index],
        x: Mapping[_Index, int | Integer]
        | Iterable[MonomialFactor[_Index]],
    ) -> None: ...
    def parent(self) -> IndexedFreeAbelianMonoid[_Index]: ...
    def _sorted_items(
        self,
    ) -> Sequence[MonomialFactor[_Index]]: ...
    def _mul_(
        self,
        other: IndexedFreeAbelianMonoidElement[_Index],
    ) -> Self: ...
    def __pow__(
        self,
        n: int | Integer,
    ) -> Self: ...
    def __floordiv__(
        self,
        elt: IndexedFreeAbelianMonoidElement[_Index],
    ) -> Self: ...
    def divides(
        self,
        m: IndexedFreeAbelianMonoidElement[_Index],
    ) -> bool: ...
    def __len__(self) -> int | Integer: ...
    length = __len__
    def dict(self) -> FreeAbelianMonoidData[_Index]: ...

class IndexedMonoid(
    Parent[IndexedMonoidElement[_Index]],
    IndexedGenerators[object],
    UniqueRepresentation,
    Generic[_Index],
):
    Element: type[IndexedMonoidElement[_Index]]
    element_class: type[IndexedMonoidElement[_Index]]

    @staticmethod
    def __classcall__(
        cls: type[IndexedMonoid[_Index]],
        indices: object,
        prefix: str | None = ...,
        names: str | Sequence[str] | None = ...,
        **kwds: object,
    ) -> IndexedMonoid[_Index]: ...
    def __init__(
        self,
        indices: object,
        prefix: str | None,
        category: object | None = ...,
        names: str | Sequence[str] | None = ...,
        **kwds: object,
    ) -> None: ...
    def _first_ngens(
        self,
        n: int,
    ) -> tuple[IndexedMonoidElement[_Index], ...]: ...
    def _element_constructor_(
        self,
        x: IndexedMonoidInput[_Index] = ...,
    ) -> IndexedMonoidElement[_Index]: ...
    def _an_element_(self) -> IndexedMonoidElement[_Index]: ...
    def cardinality(self) -> Integer | PlusInfinity: ...
    def monoid_generators(self) -> AbstractFamily: ...
    gens = monoid_generators
    def one(self) -> IndexedMonoidElement[_Index]: ...
    def gen(self, x: _Index) -> IndexedMonoidElement[_Index]: ...

class IndexedFreeMonoid(
    IndexedMonoid[_Index],
    Generic[_Index],
):
    Element: type[IndexedFreeMonoidElement[_Index]]
    element_class: type[IndexedFreeMonoidElement[_Index]]
    def _repr_(self) -> str: ...
    def one(self) -> IndexedFreeMonoidElement[_Index]: ...
    def gen(self, x: _Index) -> IndexedFreeMonoidElement[_Index]: ...
    def _element_constructor_(
        self,
        x: _Index
        | Iterable[MonomialFactor[_Index]]
        | IndexedFreeMonoidElement[_Index]
        | None = ...,
    ) -> IndexedFreeMonoidElement[_Index]: ...
    def _an_element_(self) -> IndexedFreeMonoidElement[_Index]: ...
    def monoid_generators(self) -> AbstractFamily: ...
    gens = monoid_generators

class IndexedFreeAbelianMonoid(
    IndexedMonoid[_Index],
    Generic[_Index],
):
    Element: type[IndexedFreeAbelianMonoidElement[_Index]]
    element_class: type[IndexedFreeAbelianMonoidElement[_Index]]
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: _Index
        | Mapping[_Index, int | Integer]
        | Iterable[MonomialFactor[_Index]]
        | IndexedFreeAbelianMonoidElement[_Index]
        | None = ...,
    ) -> IndexedFreeAbelianMonoidElement[_Index]: ...
    def one(self) -> IndexedFreeAbelianMonoidElement[_Index]: ...
    def gen(
        self,
        x: _Index,
    ) -> IndexedFreeAbelianMonoidElement[_Index]: ...
    def _an_element_(self) -> IndexedFreeAbelianMonoidElement[_Index]: ...
    def monoid_generators(self) -> AbstractFamily: ...
    gens = monoid_generators
