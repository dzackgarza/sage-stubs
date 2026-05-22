from collections.abc import Callable, Iterable, Mapping
from typing import TypeVar

from sage.structure.parent import Parent

_K = TypeVar("_K")
_V = TypeVar("_V")

class AbstractFamily(Parent): ...

class FiniteFamily(AbstractFamily): ...

class LazyFamily(AbstractFamily): ...

def Family(
    indices: Iterable[_K] | Mapping[_K, _V],
    function: Callable[[_K], _V] | None = None,
    hidden_keys: Iterable[_K] = ...,
    hidden_function: Callable[[_K], _V] | None = None,
    lazy: bool = False,
    name: str | None = None,
) -> AbstractFamily: ...
