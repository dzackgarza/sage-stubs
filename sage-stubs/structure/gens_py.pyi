from collections.abc import Iterator
from typing import TypeVar

_M = TypeVar("_M")

def multiplicative_iterator(M: _M) -> Iterator[object]: ...
def abelian_iterator(M: _M) -> Iterator[object]: ...
