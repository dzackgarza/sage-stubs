import builtins

class _SageObject: ...

class Circle:
    r: float
    y: float
    x: float

    def __init__(
        self,
        x: builtins.object,
        y: builtins.object,
        r: builtins.int,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...
    def plot3d(self, z: builtins.int = ..., **kwds: builtins.object) -> _SageObject: ...

def circle(
    self, radius: builtins.object, **options: builtins.object
) -> _SageObject: ...
