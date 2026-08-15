from typing import Protocol

from sage.manifolds.manifold import TopologicalManifold
from sage.manifolds.subset import ManifoldSubset
from sage.structure.sage_object import SageObject

class _PullbackMap(Protocol):
    def domain(self) -> TopologicalManifold: ...

class _PullbackSubset(Protocol):
    def __contains__(self, point: SageObject) -> bool: ...

class ManifoldSubsetPullback(ManifoldSubset):
    def __init__(
        self,
        map: _PullbackMap,
        codomain_subset: _PullbackSubset,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def is_open(self) -> bool: ...
