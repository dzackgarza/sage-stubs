from collections.abc import Callable, Hashable, Iterable, Iterator
from typing import Literal, TypeAlias

from sage.categories.category import Category
from sage.structure.parent import Parent

_SearchAlgorithm: TypeAlias = Literal["depth", "breadth", "naive"]
_Structure: TypeAlias = Literal["symmetric", "forest", "graded"]

def RecursivelyEnumeratedSet(
    seeds: Iterable[Hashable],
    successors: Callable[[Hashable], Iterable[Hashable]],
    structure: _Structure | None = None,
    enumeration: _SearchAlgorithm | None = None,
    max_depth: float = ...,
    post_process: Callable[[Hashable], Hashable | None] | None = None,
    facade: Parent | None = None,
    category: Category | None = None,
) -> RecursivelyEnumeratedSet_generic | RecursivelyEnumeratedSet_forest: ...

class RecursivelyEnumeratedSet_generic(Parent):
    def __init__(
        self,
        seeds: Iterable[Hashable],
        successors: Callable[[Hashable], Iterable[Hashable]],
        enumeration: _SearchAlgorithm = "depth",
        max_depth: float = ...,
        post_process: Callable[[Hashable], Hashable | None] | None = None,
        facade: Parent | None = None,
        category: Category | None = None,
    ) -> None: ...
    def seeds(self) -> Iterable[Hashable]: ...
    def __iter__(self) -> Iterator[Hashable]: ...
    def __contains__(self, x: object) -> bool: ...

class RecursivelyEnumeratedSet_forest(Parent):
    def __init__(
        self,
        roots: Iterable[Hashable] | None = None,
        children: Callable[[Hashable], Iterable[Hashable]] | None = None,
        post_process: Callable[[Hashable], Hashable | None] | None = None,
        algorithm: _SearchAlgorithm = 'depth',
        facade: Parent | None = None,
        category: Category | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def roots(self) -> Iterable[Hashable]: ...
    def children(self, x: Hashable) -> Iterable[Hashable]: ...
    def __iter__(self) -> Iterator[Hashable]: ...
    def depth_first_search_iterator(self) -> Iterator[Hashable]: ...
    def breadth_first_search_iterator(self) -> Iterator[Hashable]: ...
    def _elements_of_depth_iterator_rec(self, depth: int = 0) -> Iterator[Hashable]: ...
    def elements_of_depth_iterator(self, depth: int = 0) -> Iterator[Hashable]: ...
    def __contains__(self, x: object) -> bool: ...
