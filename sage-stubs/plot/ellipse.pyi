import builtins

class _SageObject: ...

class Ellipse:
    r2: float
    r1: float
    y: float
    x: float

    def __init__(
        self,
        x: builtins.object,
        y: builtins.object,
        r1: builtins.object,
        r2: builtins.object,
        angle: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...
    def plot3d(self) -> _SageObject: ...

def ellipse(
    self,
    r1: builtins.object,
    r2: builtins.object,
    angle: builtins.int = ...,
    **options: builtins.object,
) -> _SageObject: ...
