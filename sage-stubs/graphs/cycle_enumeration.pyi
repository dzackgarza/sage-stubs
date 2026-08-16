import builtins

class _SageObject: ...

def all_cycles_iterator(
    self,
    starting_vertices: builtins.object = ...,
    simple: builtins.bool = ...,
    rooted: builtins.bool = ...,
    max_length: builtins.object = ...,
    trivial: builtins.bool = ...,
    weight_function: builtins.object = ...,
    by_weight: builtins.bool = ...,
    check_weight: builtins.bool = ...,
    report_weight: builtins.bool = ...,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
def all_simple_cycles(
    self,
    starting_vertices: builtins.object = ...,
    rooted: builtins.bool = ...,
    max_length: builtins.object = ...,
    trivial: builtins.bool = ...,
    weight_function: builtins.object = ...,
    by_weight: builtins.bool = ...,
    check_weight: builtins.bool = ...,
    report_weight: builtins.bool = ...,
    algorithm: builtins.str = ...,
) -> _SageObject: ...
