import builtins
from collections.abc import (
    Iterator as _Iterator,
)

class _SageObject: ...

class BlobDiagram:
    def __init__(
        self,
        parent: builtins.object,
        marked: builtins.object,
        unmarked: builtins.object,
    ) -> None: ...
    def __hash__(self) -> builtins.int: ...
    def temperley_lieb_diagram(self) -> _SageObject: ...

class BlobDiagrams:
    def __init__(self, n: builtins.int) -> None: ...
    def cardinality(self) -> _SageObject: ...
    def order(self) -> _SageObject: ...
    def base_set(self) -> _SageObject: ...
    def __contains__(self, X: object) -> bool: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
    Element: _SageObject

class BlobAlgebra:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        k: builtins.int,
        q1: builtins.object,
        q2: builtins.object,
        q3: builtins.object,
        base_ring: builtins.object = ...,
        prefix: builtins.str = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        k: builtins.int,
        q1: builtins.object,
        q2: builtins.object,
        q3: builtins.object,
        base_ring: builtins.object,
        prefix: builtins.str,
    ) -> None: ...
    def order(self) -> _SageObject: ...
    def one_basis(self) -> _SageObject: ...
    def product_on_basis(
        self, top: builtins.object, bot: builtins.object
    ) -> _SageObject: ...
