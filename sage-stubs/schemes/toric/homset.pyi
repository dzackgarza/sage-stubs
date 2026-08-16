import builtins
from collections.abc import (
    Iterator as _Iterator,
)

class _SageObject: ...

class SchemeHomset_toric_variety:
    def __init__(
        self,
        X: builtins.object,
        Y: builtins.object,
        category: builtins.object = ...,
        check: builtins.bool = ...,
        base: builtins.object = ...,
    ) -> None: ...

class SchemeHomset_points_toric_base:
    def is_finite(self) -> bool: ...

class SchemeHomset_points_toric_field:
    def cardinality(self) -> _SageObject: ...
    def __iter__(self) -> _Iterator[_SageObject]: ...

class SchemeHomset_points_subscheme_toric_field:
    def __iter__(self) -> _Iterator[_SageObject]: ...
    def cardinality(self) -> _SageObject: ...
