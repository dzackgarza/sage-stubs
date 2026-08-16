import builtins
from collections.abc import (
    Iterable,
)

from sage.rings.integer import Integer

from .divisor import FunctionFieldDivisor

class _SageObject: ...

class JacobianPoint:
    def __init__(
        self,
        parent: JacobianGroup,
        finite_ideal: builtins.object,
        infinite_ideal: builtins.object,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def additive_order(self) -> Integer: ...
    def effective_part(self) -> FunctionFieldDivisor: ...
    def divisor(self) -> FunctionFieldDivisor: ...

class JacobianPoint_finite_field: ...

class JacobianGroup:
    Element: _SageObject

    def __init__(
        self,
        parent: builtins.object,
        function_field: builtins.object,
        base_div: builtins.object,
    ) -> None: ...
    def point(self, divisor: builtins.object) -> _SageObject: ...
    def zero(self) -> JacobianPoint: ...

class JacobianGroup_finite_field:
    Element: _SageObject

    def __iter__(self) -> Iterable[JacobianPoint_finite_field]: ...

class Jacobian:
    def __init__(
        self,
        function_field: builtins.object,
        base_div: builtins.object,
        cache_infinite_ideals: builtins.bool = ...,
        **kwds: builtins.object,
    ) -> None: ...
    def group(self, k_ext: builtins.object = ...) -> _SageObject: ...
