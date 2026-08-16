import builtins

class _SageObject: ...

class Disk:
    rad2: float
    rad1: float
    r: float
    y: float
    x: float

    def __init__(
        self,
        point: builtins.object,
        r: builtins.int,
        angle: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...
    def plot3d(self, z: builtins.int = ..., **kwds: builtins.object) -> _SageObject: ...

def disk(
    self, radius: builtins.object, angle: builtins.object, **options: builtins.object
) -> _SageObject: ...
