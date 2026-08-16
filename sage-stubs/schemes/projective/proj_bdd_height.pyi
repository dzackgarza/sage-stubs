import builtins

class _SageObject: ...

def ZZ_points_of_bounded_height(
    self, dim: builtins.object, bound: builtins.object
) -> _SageObject: ...
def QQ_points_of_bounded_height(
    self, dim: builtins.object, bound: builtins.object, normalize: builtins.bool = ...
) -> _SageObject: ...
def IQ_points_of_bounded_height(
    self, K: builtins.int, dim: builtins.object, bound: builtins.object
) -> _SageObject: ...
def points_of_bounded_height(
    self,
    K: builtins.int,
    dim: builtins.object,
    bound: builtins.object,
    prec: builtins.int = ...,
) -> _SageObject: ...
