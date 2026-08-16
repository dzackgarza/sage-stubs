import builtins

class _SageObject: ...

class Maxima:
    def __init__(
        self,
        script_subdirectory: builtins.object = ...,
        logfile: builtins.object = ...,
        server: builtins.object = ...,
        init_code: builtins.object = ...,
    ) -> None: ...
    def set_seed(self, seed: builtins.object = ...) -> _SageObject: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...
    def lisp(self, cmd: builtins.object) -> _SageObject: ...
    def set(self, var: builtins.object, value: builtins.object) -> _SageObject: ...
    def clear(self, var: builtins.object) -> _SageObject: ...
    def get(self, var: builtins.object) -> _SageObject: ...

class MaximaElement:
    def __init__(
        self,
        parent: builtins.object,
        value: builtins.object,
        is_name: builtins.bool = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def display2d(self, onscreen: builtins.bool = ...) -> _SageObject: ...

MaximaFunctionElement: _SageObject
MaximaFunction: _SageObject

class MaximaElementFunction:
    def __init__(
        self,
        parent: builtins.object,
        name: builtins.str,
        defn: builtins.object,
        args: builtins.object,
        latex: builtins.object,
    ) -> None: ...

maxima: _SageObject

def reduce_load_Maxima(self) -> _SageObject: ...
def reduce_load_Maxima_function(
    self, defn: builtins.object, args: builtins.object, latex: builtins.object
) -> _SageObject: ...
