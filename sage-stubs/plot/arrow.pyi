import builtins

class _SageObject: ...

class CurveArrow:
    def __init__(self, path: builtins.object, options: builtins.object) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...

class Arrow:
    yhead: float
    ytail: float
    xhead: float
    xtail: float

    def __init__(
        self,
        xtail: builtins.object,
        ytail: builtins.object,
        xhead: builtins.object,
        yhead: builtins.object,
        options: builtins.object,
    ) -> None: ...
    def get_minmax_data(self) -> _SageObject: ...
    def plot3d(
        self,
        ztail: builtins.int = ...,
        zhead: builtins.int = ...,
        **kwds: builtins.object,
    ) -> _SageObject: ...

def arrow(
    self=..., headpoint: builtins.object = ..., **kwds: builtins.object
) -> _SageObject: ...
def arrow2d(
    self=...,
    headpoint: builtins.object = ...,
    path: builtins.object = ...,
    **options: builtins.object,
) -> _SageObject: ...
