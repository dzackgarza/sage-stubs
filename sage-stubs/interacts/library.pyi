from collections.abc import Callable

from sage.symbolic.expression import Expression

def library_interact(
    decorator_target: Callable[..., object] | None = ..., **widgets: Callable[..., object]
) -> Callable[..., object]: ...

def html(obj: str) -> None: ...

def demo(n: int, m: int) -> None: ...

def taylor_polynomial(title: str, f: Expression, order: int) -> None: ...

def definite_integral(
    title: str,
    f: Expression,
    g: Expression,
    interval: list[float],
    x_range: list[float],
    selection: list[str],
) -> None: ...

def function_derivative(
    title: str, function: Expression, x_range: list[float], y_range: list[float]
) -> None: ...

def difference_quotient(
    title: str, f: Expression, interval: list[float], a: float, x0: float
) -> None: ...

def quadratic_equation(A: float, B: float, C: float) -> None: ...

def trigonometric_properties_triangle(
    a0: tuple[float, float], a1: tuple[float, float], a2: tuple[float, float]
) -> None: ...

def unit_circle(function: Expression, x: float) -> None: ...

def special_points(
    title: str,
    a0: tuple[float, float],
    a1: tuple[float, float],
    a2: tuple[float, float],
    show_median: bool,
    show_pb: bool,
    show_alt: bool,
    show_ab: bool,
    show_incircle: bool,
    show_euler: bool,
) -> None: ...

def coin(n: int, interval: list[float]) -> None: ...

def bisection_method(
    title: str, f: Expression, interval: list[float], d: float, maxn: int
) -> None: ...

def secant_method(
    title: str, f: Expression, interval: list[float], d: float, maxn: int
) -> None: ...

def newton_method(
    title: str,
    f: Expression,
    c: float,
    d: float,
    maxn: int,
    interval: list[float],
    list_steps: bool,
) -> None: ...

def trapezoid_integration(
    title: str,
    f: Expression,
    n: int,
    interval_input: list[float],
    interval_s: list[float],
    interval_g: list[float],
    output_form: str,
) -> None: ...

def simpson_integration(
    title: str,
    f: Expression,
    n: int,
    interval_input: list[float],
    interval_s: list[float],
    interval_g: list[float],
    output_form: str,
) -> Expression: ...

def riemann_sum(
    title: str,
    f: Expression,
    n: int,
    hr1: float,
    interval_input: list[float],
    interval_s: list[float],
    interval_g: list[float],
    hr2: float,
    list_table: bool,
    auto_update: bool = ...,
) -> None: ...

def function_tool(
    f: Expression,
    g: Expression,
    xrange: list[float],
    yrange: list[float],
    a: float,
    action: list[str],
    do_plot: bool,
) -> None: ...

def julia(
    expo: int,
    c_real: float,
    c_imag: float,
    iterations: int,
    zoom_x: list[float],
    zoom_y: list[float],
    plot_points: int,
    dpi: int,
) -> None: ...

def mandelbrot(
    expo: int,
    iterations: int,
    zoom_x: list[float],
    zoom_y: list[float],
    plot_points: int,
    dpi: int,
) -> None: ...

def cellular_automaton(N: int, rule_number: int, size: int) -> None: ...

def polar_prime_spiral(
    interval: list[float],
    show_factors: bool,
    highlight_primes: bool,
    show_curves: bool,
    n: int,
    dpi: int,
) -> None: ...
