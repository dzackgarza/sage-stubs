# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

ROOTNODE: _SageObject
LEFT: _SageObject
RIGHT: _SageObject
UP: _SageObject
DOWN: _SageObject
COLUMN: _SageObject
INDEX: _SageObject
COUNT: _SageObject
class DLXMatrix:
    def __init__(self, ones: builtins.object, initialsolution: builtins.object = ...) -> None: ...
    def __eq__(self, other: builtins.object) -> builtins.bool: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
    def __next__(self) -> _SageObject: ...
    next: _SageObject

def AllExactCovers(M: builtins.int) -> _SageObject: ...

def OneExactCover(M: builtins.int) -> _SageObject: ...
