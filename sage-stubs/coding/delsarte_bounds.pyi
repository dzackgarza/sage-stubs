import builtins

class _SageObject: ...

def krawtchouk(
    self,
    q: builtins.int,
    l: builtins.object,
    x: builtins.object,
    check: builtins.bool = ...,
) -> _SageObject: ...
def eberlein(
    self,
    w: builtins.object,
    k: builtins.int,
    u: builtins.object,
    check: builtins.bool = ...,
) -> _SageObject: ...
def delsarte_bound_constant_weight_code(
    self,
    d: builtins.object,
    w: builtins.object,
    return_data: builtins.bool = ...,
    solver: builtins.str = ...,
    isinteger: builtins.bool = ...,
) -> _SageObject: ...
def delsarte_bound_hamming_space(
    self,
    d: builtins.object,
    q: builtins.int,
    return_data: builtins.bool = ...,
    solver: builtins.str = ...,
    isinteger: builtins.bool = ...,
) -> _SageObject: ...
def delsarte_bound_additive_hamming_space(
    self,
    d: builtins.object,
    q: builtins.int,
    d_star: builtins.int = ...,
    q_base: builtins.int = ...,
    return_data: builtins.bool = ...,
    solver: builtins.str = ...,
    isinteger: builtins.bool = ...,
) -> _SageObject: ...
def delsarte_bound_Q_matrix(
    self,
    d: builtins.object,
    return_data: builtins.bool = ...,
    solver: builtins.str = ...,
    isinteger: builtins.bool = ...,
) -> _SageObject: ...
