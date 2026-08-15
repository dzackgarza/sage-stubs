# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class MarkedOutput:
    random: _SageObject
    rel_tol: _SageObject
    abs_tol: _SageObject
    tol: _SageObject
    def update(self, **kwds: builtins.object) -> _SageObject: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...

def make_marked_output(s: builtins.object, D: builtins.object) -> _SageObject: ...
