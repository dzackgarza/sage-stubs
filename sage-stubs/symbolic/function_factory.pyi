from collections.abc import Callable

from sage.symbolic.function import ConversionTable, FunctionCallable, SymbolicFunction

type FunctionOption = int | str | bool | ConversionTable | FunctionCallable | None

def function_factory(
    self,
    nargs: int = 0,
    latex_name: str | None = None,
    conversions: ConversionTable | None = None,
    evalf_params_first: bool = True,
    eval_func: FunctionCallable | None = None,
    evalf_func: FunctionCallable | None = None,
    conjugate_func: FunctionCallable | None = None,
    real_part_func: FunctionCallable | None = None,
    imag_part_func: FunctionCallable | None = None,
    derivative_func: FunctionCallable | None = None,
    tderivative_func: FunctionCallable | None = None,
    power_func: FunctionCallable | None = None,
    series_func: FunctionCallable | None = None,
    print_func: Callable[..., str] | None = None,
    print_latex_func: Callable[..., str] | None = None,
) -> SymbolicFunction: ...
def unpickle_function(
    self,
    nargs: int,
    latex_name: str | None,
    conversions: ConversionTable | None,
    evalf_params_first: bool,
    pickled_funcs: list[bytes | None],
) -> SymbolicFunction: ...
def function(
    self, **kwds: FunctionOption
) -> SymbolicFunction | list[SymbolicFunction]: ...
