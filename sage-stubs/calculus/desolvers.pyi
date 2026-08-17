from collections.abc import Callable, Sequence
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.rings.real_mpfr import RealNumber
from sage.symbolic.expression import Expression, SymbolicInput


type ODEEquation = Expression
type ODEVariable = Expression
type ODESystem = Sequence[ODEEquation]
type ODEVariables = Sequence[ODEVariable]
type InitialConditions = Sequence[SymbolicInput]
type Numeric = int | float | Integer | RealNumber
type EulerScalar = Numeric | Expression
type EulerPoint = list[EulerScalar]
type ScalarODEFunction = Callable[[EulerScalar, EulerScalar], EulerScalar]
type SystemODEFunction = Callable[[EulerScalar, EulerScalar, EulerScalar], EulerScalar]
type VectorODEFunction = Callable[[Sequence[EulerScalar]], EulerScalar]
type ODECallable = Callable[..., EulerScalar | Sequence[EulerScalar]]
type ODEInput = ODEEquation | ODESystem | ODECallable
type RKPoint = list[float]
type TidesPoint = list[RealNumber]


def fricas_desolve(
    de: ODEEquation,
    dvar: ODEVariable,
    ics: InitialConditions | None,
    ivar: ODEVariable,
) -> Expression: ...
def fricas_desolve_system(
    des: ODESystem,
    dvars: ODEVariables,
    ics: InitialConditions | None,
    ivar: ODEVariable,
) -> list[Expression]: ...
@overload
def desolve(
    de: ODEEquation,
    dvar: ODEVariable,
    ics: InitialConditions | None = None,
    ivar: ODEVariable | None = None,
    show_method: Literal[False] = False,
    contrib_ode: bool = False,
    algorithm: str = "maxima",
) -> Expression: ...
@overload
def desolve(
    de: ODEEquation,
    dvar: ODEVariable,
    ics: InitialConditions | None,
    ivar: ODEVariable | None,
    show_method: Literal[True],
    contrib_ode: bool = False,
    algorithm: str = "maxima",
) -> list[Expression | str]: ...
def desolve_laplace(
    de: ODEEquation,
    dvar: ODEVariable,
    ics: InitialConditions | None = None,
    ivar: ODEVariable | None = None,
) -> Expression: ...
def desolve_system(
    des: ODESystem,
    vars: ODEVariables,
    ics: InitialConditions | None = None,
    ivar: ODEVariable | None = None,
    algorithm: str = "maxima",
) -> list[Expression]: ...
@overload
def eulers_method(
    f: ScalarODEFunction,
    x0: EulerScalar,
    y0: EulerScalar,
    h: EulerScalar,
    x1: EulerScalar,
    algorithm: Literal["table"] = "table",
) -> None: ...
@overload
def eulers_method(
    f: ScalarODEFunction,
    x0: EulerScalar,
    y0: EulerScalar,
    h: EulerScalar,
    x1: EulerScalar,
    algorithm: str,
) -> list[EulerPoint]: ...
@overload
def eulers_method_2x2(
    f: SystemODEFunction,
    g: SystemODEFunction,
    t0: EulerScalar,
    x0: EulerScalar,
    y0: EulerScalar,
    h: EulerScalar,
    t1: EulerScalar,
    algorithm: Literal["table"] = "table",
) -> None: ...
@overload
def eulers_method_2x2(
    f: SystemODEFunction,
    g: SystemODEFunction,
    t0: EulerScalar,
    x0: EulerScalar,
    y0: EulerScalar,
    h: EulerScalar,
    t1: EulerScalar,
    algorithm: str,
) -> list[EulerPoint]: ...
def eulers_method_2x2_plot(
    f: VectorODEFunction,
    g: VectorODEFunction,
    t0: EulerScalar,
    x0: EulerScalar,
    y0: EulerScalar,
    h: EulerScalar,
    t1: EulerScalar,
) -> list[Graphics]: ...
def desolve_rk4_determine_bounds(
    ics: Sequence[float],
    end_points: Sequence[float] | None = None,
) -> tuple[float, float]: ...
@overload
def desolve_rk4(
    de: ODEInput,
    dvar: ODEVariable,
    ics: Sequence[float] | None = None,
    ivar: ODEVariable | None = None,
    end_points: Sequence[float] | None = None,
    step: float = 0.1,
    output: Literal["list"] = "list",
    **kwds: SymbolicInput,
) -> list[RKPoint]: ...
@overload
def desolve_rk4(
    de: ODEInput,
    dvar: ODEVariable,
    ics: Sequence[float] | None,
    ivar: ODEVariable | None,
    end_points: Sequence[float] | None,
    step: float,
    output: Literal["plot", "slope_field"],
    **kwds: SymbolicInput,
) -> Graphics: ...
def desolve_system_rk4(
    des: ODESystem,
    vars: ODEVariables,
    ics: Sequence[float] | None = None,
    ivar: ODEVariable | None = None,
    end_points: Sequence[float] | None = None,
    step: float = 0.1,
) -> list[RKPoint]: ...
def desolve_odeint(
    des: ODEInput,
    ics: Sequence[float],
    times: Sequence[float],
    dvars: ODEVariable | ODEVariables,
    ivar: ODEVariable | None = None,
    compute_jac: bool = False,
    args: tuple[Numeric, ...] = (),
    rtol: float | None = None,
    atol: float | None = None,
    tcrit: Sequence[float] | None = None,
    h0: float = 0.0,
    hmax: float = 0.0,
    hmin: float = 0.0,
    ixpr: int = 0,
    mxstep: int = 0,
    mxhnil: int = 0,
    mxordn: int = 12,
    mxords: int = 5,
    printmessg: int = 0,
) -> NDArray[np.float64]: ...
def desolve_mintides(
    f: ODECallable | Expression,
    ics: InitialConditions,
    initial: SymbolicInput,
    final: SymbolicInput,
    delta: SymbolicInput,
    tolrel: float = 1e-16,
    tolabs: float = 1e-16,
) -> list[TidesPoint]: ...
def desolve_tides_mpfr(
    f: ODECallable | Expression,
    ics: InitialConditions,
    initial: SymbolicInput,
    final: SymbolicInput,
    delta: SymbolicInput,
    tolrel: float = 1e-16,
    tolabs: float = 1e-16,
    digits: int = 50,
) -> list[TidesPoint]: ...
