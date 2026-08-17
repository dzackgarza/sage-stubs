from collections.abc import Callable, Sequence
from typing import Literal

from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.symbolic.expression import Expression, SymbolicInput


type RealBound = int | float | SymbolicInput | PlusInfinity | MinusInfinity
type Integrand = Expression | Callable[..., float] | int | float
type IntegrationParameters = Sequence[SymbolicInput]
type QuadratureAlgorithm = Literal["qag", "qags", "qng"]
type MonteCarloAlgorithm = Literal["plain", "miser", "vegas"]


def numerical_integral(
    func: Integrand,
    a: RealBound | Sequence[RealBound],
    b: RealBound | None = None,
    algorithm: QuadratureAlgorithm = "qag",
    max_points: int = 87,
    params: IntegrationParameters | None = None,
    eps_abs: float = 1e-6,
    eps_rel: float = 1e-6,
    rule: int = 6,
) -> tuple[float, float]: ...
def monte_carlo_integral(
    func: Integrand,
    xl: Sequence[float],
    xu: Sequence[float],
    calls: int,
    algorithm: MonteCarloAlgorithm = "plain",
    params: IntegrationParameters | None = None,
) -> tuple[float, float]: ...
