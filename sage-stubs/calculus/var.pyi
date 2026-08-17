from collections.abc import Callable, Sequence

from sage.symbolic.expression import Expression, SymbolicDomain
from sage.symbolic.function import FunctionCallable, SymbolicFunction


type VariableName = str | Sequence[str]
type VariableKeyword = str | SymbolicDomain | None
type SymbolicFunctionKeyword = (
    int
    | str
    | bool
    | dict[str, str]
    | FunctionCallable
    | Callable[..., str]
    | None
)


def var(
    *args: VariableName | Expression,
    **kwds: VariableKeyword,
) -> Expression | tuple[Expression, ...]: ...
def function(
    s: VariableName,
    **kwds: SymbolicFunctionKeyword,
) -> SymbolicFunction | tuple[SymbolicFunction, ...]: ...
def clear_vars() -> None: ...
