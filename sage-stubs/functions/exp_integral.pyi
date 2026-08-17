from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionResult

class Function_exp_integral_e(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_exp_integral_e1(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_log_integral(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_log_integral_offset(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_sin_integral(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_cos_integral(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_sinh_integral(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_cosh_integral(BuiltinFunction):
    def __init__(self) -> None: ...

class Function_exp_integral(BuiltinFunction):
    def __init__(self) -> None: ...

exp_integral_e: Function_exp_integral_e
exp_integral_e1: Function_exp_integral_e1
li: Function_log_integral
log_integral: Function_log_integral
Li: Function_log_integral_offset
log_integral_offset: Function_log_integral_offset
Si: Function_sin_integral
sin_integral: Function_sin_integral
Ci: Function_cos_integral
cos_integral: Function_cos_integral
Shi: Function_sinh_integral
sinh_integral: Function_sinh_integral
Chi: Function_cosh_integral
cosh_integral: Function_cosh_integral
Ei: Function_exp_integral
exp_integral_ei: Function_exp_integral

def exponential_integral_1(
    x: FunctionArgument,
    n: int = 0,
) -> FunctionResult | list[FunctionResult]: ...
