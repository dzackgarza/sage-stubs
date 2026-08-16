import builtins

class _SageObject: ...

uniq_c: _SageObject

def parse_color(self, base: builtins.object = ...) -> _SageObject: ...

class Texture:
    specular: builtins.int
    diffuse: builtins.int
    ambient: builtins.float
    shininess: float
    opacity: float
    name: builtins.str

    @staticmethod
    def __classcall__(
        cls: builtins.object, id: builtins.object = ..., **kwds: builtins.object
    ) -> _SageObject: ...
    def __init__(
        self,
        id: builtins.object,
        color: builtins.tuple[_SageObject, ...] = ...,
        opacity: builtins.int = ...,
        ambient: builtins.float = ...,
        diffuse: builtins.int = ...,
        specular: builtins.int = ...,
        shininess: builtins.int = ...,
        name: builtins.str = ...,
        **kwds: builtins.object,
    ) -> None: ...
    def hex_rgb(self) -> str: ...
    def tachyon_str(self) -> str: ...
    def x3d_str(self) -> str: ...
    def mtl_str(self) -> str: ...
    def jmol_str(self, obj: builtins.object) -> str: ...
