import builtins

class _SageObject: ...

class DegenerateManifold:
    def __init__(
        self,
        n: builtins.int,
        name: builtins.str,
        metric_name: builtins.str = ...,
        signature: builtins.object = ...,
        base_manifold: builtins.object = ...,
        diff_degree: builtins.object = ...,
        latex_name: builtins.str = ...,
        metric_latex_name: builtins.str = ...,
        start_index: builtins.int = ...,
        category: builtins.object = ...,
        unique_tag: builtins.object = ...,
    ) -> None: ...
    def metric(
        self,
        name: builtins.str = ...,
        signature: builtins.object = ...,
        latex_name: builtins.str = ...,
        dest_map: builtins.object = ...,
    ) -> DegenerateMetric: ...
    def open_subset(
        self,
        name: builtins.str,
        latex_name: builtins.str = ...,
        coord_def: builtins.dict[_SageObject, _SageObject] = ...,
    ) -> _SageObject: ...

class TangentTensor:
    def __init__(
        self,
        tensor: builtins.object,
        embedding: builtins.object,
        screen: builtins.object = ...,
    ) -> None: ...
    def __call__(self, *args: builtins.object) -> _SageObject: ...
    def extension(self) -> _SageObject: ...
