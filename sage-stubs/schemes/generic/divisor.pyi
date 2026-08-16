import builtins

from sage.structure.element import Element

class _SageObject: ...

def CurvePointToIdeal(self, P: builtins.int) -> _SageObject: ...

class Divisor_generic:
    def __init__(
        self,
        v: builtins.object,
        parent: builtins.object,
        check: builtins.bool = ...,
        reduce: builtins.bool = ...,
    ) -> None: ...
    def scheme(self) -> _SageObject: ...

class Divisor_curve:
    def __init__(
        self,
        v: builtins.object,
        parent: builtins.object = ...,
        check: builtins.bool = ...,
        reduce: builtins.bool = ...,
    ) -> None: ...
    def support(self) -> list[Element]: ...
    def coefficient(self, P: builtins.int) -> _SageObject: ...
