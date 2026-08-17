from collections.abc import Callable, Sequence

from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult


class MinMax_base(BuiltinFunction):
    def eval_helper(
        self,
        this_f: Callable[..., FunctionResult],
        builtin_f: Callable[[Sequence[FunctionArgument]], FunctionArgument],
        initial_val: FunctionArgument,
        args: Sequence[FunctionArgument],
    ) -> FunctionResult: ...
    def __call__(
        self,
        *args: FunctionArgument,
        **kwds: FunctionKeyword,
    ) -> FunctionResult: ...


class MaxSymbolic(MinMax_base):
    def __init__(self) -> None: ...
class MinSymbolic(MinMax_base):
    def __init__(self) -> None: ...


max_symbolic: MaxSymbolic
min_symbolic: MinSymbolic
