import builtins

class _SageObject: ...

sqrt: _SageObject

def padic_lseries(
    self,
    p: builtins.int,
    normalize: builtins.bool = ...,
    implementation: builtins.str = ...,
    precision: builtins.int = ...,
) -> _SageObject: ...
def padic_regulator(
    self,
    p: builtins.int,
    prec: builtins.int = ...,
    height: builtins.object = ...,
    check_hypotheses: builtins.bool = ...,
) -> _SageObject: ...
def padic_height_pairing_matrix(
    self,
    p: builtins.int,
    prec: builtins.int = ...,
    height: builtins.object = ...,
    check_hypotheses: builtins.bool = ...,
) -> _SageObject: ...
def padic_height(
    self,
    p: builtins.int,
    prec: builtins.int = ...,
    sigma: builtins.object = ...,
    check_hypotheses: builtins.bool = ...,
) -> _SageObject: ...
def padic_height_via_multiply(
    self,
    p: builtins.int,
    prec: builtins.int = ...,
    E2: builtins.object = ...,
    check_hypotheses: builtins.bool = ...,
) -> _SageObject: ...
def padic_sigma(
    self,
    p: builtins.int,
    N: builtins.int = ...,
    E2: builtins.object = ...,
    check: builtins.bool = ...,
    check_hypotheses: builtins.bool = ...,
) -> _SageObject: ...
def padic_sigma_truncated(
    self,
    p: builtins.int,
    N: builtins.int = ...,
    lamb: builtins.int = ...,
    E2: builtins.object = ...,
    check_hypotheses: builtins.bool = ...,
) -> _SageObject: ...
def padic_E2(
    self,
    p: builtins.int,
    prec: builtins.int = ...,
    check: builtins.bool = ...,
    check_hypotheses: builtins.bool = ...,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
def matrix_of_frobenius(
    self,
    p: builtins.int,
    prec: builtins.int = ...,
    check: builtins.bool = ...,
    check_hypotheses: builtins.bool = ...,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
