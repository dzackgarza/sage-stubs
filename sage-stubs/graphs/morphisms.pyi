import builtins

class _SageObject: ...

def reduced_homeomorphic_graph(
    self,
    allow_multiple_edges: builtins.bool = ...,
    allow_loops: builtins.bool = ...,
    return_steps: builtins.bool = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def is_homeomorphic(self, H: builtins.object) -> builtins.bool: ...
def has_homomorphism_to(
    self,
    H: builtins.object,
    core: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> builtins.bool: ...
