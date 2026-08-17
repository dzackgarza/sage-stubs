from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult, GinacFunction


class Function_gamma(GinacFunction):
    def __init__(self) -> None: ...
class Function_log_gamma(GinacFunction):
    def __init__(self) -> None: ...
class Function_gamma_inc(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_gamma_inc_lower(BuiltinFunction):
    def __init__(self) -> None: ...


gamma1: Function_gamma
log_gamma: Function_log_gamma
gamma_inc: Function_gamma_inc
gamma_inc_lower: Function_gamma_inc_lower


def gamma(a: FunctionArgument, *args: FunctionArgument, **kwds: FunctionKeyword) -> FunctionResult: ...


class Function_psi1(GinacFunction):
    def __init__(self) -> None: ...
class Function_psi2(GinacFunction):
    def __init__(self) -> None: ...


psi1: Function_psi1
psi2: Function_psi2

def psi(x: FunctionArgument, *args: FunctionArgument, **kwds: FunctionKeyword) -> FunctionResult: ...


class Function_beta(GinacFunction):
    def __init__(self) -> None: ...


beta: Function_beta
