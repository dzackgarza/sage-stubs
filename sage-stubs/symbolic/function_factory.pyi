from collections.abc import Callable
from sage.symbolic.function import (
    ConversionTable,
    SymbolicCallable,
    SymbolicFunction,
    SymbolicValue,
)

type FunctionOption = (
    int | str | bool | ConversionTable | SymbolicCallable | None
)

def function_factory(
    name: str,
    nargs: int = 0,
    latex_name: str | None = None,
    conversions: ConversionTable | None = None,
    evalf_params_first: bool = True,
    eval_func: SymbolicCallable | None = None,
    evalf_func: SymbolicCallable | None = None,
    conjugate_func: SymbolicCallable | None = None,
    real_part_func: SymbolicCallable | None = None,
    imag_part_func: SymbolicCallable | None = None,
    derivative_func: SymbolicCallable | None = None,
    tderivative_func: SymbolicCallable | None = None,
    power_func: SymbolicCallable | None = None,
    series_func: SymbolicCallable | None = None,
    print_func: Callable[..., str] | None = None,
    print_latex_func: Callable[..., str] | None = None,
) -> SymbolicFunction: ...

def unpickle_function(
    name: str,
    nargs: int,
    latex_name: str | None,
    conversions: ConversionTable | None,
    evalf_params_first: bool,
    pickled_funcs: list[bytes | None],
) -> SymbolicFunction: ...

def function(
    s: str, **kwds: FunctionOption
) -> SymbolicFunction | list[SymbolicFunction]: ...
