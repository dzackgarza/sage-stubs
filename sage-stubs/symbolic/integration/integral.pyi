from collections.abc import Callable
from typing import Literal

from sage.symbolic.expression import Expression, SymbolicInput
from sage.symbolic.function import BuiltinFunction


type IntegrationAlgorithm = Literal["maxima", "sympy", "mathematica_free", "fricas", "giac", "libgiac"] | str
type IntegrationBound = SymbolicInput | None
type Integrator = Callable[[Expression, Expression, IntegrationBound, IntegrationBound], Expression]


available_integrators: dict[IntegrationAlgorithm, Integrator]


class IndefiniteIntegral(BuiltinFunction):
    def __init__(self) -> None: ...


indefinite_integral: IndefiniteIntegral


class DefiniteIntegral(BuiltinFunction):
    def __init__(self) -> None: ...


definite_integral: DefiniteIntegral


def integrate(
    expression: SymbolicInput,
    v: Expression | None = None,
    a: IntegrationBound = None,
    b: IntegrationBound = None,
    algorithm: IntegrationAlgorithm | None = None,
    hold: bool = False,
) -> Expression: ...


integral: DefiniteIntegral | IndefiniteIntegral
