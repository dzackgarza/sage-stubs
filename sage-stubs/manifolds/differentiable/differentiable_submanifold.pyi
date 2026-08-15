# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class DifferentiableSubmanifold:
    def __init__(self, n: builtins.int, name: builtins.str, field: builtins.object, structure: builtins.object, ambient: builtins.object = ..., base_manifold: builtins.object = ..., diff_degree: builtins.object = ..., latex_name: builtins.str = ..., start_index: builtins.int = ..., category: builtins.object = ..., unique_tag: builtins.object = ...) -> None: ...
    def open_subset(self, name: builtins.str, latex_name: builtins.str = ..., coord_def: builtins.dict[_SageObject, _SageObject] = ..., supersets: builtins.object = ...) -> _SageObject: ...
