# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class MagmaExpr:
    ...

def magma_free_eval(code: builtins.str, strip: builtins.bool = ..., columns: builtins.int = ...) -> _SageObject: ...

class MagmaFree:
    def eval(self, x: builtins.object, **kwds: builtins.object) -> _SageObject: ...
    def __call__(self, code: builtins.object, strip: builtins.bool = ..., columns: builtins.int = ...) -> _SageObject: ...

magma_free: _SageObject
