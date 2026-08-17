from collections.abc import Callable
from typing import TypeVar

from sage.symbolic.expression import Expression, SymbolicInput
from sage.symbolic.function import Function


_Operand = TypeVar("_Operand")
type ExpressionCallable = Function | Callable[..., Expression]


def add_vararg(first: _Operand, *rest: _Operand) -> _Operand: ...
def mul_vararg(first: _Operand, *rest: _Operand) -> _Operand: ...


arithmetic_operators: dict[Callable[..., SymbolicInput], str]
relation_operators: dict[Callable[[SymbolicInput, SymbolicInput], bool], str]


class FDerivativeOperator:
    def __init__(
        self,
        function: ExpressionCallable,
        parameter_set: tuple[int, ...] | list[int],
    ) -> None: ...
    def __call__(self, *args: SymbolicInput) -> Expression: ...
    def __repr__(self) -> str: ...
    def function(self) -> ExpressionCallable: ...
    def change_function(self, new: ExpressionCallable) -> FDerivativeOperator: ...
    def parameter_set(self) -> list[int]: ...


class DerivativeOperator:
    class DerivativeOperatorWithParameters:
        def __init__(self, parameter_set: tuple[int, ...] | list[int]) -> None: ...
        def __call__(self, function: ExpressionCallable) -> FDerivativeOperator: ...

    def __getitem__(
        self,
        args: int | tuple[int, ...],
    ) -> DerivativeOperatorWithParameters: ...


D: DerivativeOperator
