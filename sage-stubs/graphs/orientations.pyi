import builtins

class _SageObject: ...

def orient(
    self,
    f: builtins.object,
    weighted: builtins.object = ...,
    data_structure: builtins.object = ...,
    sparse: builtins.bool = ...,
    immutable: builtins.bool = ...,
    hash_labels: builtins.object = ...,
) -> _SageObject: ...
def orientations(
    self, data_structure: builtins.object = ..., sparse: builtins.bool = ...
) -> _SageObject: ...
def acyclic_orientations(self) -> _SageObject: ...
def strong_orientation(self) -> _SageObject: ...
def strong_orientations_iterator(self) -> _SageObject: ...
def random_orientation(self) -> _SageObject: ...
def minimum_outdegree_orientation(
    self,
    use_edge_labels: builtins.bool = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
def bounded_outdegree_orientation(
    self,
    bound: builtins.object,
    solver: builtins.object = ...,
    verbose: builtins.bool = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
def eulerian_orientation(self) -> _SageObject: ...
