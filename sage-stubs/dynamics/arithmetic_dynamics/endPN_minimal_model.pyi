import builtins

class _SageObject: ...

def bCheck(
    self, v: builtins.object, p: builtins.int, b: builtins.object
) -> _SageObject: ...
def scale(self, v: builtins.object, p: builtins.int) -> _SageObject: ...
def blift(
    self,
    Li: builtins.object,
    p: builtins.int,
    k: builtins.int,
    S: builtins.object = ...,
    all_orbits: builtins.bool = ...,
) -> _SageObject: ...
def affine_minimal(
    self,
    return_transformation: builtins.bool = ...,
    D: builtins.object = ...,
    quick: builtins.bool = ...,
) -> _SageObject: ...
def Min(
    self,
    p: builtins.int,
    ubRes: builtins.object,
    conj: builtins.object,
    all_orbits: builtins.bool = ...,
) -> _SageObject: ...
def BM_all_minimal(
    self, return_transformation: builtins.bool = ..., D: builtins.object = ...
) -> _SageObject: ...
def HS_minimal(
    self, return_transformation: builtins.bool = ..., D: builtins.object = ...
) -> _SageObject: ...
def HS_all_minimal_p(
    self,
    f: builtins.object,
    m: builtins.int = ...,
    return_transformation: builtins.bool = ...,
) -> _SageObject: ...
def HS_all_minimal(
    self, return_transformation: builtins.bool = ..., D: builtins.object = ...
) -> _SageObject: ...
def get_bound_dynamical(
    self,
    f: builtins.object,
    m: builtins.int = ...,
    dynatomic: builtins.bool = ...,
    prec: builtins.int = ...,
    emb: builtins.object = ...,
) -> _SageObject: ...
def smallest_dynamical(
    self,
    dynatomic: builtins.bool = ...,
    start_n: builtins.int = ...,
    prec: builtins.int = ...,
    emb: builtins.object = ...,
    algorithm: builtins.str = ...,
    check_minimal: builtins.bool = ...,
) -> _SageObject: ...
