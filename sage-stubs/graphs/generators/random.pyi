import builtins

class _SageObject: ...

def RandomGNP(
    self,
    p: builtins.int,
    seed: builtins.object = ...,
    fast: builtins.bool = ...,
    algorithm: builtins.str = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomBarabasiAlbert(
    self, m: builtins.int, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomBipartite(
    self,
    n2: builtins.object,
    p: builtins.int,
    set_position: builtins.bool = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomRegularBipartite(
    self,
    n2: builtins.object,
    d1: builtins.object,
    set_position: builtins.bool = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomBlockGraph(
    self,
    k: builtins.int,
    kmax: builtins.object = ...,
    incidence_structure: builtins.bool = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomBoundedToleranceGraph(
    self, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomGNM(
    self,
    m: builtins.int,
    dense: builtins.bool = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomNewmanWattsStrogatz(
    self,
    k: builtins.int,
    p: builtins.int,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomHolmeKim(
    self,
    m: builtins.int,
    p: builtins.int,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomIntervalGraph(
    self, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomProperIntervalGraph(
    self, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def growing_subtrees(self, k: builtins.int) -> _SageObject: ...
def connecting_nodes(self, l: builtins.object) -> _SageObject: ...
def pruned_tree(self, f: builtins.object, s: builtins.object) -> _SageObject: ...
def RandomChordalGraph(
    self,
    algorithm: builtins.str = ...,
    k: builtins.int = ...,
    l: builtins.object = ...,
    f: builtins.object = ...,
    s: builtins.object = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomKTree(
    self, k: builtins.int, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomPartialKTree(
    self,
    k: builtins.int,
    x: builtins.object,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def RandomRegular(
    self, n: builtins.int, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomShell(
    self, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomToleranceGraph(
    self, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomTriangulation(
    self,
    set_position: builtins.bool = ...,
    k: builtins.int = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
def blossoming_contour(
    self, shift: builtins.int = ..., seed: builtins.object = ...
) -> _SageObject: ...
def RandomBicubicPlanar(
    self, seed: builtins.object = ..., immutable: builtins.bool = ...
) -> _SageObject: ...
def RandomUnitDiskGraph(
    self,
    radius: builtins.float = ...,
    side: builtins.int = ...,
    seed: builtins.object = ...,
    immutable: builtins.bool = ...,
) -> _SageObject: ...
