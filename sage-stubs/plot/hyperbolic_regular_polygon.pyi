import builtins

from sage.rings.cc import CC

class _SageObject: ...

class HyperbolicRegularPolygon:
    center: CC

    def __init__(
        self,
        sides: builtins.object,
        i_angle: builtins.object,
        center: builtins.object,
        options: builtins.object,
    ) -> None: ...

def hyperbolic_regular_polygon(
    self,
    i_angle: builtins.object,
    center: builtins.object = ...,
    **options: builtins.object,
) -> _SageObject: ...
