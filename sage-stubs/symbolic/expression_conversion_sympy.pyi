from typing import Protocol

from sympy.core.basic import Basic
from sympy.core.function import Lambda

from sage.symbolic.expression import Expression, SymbolicOperator
from sage.symbolic.expression_conversions import (
    Converter,
    SymbolicDerivativeOperator,
    SymbolicPyObject,
    SymbolicRelationOperator,
)


type SympyExpression = Basic
type SympyPyObject = Basic | int | float | complex | bool | str


class SympyFunctionOperator(SymbolicOperator, Protocol):
    def _sympy_(self, *args: Expression) -> SympyExpression: ...
    def _sympy_init_(self) -> str: ...


class SympyConverter(Converter[SympyExpression | Lambda]):
    def __init__(self) -> None: ...
    def __call__(
        self,
        ex: Expression | None = None,
    ) -> SympyExpression | Lambda: ...
    def pyobject(
        self,
        ex: Expression,
        obj: SymbolicPyObject,
    ) -> SympyExpression | SympyPyObject: ...
    def arithmetic(
        self,
        ex: Expression,
        operator: SymbolicOperator,
    ) -> SympyExpression: ...
    def symbol(self, ex: Expression) -> SympyExpression: ...
    def relation(
        self,
        ex: Expression,
        op: SymbolicRelationOperator,
    ) -> SympyExpression: ...
    def composition(
        self,
        ex: Expression,
        operator: SympyFunctionOperator,
    ) -> SympyExpression: ...
    def tuple(self, ex: Expression) -> tuple[Expression, ...]: ...
    def derivative(
        self,
        ex: Expression,
        operator: SymbolicDerivativeOperator,
    ) -> SympyExpression: ...


sympy_converter: SympyConverter
