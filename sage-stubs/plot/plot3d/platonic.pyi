import builtins

class _SageObject: ...

def index_face_set(
    self,
    point_list: builtins.object,
    enclosed: builtins.object,
    **kwds: builtins.object,
) -> _SageObject: ...
def prep(
    self, center: builtins.object, size: builtins.int, kwds: builtins.object
) -> _SageObject: ...
def tetrahedron(
    self=..., size: builtins.int = ..., **kwds: builtins.object
) -> _SageObject: ...
def cube(
    self=...,
    size: builtins.int = ...,
    color: builtins.object = ...,
    frame_thickness: builtins.int = ...,
    frame_color: builtins.object = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def octahedron(
    self=..., size: builtins.int = ..., **kwds: builtins.object
) -> _SageObject: ...
def dodecahedron(
    self=..., size: builtins.int = ..., **kwds: builtins.object
) -> _SageObject: ...
def icosahedron(
    self=..., size: builtins.int = ..., **kwds: builtins.object
) -> _SageObject: ...
