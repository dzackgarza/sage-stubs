import builtins

from sage.structure.element import Element

class _SageObject: ...

class BSD_data:
    N_factorization: None
    primes: None
    gens: None
    rank: None
    N: None
    sha_an: None
    Sha: None
    two_tor_rk: None
    curve: None

    def __init__(self) -> None: ...
    def update(self) -> None: ...

def mwrank_two_descent_work(
    self, two_tor_rk: builtins.object
) -> tuple[Element, ...]: ...
def pari_two_descent_work(self) -> tuple[Element, ...]: ...
def native_two_isogeny_descent_work(
    self, two_tor_rk: builtins.object
) -> tuple[Element, ...]: ...
def heegner_index_work(self) -> tuple[Element, ...]: ...
def prove_BSD(
    self,
    verbosity: builtins.int = ...,
    two_desc: builtins.str = ...,
    proof: builtins.bool = ...,
    secs_hi: builtins.int = ...,
    return_BSD: builtins.bool = ...,
) -> _SageObject: ...
