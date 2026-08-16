import builtins

class _SageObject: ...

def fricas_desolve(
    self, dvar: builtins.object, ics: builtins.object, ivar: builtins.object
) -> _SageObject: ...
def fricas_desolve_system(
    self, dvars: builtins.object, ics: builtins.object, ivar: builtins.object
) -> _SageObject: ...
def desolve(
    self,
    dvar: builtins.object,
    ics: builtins.object = ...,
    ivar: builtins.object = ...,
    show_method: builtins.bool = ...,
    contrib_ode: builtins.bool = ...,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
def desolve_laplace(
    self, dvar: builtins.object, ics: builtins.object = ..., ivar: builtins.object = ...
) -> _SageObject: ...
def desolve_system(
    self,
    vars: builtins.object,
    ics: builtins.object = ...,
    ivar: builtins.object = ...,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
def eulers_method(
    self,
    x0: builtins.object,
    y0: builtins.object,
    h: builtins.object,
    x1: builtins.object,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
def eulers_method_2x2(
    self,
    g: builtins.object,
    t0: builtins.object,
    x0: builtins.object,
    y0: builtins.object,
    h: builtins.object,
    t1: builtins.object,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
def eulers_method_2x2_plot(
    self,
    g: builtins.object,
    t0: builtins.object,
    x0: builtins.object,
    y0: builtins.object,
    h: builtins.object,
    t1: builtins.object,
) -> _SageObject: ...
def desolve_rk4_determine_bounds(
    self, end_points: builtins.object = ...
) -> _SageObject: ...
def desolve_rk4(
    self,
    dvar: builtins.object,
    ics: builtins.object = ...,
    ivar: builtins.object = ...,
    end_points: builtins.object = ...,
    step: builtins.float = ...,
    output: builtins.str = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def desolve_system_rk4(
    self,
    vars: builtins.object,
    ics: builtins.object = ...,
    ivar: builtins.object = ...,
    end_points: builtins.object = ...,
    step: builtins.float = ...,
) -> _SageObject: ...
def desolve_odeint(
    self,
    ics: builtins.object,
    times: builtins.object,
    dvars: builtins.object,
    ivar: builtins.object = ...,
    compute_jac: builtins.bool = ...,
    args: builtins.tuple[_SageObject, ...] = ...,
    rtol: builtins.object = ...,
    atol: builtins.object = ...,
    tcrit: builtins.object = ...,
    h0: builtins.float = ...,
    hmax: builtins.float = ...,
    hmin: builtins.float = ...,
    ixpr: builtins.int = ...,
    mxstep: builtins.int = ...,
    mxhnil: builtins.int = ...,
    mxordn: builtins.int = ...,
    mxords: builtins.int = ...,
    printmessg: builtins.int = ...,
) -> _SageObject: ...
def desolve_mintides(
    self,
    ics: builtins.object,
    initial: builtins.object,
    final: builtins.object,
    delta: builtins.object,
    tolrel: builtins.float = ...,
    tolabs: builtins.float = ...,
) -> _SageObject: ...
def desolve_tides_mpfr(
    self,
    ics: builtins.object,
    initial: builtins.object,
    final: builtins.object,
    delta: builtins.object,
    tolrel: builtins.float = ...,
    tolabs: builtins.float = ...,
    digits: builtins.int = ...,
) -> _SageObject: ...
