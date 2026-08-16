import builtins

from sage.repl.rich_output.buffer import OutputBuffer

class _SageObject: ...

class OutputSceneJmol:
    preview_png: OutputBuffer
    scene_zip: OutputBuffer

    def __init__(
        self, scene_zip: builtins.object, preview_png: builtins.object
    ) -> None: ...
    def launch_script_filename(self) -> _SageObject: ...
    @classmethod
    def example(cls) -> _SageObject: ...

class OutputSceneCanvas3d:
    canvas3d: OutputBuffer

    def __init__(self, canvas3d: builtins.object) -> None: ...
    @classmethod
    def example(cls) -> _SageObject: ...

class OutputSceneThreejs:
    html: OutputBuffer

    def __init__(self, html: builtins.object) -> None: ...

class OutputSceneWavefront:
    mtl: OutputBuffer
    obj: OutputBuffer

    def __init__(self, obj: builtins.object, mtl: builtins.object) -> None: ...
    def mtllib(self) -> _SageObject: ...
    def obj_filename(self) -> _SageObject: ...
    @classmethod
    def example(cls) -> _SageObject: ...
