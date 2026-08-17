from collections.abc import Callable, Sequence
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

from sage.plot.graphics import Graphics


type BoundaryFunction = Callable[[float], complex]
type PlotRange = Sequence[float]
type RGBColor = Sequence[float]
type PlotOption = bool | int | float | str | RGBColor | None
type ComplexGrid = NDArray[np.complex128]
type RealGrid = NDArray[np.float64]
type RGBGrid = NDArray[np.float64]


FLOAT: type[np.float64]
COMPLEX: type[np.complex128]


class Riemann_Map:
    def __init__(
        self,
        fs: Sequence[BoundaryFunction],
        fprimes: Sequence[BoundaryFunction],
        a: complex,
        N: int = 500,
        ncorners: int = 4,
        opp: bool = False,
        exterior: bool = False,
    ) -> None: ...
    def _repr_(self) -> str: ...
    @overload
    def get_szego(
        self,
        boundary: int = -1,
        absolute_value: Literal[False] = False,
    ) -> list[list[float | complex]]: ...
    @overload
    def get_szego(
        self,
        boundary: int,
        absolute_value: Literal[True],
    ) -> list[list[float]]: ...
    def get_theta_points(self, boundary: int = -1) -> list[list[float]]: ...
    def riemann_map(self, pt: complex) -> complex: ...
    def inverse_riemann_map(self, pt: complex) -> complex: ...
    def plot_boundaries(
        self,
        plotjoined: bool = True,
        rgbcolor: RGBColor | None = None,
        thickness: float = 1,
    ) -> Graphics: ...
    def compute_on_grid(
        self,
        plot_range: PlotRange,
        x_points: int,
    ) -> tuple[ComplexGrid, float, float, float, float]: ...
    def plot_spiderweb(
        self,
        spokes: int = 16,
        circles: int = 4,
        pts: int = 32,
        linescale: float = 0.99,
        rgbcolor: RGBColor | None = None,
        thickness: float = 1,
        plotjoined: bool = True,
        withcolor: bool = False,
        plot_points: int = 200,
        min_mag: float = 0.001,
        **options: PlotOption,
    ) -> Graphics: ...
    def plot_colored(
        self,
        plot_range: PlotRange | None = None,
        plot_points: int = 100,
        **options: PlotOption,
    ) -> Graphics: ...


def get_derivatives(
    z_values: ComplexGrid,
    xstep: float,
    ystep: float,
) -> tuple[RealGrid, RealGrid]: ...
def complex_to_spiderweb(
    z_values: ComplexGrid,
    dr: RealGrid,
    dtheta: RealGrid,
    spokes: int,
    circles: int,
    rgbcolor: RGBColor,
    thickness: float,
    withcolor: bool,
    min_mag: float,
) -> RGBGrid: ...
def complex_to_rgb(z_values: ComplexGrid) -> RGBGrid: ...
def analytic_boundary(t: float, n: int, epsilon: float) -> float: ...
@overload
def cauchy_kernel(
    t: float,
    args: tuple[float, complex, int, Literal["c"]],
) -> complex: ...
@overload
def cauchy_kernel(
    t: float,
    args: tuple[float, complex, int, Literal["r", "i"]],
) -> float: ...
@overload
def cauchy_kernel(
    t: float,
    args: tuple[float, complex, int, str],
) -> complex | float | None: ...
def analytic_interior(z: complex, n: int, epsilon: float) -> complex: ...
