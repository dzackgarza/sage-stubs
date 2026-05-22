from collections.abc import Iterator
from typing import Generic, TypeVar

_DataT = TypeVar("_DataT")
_StateT = TypeVar("_StateT")

class GenericBacktracker(Generic[_DataT, _StateT]):
    def __init__(self, initial_data: _DataT, initial_state: _StateT) -> None: ...
    def __iter__(self) -> Iterator[_DataT]: ...
    def _rec(self, x: _DataT, state: _StateT) -> Iterator[tuple[_DataT, _StateT, bool]]: ...
