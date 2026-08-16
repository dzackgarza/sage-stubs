import builtins

class _SageObject: ...

def is_dominating(
    self, dom: builtins.object, focus: builtins.object = ...
) -> builtins.bool: ...
def is_redundant(
    self, dom: builtins.object, focus: builtins.object = ...
) -> builtins.bool: ...
def private_neighbors(
    self, vertex: builtins.object, dom: builtins.object
) -> _SageObject: ...
def dominating_sets(
    self,
    k: builtins.int = ...,
    independent: builtins.bool = ...,
    total: builtins.bool = ...,
    connected: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
def dominating_set(
    self,
    k: builtins.int = ...,
    independent: builtins.bool = ...,
    total: builtins.bool = ...,
    connected: builtins.bool = ...,
    value_only: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
def minimal_dominating_sets(
    self,
    to_dominate: builtins.object = ...,
    work_on_copy: builtins.bool = ...,
    k: builtins.int = ...,
) -> _SageObject: ...
def greedy_dominating_set(
    self,
    k: builtins.int = ...,
    vertices: builtins.object = ...,
    ordering: builtins.object = ...,
    return_sets: builtins.bool = ...,
    closest: builtins.bool = ...,
) -> _SageObject: ...
def maximum_leaf_number(
    self,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
