# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class CharacteristicSpeciesStructure:
    def canonical_label(self) -> _SageObject: ...
    def transport(self, perm: builtins.object) -> _SageObject: ...
    def automorphism_group(self) -> _SageObject: ...

class CharacteristicSpecies:
    def __init__(self, n: builtins.int, min: builtins.object = ..., max: builtins.object = ..., weight: builtins.object = ...) -> None: ...

CharacteristicSpecies_class: _SageObject
class EmptySetSpecies:
    def __init__(self, min: builtins.object = ..., max: builtins.object = ..., weight: builtins.object = ...) -> None: ...

EmptySetSpecies_class: _SageObject
class SingletonSpecies:
    def __init__(self, min: builtins.object = ..., max: builtins.object = ..., weight: builtins.object = ...) -> None: ...

SingletonSpecies_class: _SageObject
