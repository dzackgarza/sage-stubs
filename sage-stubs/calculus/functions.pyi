from sage.matrix.matrix0 import Matrix
from sage.structure.element import Element
from sage.symbolic.expression import Expression


type CalculusFunction = Expression | Element


def wronskian(*args: CalculusFunction) -> CalculusFunction: ...
def jacobian(
    functions: CalculusFunction | tuple[CalculusFunction, ...] | list[CalculusFunction],
    variables: Expression | tuple[Expression, ...] | list[Expression],
) -> Matrix: ...
