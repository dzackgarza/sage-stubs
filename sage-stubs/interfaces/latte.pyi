import builtins

class _SageObject: ...

def count(
    self,
    ehrhart_polynomial: builtins.bool = ...,
    multivariate_generating_function: builtins.bool = ...,
    raw_output: builtins.bool = ...,
    verbose: builtins.bool = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def integrate(
    self,
    polynomial: builtins.object = ...,
    algorithm: builtins.str = ...,
    raw_output: builtins.bool = ...,
    verbose: builtins.bool = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def to_latte_polynomial(self) -> _SageObject: ...
