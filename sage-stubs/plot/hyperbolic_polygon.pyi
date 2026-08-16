import builtins

class _SageObject: ...

class HyperbolicPolygon:
    def __init__(
        self, pts: builtins.object, model: builtins.object, options: builtins.object
    ) -> None: ...

def hyperbolic_polygon(
    self,
    model: builtins.str = ...,
    resolution: builtins.int = ...,
    **options: builtins.object,
) -> _SageObject: ...
def hyperbolic_triangle(
    self,
    b: builtins.object,
    c: builtins.object,
    model: builtins.str = ...,
    **options: builtins.object,
) -> _SageObject: ...
