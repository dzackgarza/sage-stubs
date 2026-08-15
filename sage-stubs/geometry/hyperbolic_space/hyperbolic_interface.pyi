# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

def HyperbolicSpace(n: builtins.int) -> _SageObject: ...

class HyperbolicPlane:
    def __init__(self) -> None: ...
    def a_realization(self) -> _SageObject: ...
    UHP: _SageObject
    UpperHalfPlane: _SageObject
    PD: _SageObject
    PoincareDisk: _SageObject
    KM: _SageObject
    KleinDisk: _SageObject
    HM: _SageObject
    Hyperboloid: _SageObject

class HyperbolicModels:
    def __init__(self, base: builtins.object) -> None: ...
    def super_categories(self) -> _SageObject: ...
    class ParentMethods:
        ...
