import builtins

class _SageObject: ...

class Arc:
    s2: float
    s1: float
    angle: float
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
        s1: builtins.object,
        s2: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...
    def bezier_path(self) -> _SageObject: ...
    def plot3d(self) -> _SageObject: ...

def arc(
    self,
    r1: builtins.object,
    r2: builtins.object = ...,
    angle: builtins.float = ...,
    sector: builtins.tuple[_SageObject, ...] = ...,
    **options: builtins.object,
) -> _SageObject: ...
