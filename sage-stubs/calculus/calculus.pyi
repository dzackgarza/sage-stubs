import builtins

class _SageObject: ...

def symbolic_sum(
    self,
    v: builtins.object,
    a: builtins.object,
    b: builtins.object,
    algorithm: builtins.str = ...,
    hold: builtins.bool = ...,
) -> _SageObject: ...
def nintegral(
    self,
    x: builtins.object,
    a: builtins.object,
    b: builtins.object,
    desired_relative_error: builtins.str = ...,
    maximum_num_subintervals: builtins.int = ...,
) -> _SageObject: ...

nintegrate: _SageObject

def symbolic_product(
    self,
    v: builtins.object,
    a: builtins.object,
    b: builtins.object,
    algorithm: builtins.str = ...,
    hold: builtins.bool = ...,
) -> _SageObject: ...
def minpoly(
    self,
    var: builtins.str = ...,
    algorithm: builtins.str = ...,
    bits: builtins.object = ...,
    degree: builtins.int = ...,
    epsilon: builtins.int = ...,
) -> _SageObject: ...
def limit(
    self,
    *args: builtins.object,
    dir: builtins.object = ...,
    taylor: builtins.bool = ...,
    algorithm: builtins.str = ...,
    **kwargs: builtins.object,
) -> _SageObject: ...

lim: _SageObject

def mma_free_limit(
    self, v: builtins.object, a: builtins.object, dir: builtins.object = ...
) -> _SageObject: ...
def laplace(
    self, t: builtins.object, s: builtins.object, algorithm: builtins.str = ...
) -> _SageObject: ...
def inverse_laplace(
    self, s: builtins.object, t: builtins.object, algorithm: builtins.str = ...
) -> _SageObject: ...
def at(self, *args: builtins.object, **kwds: builtins.object) -> _SageObject: ...
def dummy_diff(self, *args: builtins.object) -> _SageObject: ...
def dummy_integrate(self, *args: builtins.object) -> _SageObject: ...
def dummy_laplace(self, *args: builtins.object) -> _SageObject: ...
def dummy_inverse_laplace(self, *args: builtins.object) -> _SageObject: ...
def dummy_pochhammer(self, *args: builtins.object) -> _SageObject: ...

symtable: _SageObject
maxima_qp: _SageObject
maxima_var: _SageObject
sci_not: _SageObject
polylog_ex: _SageObject
maxima_polygamma: _SageObject
maxima_hyper: _SageObject

def symbolic_expression_from_maxima_string(
    self, equals_sub: builtins.bool = ..., maxima: builtins.object = ...
) -> _SageObject: ...
def mapped_opts(self) -> _SageObject: ...
def maxima_options(self, **kwds: builtins.object) -> _SageObject: ...

syms_cur: _SageObject
syms_default: _SageObject
parser_make_var: _SageObject
parser_make_function: _SageObject
SR_parser: _SageObject

def symbolic_expression_from_string(
    self,
    syms: builtins.object = ...,
    accept_sequence: builtins.bool = ...,
    *,
    parser: builtins.object = ...,
) -> _SageObject: ...

parser_make_Mvar: _SageObject
SRM_parser: _SageObject
SR_parser_giac: _SageObject
