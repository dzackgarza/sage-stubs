import builtins

class _SageObject: ...

class DatabaseCremona:
    def __init__(
        self,
        name: builtins.str = ...,
        spkg: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...

class DatabaseEllcurves:
    def __init__(self) -> None: ...

class DatabaseGraphs:
    def __init__(self) -> None: ...

class DatabaseJones:
    def __init__(self) -> None: ...

class DatabaseKnotInfo:
    def __init__(self) -> None: ...

class DatabaseMatroids:
    def __init__(self) -> None: ...

class DatabaseCubicHecke:
    def __init__(self) -> None: ...

class DatabaseReflexivePolytopes:
    def __init__(self, name: builtins.str = ...) -> None: ...

def all_features(self) -> _SageObject: ...
