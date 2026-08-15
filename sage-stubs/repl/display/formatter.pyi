# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

IPYTHON_NATIVE_TYPES: _SageObject
PLAIN_TEXT: _SageObject
TEXT_LATEX: _SageObject
TEXT_HTML: _SageObject
class SageDisplayFormatter:
    def __init__(self, *args: builtins.object, **kwds: builtins.object) -> None: ...
    def format(self, obj: builtins.object, include: builtins.object = ..., exclude: builtins.object = ...) -> _SageObject: ...

class SagePlainTextFormatter:
    def __init__(self, *args: builtins.object, **kwds: builtins.object) -> None: ...
    def __call__(self, obj: builtins.object) -> _SageObject: ...
