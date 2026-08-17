from collections.abc import Callable, Sequence
from typing import overload

from sage.structure.element import Matrix, Vector
from sage.symbolic.expression import Expression, SymbolicInput


type SymbolicScalarFactory = Callable[..., SymbolicInput]
type SymbolicExpressionInput = (
    SymbolicInput
    | Sequence[SymbolicInput]
    | Matrix
    | Vector
    | SymbolicScalarFactory
)


@overload
def symbolic_expression(x: Matrix) -> Matrix: ...
@overload
def symbolic_expression(x: Vector | Sequence[SymbolicInput]) -> Vector: ...
@overload
def symbolic_expression(x: SymbolicScalarFactory) -> Expression | Vector: ...
@overload
def symbolic_expression(x: SymbolicInput) -> Expression: ...
