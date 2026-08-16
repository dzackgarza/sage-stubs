import builtins

class _SageObject: ...

x: _SageObject

def library_interact(self=..., **widgets: builtins.object) -> _SageObject: ...
def html(self) -> _SageObject: ...
def demo(self, m: builtins.int) -> _SageObject: ...
def taylor_polynomial(self, f: builtins.object, order: builtins.int) -> _SageObject: ...
def definite_integral(
    self,
    f: builtins.object,
    g: builtins.object,
    interval: builtins.object,
    x_range: builtins.object,
    selection: builtins.object,
) -> _SageObject: ...
def function_derivative(
    self, function: builtins.object, x_range: builtins.object, y_range: builtins.object
) -> _SageObject: ...
def difference_quotient(
    self,
    f: builtins.object,
    interval: builtins.object,
    a: builtins.object,
    x0: builtins.object,
) -> _SageObject: ...
def quadratic_equation(self, B: builtins.object, C: builtins.object) -> _SageObject: ...
def trigonometric_properties_triangle(
    self, a1: builtins.object, a2: builtins.object
) -> _SageObject: ...
def unit_circle(self, x: builtins.object) -> _SageObject: ...
def special_points(
    self,
    a0: builtins.object,
    a1: builtins.object,
    a2: builtins.object,
    show_median: builtins.object,
    show_pb: builtins.object,
    show_alt: builtins.object,
    show_ab: builtins.object,
    show_incircle: builtins.object,
    show_euler: builtins.object,
) -> _SageObject: ...
def coin(self, interval: builtins.object) -> _SageObject: ...
def bisection_method(
    self,
    f: builtins.object,
    interval: builtins.object,
    d: builtins.object,
    maxn: builtins.object,
) -> _SageObject: ...
def secant_method(
    self,
    f: builtins.object,
    interval: builtins.object,
    d: builtins.object,
    maxn: builtins.object,
) -> _SageObject: ...
def newton_method(
    self,
    f: builtins.object,
    c: builtins.object,
    d: builtins.object,
    maxn: builtins.object,
    interval: builtins.object,
    list_steps: builtins.object,
) -> _SageObject: ...
def trapezoid_integration(
    self,
    f: builtins.object,
    n: builtins.int,
    interval_input: builtins.object,
    interval_s: builtins.object,
    interval_g: builtins.object,
    output_form: builtins.object,
) -> _SageObject: ...
def simpson_integration(
    self,
    f: builtins.object,
    n: builtins.int,
    interval_input: builtins.object,
    interval_s: builtins.object,
    interval_g: builtins.object,
    output_form: builtins.object,
) -> _SageObject: ...
def riemann_sum(
    self,
    f: builtins.object,
    n: builtins.int,
    hr1: builtins.object,
    interval_input: builtins.object,
    interval_s: builtins.object,
    interval_g: builtins.object,
    hr2: builtins.object,
    list_table: builtins.object,
    auto_update: builtins.bool = ...,
) -> _SageObject: ...
def function_tool(
    self,
    g: builtins.object,
    xrange: builtins.object,
    yrange: builtins.object,
    a: builtins.object,
    action: builtins.object,
    do_plot: builtins.object,
) -> _SageObject: ...
def julia(
    self,
    c_real: builtins.object,
    c_imag: builtins.object,
    iterations: builtins.object,
    zoom_x: builtins.object,
    zoom_y: builtins.object,
    plot_points: builtins.object,
    dpi: builtins.object,
) -> _SageObject: ...
def mandelbrot(
    self,
    iterations: builtins.object,
    zoom_x: builtins.object,
    zoom_y: builtins.object,
    plot_points: builtins.object,
    dpi: builtins.object,
) -> _SageObject: ...
def cellular_automaton(
    self, rule_number: builtins.object, size: builtins.int
) -> _SageObject: ...
def polar_prime_spiral(
    self,
    show_factors: builtins.object,
    highlight_primes: builtins.object,
    show_curves: builtins.object,
    n: builtins.int,
    dpi: builtins.object,
) -> _SageObject: ...
