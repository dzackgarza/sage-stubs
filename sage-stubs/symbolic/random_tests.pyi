# Generated from the pinned Sage 10.7 source tree.
import builtins
from collections.abc import AsyncIterator as _AsyncIterator, Iterable as _Iterable, Iterator as _Iterator
from typing import Self

class _SageObject: ...

fast_binary: _SageObject
fast_unary: _SageObject
fast_nodes: _SageObject
full_binary: _SageObject
full_unary: _SageObject
full_functions: _SageObject
full_nullary: _SageObject
full_internal: _SageObject
def normalize_prob_list(pl: builtins.object, extra: builtins.tuple[_SageObject, ...] = ...) -> _SageObject: ...

def choose_from_prob_list(lst: builtins.object) -> _SageObject: ...

def random_integer_vector(n: builtins.int, length: builtins.int) -> _SageObject: ...

def random_expr_helper(n_nodes: builtins.object, internal: builtins.object, leaves: builtins.object, verbose: builtins.object) -> _SageObject: ...

def random_expr(size: builtins.int, nvars: builtins.int = ..., ncoeffs: builtins.object = ..., var_frac: builtins.float = ..., internal: builtins.object = ..., nullary: builtins.object = ..., nullary_frac: builtins.float = ..., coeff_generator: builtins.object = ..., verbose: builtins.bool = ...) -> _SageObject: ...

def assert_strict_weak_order(a: builtins.object, b: builtins.object, c: builtins.object, cmp_func: builtins.object) -> _SageObject: ...

def check_symbolic_expression_order(repetitions: builtins.int = ...) -> _SageObject: ...
