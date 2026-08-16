import builtins

from sage.modules.free_module import FreeModule
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.rings.integer import Integer

class _SageObject: ...

class UniformSampler:
    upper_bound: Integer
    lower_bound: Integer

    def __init__(
        self, lower_bound: builtins.object, upper_bound: builtins.object
    ) -> None: ...
    def __call__(self) -> _SageObject: ...

class UniformPolynomialSampler:
    D: UniformSampler
    upper_bound: Integer
    lower_bound: Integer
    P: builtins.int
    n: Integer

    def __init__(
        self,
        P: builtins.int,
        n: builtins.int,
        lower_bound: builtins.object,
        upper_bound: builtins.object,
    ) -> None: ...
    def __call__(self) -> _SageObject: ...

class LWE:
    secret_dist: builtins.str
    FM: FreeModule
    K: IntegerModRing
    m: builtins.int
    n: Integer

    def __init__(
        self,
        n: builtins.int,
        q: builtins.int,
        D: builtins.object,
        secret_dist: builtins.str = ...,
        m: builtins.int = ...,
    ) -> None: ...
    def __call__(self) -> _SageObject: ...

class Regev:
    def __init__(
        self, n: builtins.int, secret_dist: builtins.str = ..., m: builtins.int = ...
    ) -> None: ...

class LindnerPeikert:
    def __init__(
        self, n: builtins.int, delta: builtins.float = ..., m: builtins.int = ...
    ) -> None: ...

class UniformNoiseLWE:
    def __init__(
        self, n: builtins.int, instance: builtins.str = ..., m: builtins.int = ...
    ) -> None: ...

class RingLWE:
    secret_dist: builtins.str
    q: builtins.int
    K: IntegerModRing
    m: builtins.int
    N: Integer

    def __init__(
        self,
        N: builtins.int,
        q: builtins.int,
        D: builtins.object,
        poly: builtins.object = ...,
        secret_dist: builtins.str = ...,
        m: builtins.int = ...,
    ) -> None: ...
    def __call__(self) -> _SageObject: ...

class RingLindnerPeikert:
    def __init__(
        self, N: builtins.int, delta: builtins.float = ..., m: builtins.int = ...
    ) -> None: ...

class RingLWEConverter:
    def __init__(self, ringlwe: builtins.object) -> None: ...
    def __call__(self) -> _SageObject: ...

def samples(
    self,
    n: builtins.int,
    lwe: builtins.object,
    seed: builtins.object = ...,
    balanced: builtins.bool = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def balance_sample(self, q: builtins.int = ...) -> _SageObject: ...
