import builtins

class _SageObject: ...

fast_binary: _SageObject
fast_unary: _SageObject
fast_nodes: _SageObject
full_binary: _SageObject
full_unary: _SageObject
full_functions: _SageObject
full_nullary: _SageObject
full_internal: _SageObject

def normalize_prob_list(
    self, extra: builtins.tuple[_SageObject, ...] = ...
) -> _SageObject: ...
def choose_from_prob_list(self) -> _SageObject: ...
def random_integer_vector(self, length: builtins.int) -> _SageObject: ...
def random_expr_helper(
    self, internal: builtins.object, leaves: builtins.object, verbose: builtins.object
) -> _SageObject: ...
def random_expr(
    self,
    nvars: builtins.int = ...,
    ncoeffs: builtins.object = ...,
    var_frac: builtins.float = ...,
    internal: builtins.object = ...,
    nullary: builtins.object = ...,
    nullary_frac: builtins.float = ...,
    coeff_generator: builtins.object = ...,
    verbose: builtins.bool = ...,
) -> _SageObject: ...
def assert_strict_weak_order(
    self, b: builtins.object, c: builtins.object, cmp_func: builtins.object
) -> _SageObject: ...
def check_symbolic_expression_order(self=...) -> _SageObject: ...
