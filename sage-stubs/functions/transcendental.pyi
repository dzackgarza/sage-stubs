import builtins

class _SageObject: ...

class Function_zeta:
    def __init__(self) -> None: ...

zeta: _SageObject

class Function_stieltjes:
    def __init__(self) -> None: ...

stieltjes: _SageObject

class Function_HurwitzZeta:
    def __init__(self) -> None: ...

hurwitz_zeta_func: _SageObject

def hurwitz_zeta(
    self, x: builtins.object, **kwargs: builtins.object
) -> _SageObject: ...

class Function_zetaderiv:
    def __init__(self) -> None: ...

zetaderiv: _SageObject

def zeta_symmetric(self) -> _SageObject: ...

class DickmanRho:
    def __init__(self) -> None: ...
    def power_series(
        self, n: builtins.int, abs_prec: builtins.object
    ) -> _SageObject: ...
    def approximate(
        self, x: builtins.object, parent: builtins.object = ...
    ) -> _SageObject: ...

dickman_rho: _SageObject
