import builtins

from sage.manifolds.continuous_map import ContinuousMap
from sage.manifolds.manifold import TopologicalManifold

class _SageObject: ...

class TopologicalSubmanifold:
    def __init__(
        self,
        n: builtins.int,
        name: builtins.str,
        field: builtins.object,
        structure: builtins.object,
        ambient: builtins.object = ...,
        base_manifold: builtins.object = ...,
        latex_name: builtins.str = ...,
        start_index: builtins.int = ...,
        category: builtins.object = ...,
        unique_tag: builtins.object = ...,
    ) -> None: ...
    def open_subset(
        self,
        name: builtins.str,
        latex_name: builtins.str = ...,
        coord_def: builtins.dict[_SageObject, _SageObject] = ...,
        supersets: builtins.object = ...,
    ) -> _SageObject: ...
    def set_immersion(
        self,
        phi: builtins.object,
        inverse: builtins.object = ...,
        var: builtins.object = ...,
        t_inverse: builtins.object = ...,
    ) -> _SageObject: ...
    def declare_embedding(self) -> _SageObject: ...
    def set_embedding(
        self,
        phi: builtins.object,
        inverse: builtins.object = ...,
        var: builtins.object = ...,
        t_inverse: builtins.object = ...,
    ) -> _SageObject: ...
    def adapted_chart(
        self, postscript: builtins.object = ..., latex_postscript: builtins.object = ...
    ) -> _SageObject: ...
    def plot(
        self,
        param: builtins.object,
        u: builtins.object,
        v: builtins.object,
        chart1: builtins.object = ...,
        chart2: builtins.object = ...,
        **kwargs: builtins.object,
    ) -> _SageObject: ...
    def ambient(self) -> TopologicalManifold: ...
    def immersion(self) -> ContinuousMap: ...
    def embedding(self) -> ContinuousMap: ...
    def as_subset(self) -> _SageObject: ...
