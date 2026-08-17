from collections.abc import Callable, Sequence
from os import PathLike

from sage.calculus.interpolation import Spline


type ODEState = Sequence[float]
type ODEParameters = Sequence[float]
type ODEFunction = (
    Callable[[float, ODEState], Sequence[float]]
    | Callable[[float, ODEState, ODEParameters], Sequence[float]]
)
type ODEJacobian = (
    Callable[[float, ODEState], Sequence[Sequence[float]]]
    | Callable[[float, ODEState, ODEParameters], Sequence[Sequence[float]]]
)
type ODESolutionPoint = tuple[float, list[float]]
type PlotOption = bool | int | float | str | tuple[float, float, float] | None


class ode_system:
    def __init__(self) -> None: ...


class ode_solver:
    function: ODEFunction | ode_system | None
    jacobian: ODEJacobian | None
    h: float
    error_abs: float
    error_rel: float
    a: float | bool
    a_dydt: float | bool
    scale_abs: Sequence[float] | bool
    algorithm: str
    y_0: list[float] | None
    t_span: list[float] | None
    params: list[float]
    solution: list[ODESolutionPoint]

    def __init__(
        self,
        function: ODEFunction | ode_system | None = None,
        jacobian: ODEJacobian | None = None,
        h: float = 1e-2,
        error_abs: float = 1e-10,
        error_rel: float = 1e-10,
        a: float | bool = False,
        a_dydt: float | bool = False,
        scale_abs: Sequence[float] | bool = False,
        algorithm: str = "rkf45",
        y_0: Sequence[float] | None = None,
        t_span: Sequence[float] | None = None,
        params: Sequence[float] | None = None,
    ) -> None: ...
    def __setattr__(self, name: str, value: object) -> None: ...
    def interpolate_solution(self, i: int = 0) -> Spline: ...
    def plot_solution(
        self,
        i: int = 0,
        filename: str | PathLike[str] | None = None,
        interpolate: bool = False,
        **kwds: PlotOption,
    ) -> None: ...
    def ode_solve(
        self,
        t_span: Sequence[float] | bool = False,
        y_0: Sequence[float] | bool = False,
        num_points: int | bool = False,
        params: Sequence[float] | None = None,
    ) -> None: ...
