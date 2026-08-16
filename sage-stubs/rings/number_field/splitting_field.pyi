import builtins

from sage.rings.integer import Integer

class _SageObject: ...

class SplittingFieldAbort:
    def __init__(self, div: builtins.object, mult: builtins.object) -> None: ...

class SplittingData:
    dm: Integer

    def __init__(self, _pol: builtins.object, _dm: builtins.object) -> None: ...
    def key(self) -> _SageObject: ...
    def poldegree(self) -> _SageObject: ...

def splitting_field(
    self,
    name: builtins.str,
    map: builtins.bool = ...,
    degree_multiple: builtins.object = ...,
    abort_degree: builtins.object = ...,
    simplify: builtins.bool = ...,
    simplify_all: builtins.bool = ...,
) -> _SageObject: ...
