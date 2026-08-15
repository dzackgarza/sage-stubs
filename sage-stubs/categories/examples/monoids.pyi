# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class FreeMonoid:
    def __init__(self, alphabet: builtins.tuple[_SageObject, ...] = ...) -> None: ...
    def one(self) -> _SageObject: ...
    def monoid_generators(self) -> _SageObject: ...
    class Element:
        wrapped_class: _SageObject

Example: _SageObject
