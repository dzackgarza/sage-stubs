# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

class NilpotentLieAlgebra_dense:
    @staticmethod
    def __classcall_private__(cls: builtins.object, R: builtins.int, s_coeff: builtins.object, names: builtins.object = ..., index_set: builtins.object = ..., category: builtins.object = ..., **kwds: builtins.object) -> _SageObject: ...
    def __init__(self, R: builtins.int, s_coeff: builtins.object, names: builtins.object, index_set: builtins.object, step: builtins.int = ..., **kwds: builtins.object) -> None: ...

class FreeNilpotentLieAlgebra:
    @staticmethod
    def __classcall_private__(cls: builtins.object, R: builtins.int, r: builtins.int, s: builtins.object, names: builtins.object = ..., naming: builtins.str = ..., category: builtins.object = ..., **kwds: builtins.object) -> _SageObject: ...
    def __init__(self, R: builtins.int, r: builtins.int, s: builtins.object, names: builtins.object, naming: builtins.object, category: builtins.object, **kwds: builtins.object) -> None: ...
    class options:
        NAME: _SageObject
        module: _SageObject
        display: _SageObject
    def degree_on_basis(self, w: builtins.object) -> builtins.int: ...
