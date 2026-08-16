import builtins

from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing

class _SageObject: ...

def integral_elements_in_box(self, C: builtins.object) -> _SageObject: ...

eps_global: _SageObject

class tr_data_rel:
    Fx: PolynomialRing
    m: builtins.int

    def __init__(
        self,
        F: builtins.object,
        m: builtins.int,
        B: builtins.object,
        a: builtins.object = ...,
    ) -> None: ...
    def incr(
        self,
        f_out: builtins.object,
        verbose: builtins.bool = ...,
        haltk: builtins.int = ...,
    ) -> _SageObject: ...

def enumerate_totallyreal_fields_rel(
    self,
    m: builtins.int,
    B: builtins.object,
    a: builtins.list[_SageObject] = ...,
    verbose: builtins.int = ...,
    return_seqs: builtins.bool = ...,
    return_pari_objects: builtins.bool = ...,
) -> _SageObject: ...
def enumerate_totallyreal_fields_all(
    self,
    B: builtins.object,
    verbose: builtins.int = ...,
    return_seqs: builtins.bool = ...,
    return_pari_objects: builtins.bool = ...,
) -> _SageObject: ...
