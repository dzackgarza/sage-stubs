from collections.abc import Callable, Iterable, Iterator
from typing import TypeAlias

from sage.structure.sage_object import SageObject

_LazyListMaterialized: TypeAlias = list[object]

class lazy_list_generic:
    cache: _LazyListMaterialized
    start: int
    stop: int
    step: int
    master: lazy_list_generic | None

    def __init__(
        self,
        cache: _LazyListMaterialized | None = None,
        start: int | None = None,
        stop: int | None = None,
        step: int | None = None,
    ) -> None: ...
    def list(self) -> _LazyListMaterialized: ...
    def _info(self) -> None: ...
    def __add__(self, other: Iterable[object]) -> lazy_list_from_iterator: ...
    def __reduce__(self) -> tuple[object, ...]: ...
    def _fit(self, n: int) -> int: ...
    def get(self, i: int) -> SageObject: ...
    def __call__(self, i: int) -> SageObject: ...
    def __iter__(self) -> Iterator[object]: ...
    def __getitem__(self, key: int | slice) -> object | lazy_list_generic: ...
    def _update_cache_up_to(self, i: int) -> int: ...
    def _get_cache_(self) -> _LazyListMaterialized: ...

class lazy_list_from_iterator(lazy_list_generic):
    iterator: Iterator[object]
    def __init__(
        self,
        iterator: Iterator[object],
        cache: _LazyListMaterialized | None = None,
        stop: int | None = None,
    ) -> None: ...
    def __reduce__(self) -> tuple[object, ...]: ...
    def _update_cache_up_to(self, i: int) -> int: ...

class lazy_list_from_function(lazy_list_generic):
    callable: Callable[[int], object]
    def __init__(
        self,
        function: Callable[[int], object],
        cache: _LazyListMaterialized | None = None,
        stop: int | None = None,
    ) -> None: ...
    def __reduce__(self) -> tuple[object, ...]: ...
    def _update_cache_up_to(self, i: int) -> int: ...

class lazy_list_from_update_function(lazy_list_generic):
    update_function: Callable[[_LazyListMaterialized], None]
    def __init__(
        self,
        function: Callable[[_LazyListMaterialized], None],
        cache: _LazyListMaterialized | None = None,
        stop: int | None = None,
    ) -> None: ...
    def __reduce__(self) -> tuple[object, ...]: ...
    def _update_cache_up_to(self, i: int) -> int: ...

def lazy_list(
    data: Iterable[object] | Callable[[int], object] | list[object] | tuple[object, ...] | lazy_list_generic | None = None,
    initial_values: list[object] | None = None,
    start: int | None = None,
    stop: int | None = None,
    step: int | None = None,
    update_function: Callable[[list[object]], None] | None = None,
) -> lazy_list_generic: ...
def slice_unpickle(master: lazy_list_generic, start: int, stop: int, step: int) -> lazy_list_generic: ...
def lazy_list_formatter(
    L: Iterable[object],
    name: str = ...,
    separator: str = ...,
    more: str = ...,
    opening_delimiter: str = ...,
    closing_delimiter: str = ...,
    preview: int = ...,
) -> str: ...
