from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult, GinacFunction


class Function_exp(GinacFunction):
    def __init__(self) -> None: ...
class Function_log1(GinacFunction):
    def __init__(self) -> None: ...
class Function_log2(GinacFunction):
    def __init__(self) -> None: ...
class Function_polylog(GinacFunction):
    def __init__(self) -> None: ...
class Function_dilog(GinacFunction):
    def __init__(self) -> None: ...
class Function_lambert_w(BuiltinFunction):
    def __init__(self) -> None: ...
    def __call__(self, *args: FunctionArgument, **kwds: FunctionKeyword) -> FunctionResult: ...
class Function_exp_polar(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_harmonic_number_generalized(BuiltinFunction):
    def __init__(self) -> None: ...
    def __call__(
        self,
        z: FunctionArgument,
        m: FunctionArgument = 1,
        **kwds: FunctionKeyword,
    ) -> FunctionResult: ...
class Function_harmonic_number(BuiltinFunction):
    def __init__(self) -> None: ...


exp: Function_exp
ln: Function_log1
function_log: Function_log1
logb: Function_log2
polylog: Function_polylog
dilog: Function_dilog
lambert_w: Function_lambert_w
exp_polar: Function_exp_polar
harmonic_number: Function_harmonic_number_generalized
harmonic_m1: Function_harmonic_number
