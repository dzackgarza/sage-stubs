from collections.abc import Iterator
from typing import TypeVar

_M = TypeVar("_M")

def multiplicative_iterator(self) -> Iterator[object]: ...
def abelian_iterator(self) -> Iterator[object]: ...
