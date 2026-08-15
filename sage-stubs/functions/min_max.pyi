# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class MinMax_base:
    def eval_helper(self, this_f: builtins.object, builtin_f: builtins.object, initial_val: builtins.object, args: builtins.object) -> _SageObject: ...
    def __call__(self, *args: builtins.object, **kwds: builtins.object) -> _SageObject: ...

class MaxSymbolic:
    def __init__(self) -> None: ...

max_symbolic: _SageObject
class MinSymbolic:
    def __init__(self) -> None: ...

min_symbolic: _SageObject
