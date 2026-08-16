import builtins

class _SageObject: ...

available_integrators: _SageObject

class IndefiniteIntegral:
    def __init__(self) -> None: ...

indefinite_integral: _SageObject

class DefiniteIntegral:
    def __init__(self) -> None: ...

definite_integral: _SageObject

def integrate(
    self,
    v: builtins.object = ...,
    a: builtins.object = ...,
    b: builtins.object = ...,
    algorithm: builtins.str = ...,
    hold: builtins.bool = ...,
) -> _SageObject: ...

integral: _SageObject
