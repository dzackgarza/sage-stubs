import builtins

from sage.rings.cc import CC

class _SageObject: ...
class HyperbolicArcCore: ...

class HyperbolicArc:
    B: CC
    A: CC

    def __init__(
        self,
        A: builtins.object,
        B: builtins.object,
        model: builtins.object,
        options: builtins.object,
    ) -> None: ...

def hyperbolic_arc(
    self, b: builtins.object, model: builtins.str = ..., **options: builtins.object
) -> _SageObject: ...
