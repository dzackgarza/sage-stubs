from typing import TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")

class CallableDict(dict[_K, _V]):
    def __call__(self, key: _K) -> _V: ...
