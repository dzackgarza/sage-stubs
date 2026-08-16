from collections.abc import Iterable, Iterator
from typing import Protocol

from sage.combinat.backtrack import GenericBacktracker

class CrystalElement(Protocol):
    def e(self, i: int) -> CrystalElement | None: ...
    def f(self, i: int) -> CrystalElement | None: ...

class CrystalProtocol(Protocol):
    def index_set(self) -> Iterable[int]: ...
    def highest_weight_vectors(self) -> Iterable[CrystalElement]: ...

class CrystalBacktracker(GenericBacktracker[CrystalElement | None, str | None]):
    def __init__(
        self,
        crystal: CrystalProtocol | _DataT,
        index_set: Iterable[int] | _StateT | None = None,
    ) -> None: ...
    def _rec(
        self, x: CrystalElement | _DataT | None, state: str | _StateT | None
    ) -> Iterator[tuple[CrystalElement, str, bool]]: ...
