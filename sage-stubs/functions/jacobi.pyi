import builtins

class _SageObject: ...

HALF: _SageObject

class Jacobi:
    def __init__(self, kind: builtins.object) -> None: ...

jacobi_nd: _SageObject
jacobi_ns: _SageObject
jacobi_nc: _SageObject
jacobi_dn: _SageObject
jacobi_ds: _SageObject
jacobi_dc: _SageObject
jacobi_sn: _SageObject
jacobi_sd: _SageObject
jacobi_sc: _SageObject
jacobi_cn: _SageObject
jacobi_cd: _SageObject
jacobi_cs: _SageObject

class InverseJacobi:
    def __init__(self, kind: builtins.object) -> None: ...

inverse_jacobi_nd: _SageObject
inverse_jacobi_ns: _SageObject
inverse_jacobi_nc: _SageObject
inverse_jacobi_dn: _SageObject
inverse_jacobi_ds: _SageObject
inverse_jacobi_dc: _SageObject
inverse_jacobi_sn: _SageObject
inverse_jacobi_sd: _SageObject
inverse_jacobi_sc: _SageObject
inverse_jacobi_cn: _SageObject
inverse_jacobi_cd: _SageObject
inverse_jacobi_cs: _SageObject

def jacobi(
    self, z: builtins.object, m: builtins.int, **kwargs: builtins.object
) -> _SageObject: ...
def inverse_jacobi(
    self, x: builtins.object, m: builtins.int, **kwargs: builtins.object
) -> _SageObject: ...

class JacobiAmplitude:
    def __init__(self) -> None: ...

jacobi_am: _SageObject

def inverse_jacobi_f(self, x: builtins.object, m: builtins.int) -> _SageObject: ...
def jacobi_am_f(self, m: builtins.int) -> _SageObject: ...
