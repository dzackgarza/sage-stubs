import builtins

class _SageObject: ...

class ProjectiveConic_number_field:
    def __init__(self, A: builtins.object, f: builtins.object) -> None: ...
    def has_rational_point(
        self,
        point: builtins.bool = ...,
        obstruction: builtins.bool = ...,
        algorithm: builtins.str = ...,
        read_cache: builtins.bool = ...,
    ) -> builtins.bool: ...
    def is_locally_solvable(self, p: builtins.int) -> bool: ...
    def local_obstructions(
        self,
        finite: builtins.bool = ...,
        infinite: builtins.bool = ...,
        read_cache: builtins.bool = ...,
    ) -> _SageObject: ...
