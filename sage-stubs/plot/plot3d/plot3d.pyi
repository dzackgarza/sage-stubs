import builtins

class _SageObject: ...

class Spherical:
    def transform(
        self,
        radius: builtins.object = ...,
        azimuth: builtins.object = ...,
        inclination: builtins.object = ...,
    ) -> _SageObject: ...

class SphericalElevation:
    def transform(
        self,
        radius: builtins.object = ...,
        azimuth: builtins.object = ...,
        elevation: builtins.object = ...,
    ) -> _SageObject: ...

class Cylindrical:
    def transform(
        self,
        radius: builtins.object = ...,
        azimuth: builtins.object = ...,
        height: builtins.object = ...,
    ) -> _SageObject: ...

class TrivialTriangleFactory:
    def triangle(
        self,
        a: builtins.object,
        b: builtins.object,
        c: builtins.object,
        color: builtins.object = ...,
    ) -> _SageObject: ...
    def smooth_triangle(
        self,
        a: builtins.object,
        b: builtins.object,
        c: builtins.object,
        da: builtins.object,
        db: builtins.object,
        dc: builtins.object,
        color: builtins.object = ...,
    ) -> _SageObject: ...

def plot3d(
    self,
    urange: builtins.object,
    vrange: builtins.object,
    adaptive: builtins.bool = ...,
    transformation: builtins.object = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def plot3d_adaptive(
    self,
    x_range: builtins.object,
    y_range: builtins.object,
    color: builtins.str = ...,
    grad_f: builtins.object = ...,
    max_bend: builtins.float = ...,
    max_depth: builtins.int = ...,
    initial_depth: builtins.int = ...,
    num_colors: builtins.int = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def spherical_plot3d(
    self, urange: builtins.object, vrange: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def cylindrical_plot3d(
    self, urange: builtins.object, vrange: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def axes(
    self=..., radius: builtins.object = ..., **kwds: builtins.object
) -> _SageObject: ...
