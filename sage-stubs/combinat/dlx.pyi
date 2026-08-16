import builtins
from collections.abc import (
    Iterator as _Iterator,
)

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
    def __init__(
        self, ones: builtins.object, initialsolution: builtins.object = ...
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
    def __next__(self) -> _SageObject: ...
    next: _SageObject

def AllExactCovers(self) -> _SageObject: ...
def OneExactCover(self) -> _SageObject: ...
