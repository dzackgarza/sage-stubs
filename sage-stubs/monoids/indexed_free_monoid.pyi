from collections.abc import Iterable, Iterator, Mapping, Sequence
from typing import Generic, Protocol, Self, TypeVar

from sage.categories.category import Category
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import MonoidElement
from sage.structure.indexed_generators import IndexedGenerators
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Index = TypeVar("_Index", default=int)


class IndexSet(Protocol[_Index]):
    def __contains__(self, value: object) -> bool: ...
    def __iter__(self) -> Iterator[_Index]: ...


type MonomialFactor[_Index] = tuple[_Index, int | Integer]
type FreeMonoidData[_Index] = tuple[MonomialFactor[_Index], ...]
type FreeAbelianMonoidData[_Index] = dict[_Index, int | Integer]
type IndexedMonoidInput[_Index] = (
    _Index
    | Sequence[MonomialFactor[_Index]]
    | Mapping[_Index, int | Integer]
    | IndexedMonoidElement[_Index]
    | None
)
type IndexedMonoidIndices[_Index] = Parent[_Index] | IndexSet[_Index] | Iterable[_Index]


class IndexedMonoidElement(MonoidElement, Generic[_Index]):
    def __init__(
        self,
        F: IndexedMonoid[_Index],
        x: FreeMonoidData[_Index] | FreeAbelianMonoidData[_Index],
    ) -> None: ...
    def parent(self) -> IndexedMonoid[_Index]: ...
    def _sorted_items(self) -> Sequence[MonomialFactor[_Index]]: ...
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
    def _mul_(self, other: Self) -> Self: ...
    def __pow__(self, exponent: int | Integer) -> Self: ...
    def __len__(self) -> int: ...
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
    def _sorted_items(self) -> Sequence[MonomialFactor[_Index]]: ...
    def _mul_(self, other: Self) -> Self: ...
    def __pow__(self, exponent: int | Integer) -> Self: ...
    def __floordiv__(self, divisor: Self) -> Self: ...
    def divides(self, other: Self) -> bool: ...
    def __len__(self) -> int: ...
    length = __len__
    def dict(self) -> FreeAbelianMonoidData[_Index]: ...


class IndexedMonoid(
    Parent[IndexedMonoidElement[_Index]],
    IndexedGenerators[IndexedMonoidIndices[_Index]],
    UniqueRepresentation,
    Generic[_Index],
):
    Element: type[IndexedMonoidElement[_Index]]
    element_class: type[IndexedMonoidElement[_Index]]

    @staticmethod
    def __classcall__(
        cls: type[IndexedMonoid[_Index]],
        indices: IndexedMonoidIndices[_Index],
        prefix: str | None = ...,
        names: str | Sequence[str] | None = ...,
        **kwds: object,
    ) -> IndexedMonoid[_Index]: ...
    def __init__(
        self,
        indices: IndexedMonoidIndices[_Index],
        prefix: str | None,
        category: Category | None = ...,
        names: str | Sequence[str] | None = ...,
        **kwds: object,
    ) -> None: ...
    def indices(self) -> IndexedMonoidIndices[_Index]: ...
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


class IndexedFreeMonoid(IndexedMonoid[_Index], Generic[_Index]):
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
    def gen(self, x: _Index) -> IndexedFreeAbelianMonoidElement[_Index]: ...
    def _an_element_(self) -> IndexedFreeAbelianMonoidElement[_Index]: ...
    def monoid_generators(self) -> AbstractFamily: ...
    gens = monoid_generators
