from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping
from typing import Generic, TypeVar

from sage.structure.parent import Parent

_K = TypeVar("_K")
_V = TypeVar("_V")

class AbstractFamily(Parent, Generic[_K, _V]):
    def hidden_keys(self) -> list[Hashable]: ...
    def keys(self) -> Iterable[_K]: ...
    def __iter__(self) -> Iterator[_V]: ...
    def __getitem__(self, i: _K) -> _V: ...

class FiniteFamily(AbstractFamily[_K, _V]): ...

class LazyFamily(AbstractFamily[_K, _V]): ...

def Family(
    indices: Iterable[_K] | Mapping[_K, _V],
    function: Callable[[_K], _V] | None = None,
    hidden_keys: Iterable[_K] = ...,
    hidden_function: Callable[[_K], _V] | None = None,
    lazy: bool = False,
    name: str | None = None,
) -> AbstractFamily[_K, _V]: ...
