# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class ManifoldObjectFiniteFamily:
    def __init__(self, objects: builtins.tuple[_SageObject, ...] = ..., keys: builtins.object = ...) -> None: ...
    def __lt__(self, other: builtins.object) -> builtins.bool: ...

class ManifoldSubsetFiniteFamily:
    @classmethod
    def from_subsets_or_families(cls, *subsets_or_families: builtins.object) -> _SageObject: ...
