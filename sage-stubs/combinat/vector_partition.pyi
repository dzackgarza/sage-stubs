import builtins
from collections.abc import (
    Iterator as _Iterator,
)

from sage.structure.element import Element

class _SageObject: ...

def find_min(self) -> list[int]: ...
def IntegerVectorsIterator(self, min: builtins.object = ...) -> _SageObject: ...

class VectorPartition:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object, vecpar: builtins.object
    ) -> _SageObject: ...
    def __init__(self, parent: builtins.object, vecpar: builtins.object) -> None: ...
    def sum(self) -> list[Element]: ...
    def partition_at_vertex(self, i: builtins.int) -> _SageObject: ...

class VectorPartitions:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        vec: builtins.object,
        min: builtins.object = ...,
        parts: builtins.object = ...,
        distinct: builtins.bool = ...,
        is_repeatable: builtins.object = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        vec: builtins.object,
        min: builtins.object = ...,
        parts: builtins.object = ...,
        distinct: builtins.bool = ...,
        is_repeatable: builtins.object = ...,
    ) -> None: ...
    Element: _SageObject

    def __iter__(self) -> _Iterator[_SageObject]: ...
