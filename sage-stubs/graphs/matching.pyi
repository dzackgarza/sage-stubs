import builtins

class _SageObject: ...

def has_perfect_matching(
    self,
    algorithm: builtins.str = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> builtins.bool: ...
def is_bicritical(
    self,
    matching: builtins.object = ...,
    algorithm: builtins.str = ...,
    coNP_certificate: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> builtins.bool: ...
def is_factor_critical(
    self,
    matching: builtins.object = ...,
    algorithm: builtins.str = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> builtins.bool: ...
def is_matching_covered(
    self,
    matching: builtins.object = ...,
    algorithm: builtins.str = ...,
    coNP_certificate: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> builtins.bool: ...
def matching(
    self,
    value_only: builtins.bool = ...,
    algorithm: builtins.str = ...,
    use_edge_labels: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
def perfect_matchings(self, labels: builtins.bool = ...) -> _SageObject: ...
def M_alternating_even_mark(
    self, vertex: builtins.object, matching: builtins.object
) -> _SageObject: ...
