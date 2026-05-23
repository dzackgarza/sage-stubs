from collections.abc import Callable, Hashable, Iterable, Iterator
from typing import TypeAlias

from sage.categories.category import Category
from sage.structure.element import Element
from sage.structure.element import InfinityElement
from sage.structure.parent import Parent

_RecursiveElement: TypeAlias = Element | Hashable
_SearchAlgorithm: TypeAlias = str
_Structure: TypeAlias = str

def RecursivelyEnumeratedSet(
    seeds: Iterable[_RecursiveElement],
    successors: Callable[[_RecursiveElement], Iterable[_RecursiveElement]],
    structure: _Structure | None = None,
    enumeration: _SearchAlgorithm | None = None,
    max_depth: float | InfinityElement = ...,
    post_process: Callable[[_RecursiveElement], _RecursiveElement | None] | None = None,
    facade: Parent | None = None,
    category: Category | None = None,
) -> RecursivelyEnumeratedSet_generic | RecursivelyEnumeratedSet_forest: ...

class RecursivelyEnumeratedSet_generic(Parent):
    def __init__(
        self,
        seeds: Iterable[_RecursiveElement],
        successors: Callable[[_RecursiveElement], Iterable[_RecursiveElement]],
        enumeration: _SearchAlgorithm = "depth",
        max_depth: float | InfinityElement = ...,
        post_process: Callable[[_RecursiveElement], _RecursiveElement | None] | None = None,
        facade: Parent | None = None,
        category: Category | None = None,
    ) -> None: ...
    def seeds(self) -> Iterable[_RecursiveElement]: ...
    def __iter__(self) -> Iterator[_RecursiveElement]: ...
    def __contains__(self, x: object) -> bool: ...

class RecursivelyEnumeratedSet_forest(Parent):
    def __init__(
        self,
        roots: Iterable[_RecursiveElement] | None = None,
        children: Callable[[_RecursiveElement], Iterable[_RecursiveElement]] | None = None,
        post_process: Callable[[_RecursiveElement], _RecursiveElement | None] | None = None,
        algorithm: _SearchAlgorithm = 'depth',
        facade: Parent | None = None,
        category: Category | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def roots(self) -> Iterable[_RecursiveElement]: ...
    def children(self, x: _RecursiveElement) -> Iterable[_RecursiveElement]: ...
    def __iter__(self) -> Iterator[_RecursiveElement]: ...
    def depth_first_search_iterator(self) -> Iterator[_RecursiveElement]: ...
    def breadth_first_search_iterator(self) -> Iterator[_RecursiveElement]: ...
    def _elements_of_depth_iterator_rec(self, depth: int = 0) -> Iterator[_RecursiveElement]: ...
    def elements_of_depth_iterator(self, depth: int = 0) -> Iterator[_RecursiveElement]: ...
    def __contains__(self, x: object) -> bool: ...
