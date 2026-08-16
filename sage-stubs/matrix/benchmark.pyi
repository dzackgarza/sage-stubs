import builtins

class _SageObject: ...

verbose: _SageObject
timeout: _SageObject

def report(
    self,
    title: builtins.object,
    systems: builtins.list[_SageObject] = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def report_ZZ(self, **kwds: builtins.object) -> _SageObject: ...
def nullspace_ZZ(
    self=...,
    min: builtins.int = ...,
    max: builtins.object = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def charpoly_ZZ(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def rank_ZZ(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def rank2_ZZ(
    self=...,
    min: builtins.int = ...,
    max: builtins.object = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def smithform_ZZ(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def matrix_multiply_ZZ(
    self=...,
    min: builtins.object = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def matrix_add_ZZ(
    self=...,
    min: builtins.object = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def matrix_add_ZZ_2(
    self=...,
    bits: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def det_ZZ(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def det_QQ(
    self=...,
    num_bound: builtins.int = ...,
    den_bound: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def vecmat_ZZ(
    self=...,
    min: builtins.object = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def report_GF(self=..., **kwds: builtins.object) -> _SageObject: ...
def nullspace_GF(
    self=..., p: builtins.int = ..., system: builtins.str = ...
) -> _SageObject: ...
def charpoly_GF(
    self=..., p: builtins.int = ..., system: builtins.str = ...
) -> _SageObject: ...
def matrix_add_GF(
    self=...,
    p: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def matrix_multiply_GF(
    self=...,
    p: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def rank_GF(
    self=..., p: builtins.int = ..., system: builtins.str = ...
) -> _SageObject: ...
def rank2_GF(
    self=..., p: builtins.int = ..., system: builtins.str = ...
) -> _SageObject: ...
def det_GF(
    self=..., p: builtins.int = ..., system: builtins.str = ...
) -> _SageObject: ...
def hilbert_matrix(self) -> _SageObject: ...
def echelon_QQ(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def inverse_QQ(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def matrix_multiply_QQ(
    self=...,
    bnd: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def det_hilbert_QQ(self=..., system: builtins.str = ...) -> _SageObject: ...
def invert_hilbert_QQ(self=..., system: builtins.str = ...) -> _SageObject: ...
def MatrixVector_QQ(
    self=...,
    h: builtins.int = ...,
    system: builtins.str = ...,
    times: builtins.int = ...,
) -> _SageObject: ...
def nullspace_RR(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
def nullspace_RDF(
    self=...,
    min: builtins.int = ...,
    max: builtins.int = ...,
    system: builtins.str = ...,
) -> _SageObject: ...
