import builtins
from collections.abc import (
    Iterator as _Iterator,
)

class _SageObject: ...

class ShuffleProduct_abstract:
    def __init__(
        self,
        l1: builtins.object,
        l2: builtins.object,
        element_constructor: builtins.object = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __contains__(self, x: object) -> bool: ...

class SetShuffleProduct:
    def __init__(
        self,
        l1: builtins.object,
        l2: builtins.object,
        element_constructor: builtins.object = ...,
    ) -> None: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
    def cardinality(self) -> _SageObject: ...

class ShuffleProduct:
    def __init__(
        self,
        l1: builtins.object,
        l2: builtins.object,
        element_constructor: builtins.object = ...,
    ) -> None: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
    def __contains__(self, iterable: object) -> bool: ...
    def cardinality(self) -> _SageObject: ...

class ShuffleProduct_overlapping_r:
    r: builtins.int

    def __init__(
        self,
        w1: builtins.object,
        w2: builtins.object,
        r: builtins.int,
        element_constructor: builtins.object = ...,
        add: builtins.object = ...,
    ) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...

class ShuffleProduct_overlapping:
    def __init__(
        self,
        w1: builtins.object,
        w2: builtins.object,
        element_constructor: builtins.object = ...,
        add: builtins.object = ...,
    ) -> None: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...
