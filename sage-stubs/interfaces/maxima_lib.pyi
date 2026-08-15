# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

init_code: _SageObject
maxima_eval: _SageObject
maxima_lib_instances: _SageObject
maxprint: _SageObject
meval: _SageObject
msetq: _SageObject
mlist: _SageObject
mequal: _SageObject
cadadr: _SageObject
max_integrate: _SageObject
max_sum: _SageObject
max_simplify_sum: _SageObject
max_prod: _SageObject
max_simplify_prod: _SageObject
max_ratsimp: _SageObject
max_limit: _SageObject
max_tlimit: _SageObject
max_plus: _SageObject
max_minus: _SageObject
max_use_grobner: _SageObject
max_to_poly_solve: _SageObject
max_at: _SageObject
def stdout_to_string(s: builtins.object) -> _SageObject: ...

def max_to_string(s: builtins.object) -> _SageObject: ...

my_mread: _SageObject
def parse_max_string(s: builtins.object) -> _SageObject: ...

class MaximaLib:
    def __init__(self) -> None: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...
    eval: _SageObject
    def lisp(self, cmd: builtins.object) -> _SageObject: ...
    def set(self, var: builtins.object, value: builtins.object) -> _SageObject: ...
    def clear(self, var: builtins.object) -> _SageObject: ...
    def get(self, var: builtins.object) -> _SageObject: ...
    def sr_integral(self, *args: builtins.object) -> _SageObject: ...
    def sr_sum(self, *args: builtins.object) -> _SageObject: ...
    def sr_prod(self, *args: builtins.object) -> _SageObject: ...
    def sr_limit(self, expr: builtins.object, v: builtins.object, a: builtins.object, dir: builtins.object = ...) -> _SageObject: ...
    def sr_tlimit(self, expr: builtins.object, v: builtins.object, a: builtins.object, dir: builtins.object = ...) -> _SageObject: ...

class MaximaLibElement:
    def ecl(self) -> _SageObject: ...
    def to_poly_solve(self, vars: builtins.object, options: builtins.str = ...) -> _SageObject: ...
    def display2d(self, onscreen: builtins.bool = ...) -> _SageObject: ...

MaximaLibFunctionElement: _SageObject
MaximaLibFunction: _SageObject
class MaximaLibElementFunction:
    ...

maxima_lib: _SageObject
maxima: _SageObject
def reduce_load_MaximaLib() -> _SageObject: ...

car: _SageObject
cdr: _SageObject
caar: _SageObject
cadr: _SageObject
cddr: _SageObject
caddr: _SageObject
caaadr: _SageObject
NIL: _SageObject
lisp_length: _SageObject
sage_op_dict: _SageObject
max_op_dict: _SageObject
def sage_rat(x: builtins.object, y: builtins.object) -> _SageObject: ...

mplus: _SageObject
mtimes: _SageObject
rat: _SageObject
ratdisrep: _SageObject
mrat: _SageObject
mqapply: _SageObject
max_li: _SageObject
max_psi: _SageObject
max_hyper: _SageObject
max_array: _SageObject
mdiff: _SageObject
max_lambert_w: _SageObject
max_harmo: _SageObject
max_pochhammer: _SageObject
def mrat_to_sage(expr: builtins.object) -> _SageObject: ...

def mqapply_to_sage(expr: builtins.object) -> _SageObject: ...

def mdiff_to_sage(expr: builtins.object) -> _SageObject: ...

def mlist_to_sage(expr: builtins.object) -> _SageObject: ...

def max_at_to_sage(expr: builtins.object) -> _SageObject: ...

def dummy_integrate(expr: builtins.object) -> _SageObject: ...

def max_harmonic_to_sage(expr: builtins.object) -> _SageObject: ...

def max_pochhammer_to_sage(expr: builtins.object) -> _SageObject: ...

special_max_to_sage: _SageObject
special_sage_to_max: _SageObject
sage_sym_dict: _SageObject
max_sym_dict: _SageObject
max_i: _SageObject
def pyobject_to_max(obj: builtins.object) -> _SageObject: ...

def sr_to_max(expr: builtins.object) -> _SageObject: ...

max_to_pynac_table: _SageObject
def max_to_sr(expr: builtins.object) -> _SageObject: ...

max_equal: _SageObject
max_notequal: _SageObject
max_is: _SageObject
test_max_equal: _SageObject
test_max_notequal: _SageObject
test_max_relation: _SageObject
