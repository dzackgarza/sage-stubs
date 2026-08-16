import builtins

class _SageObject: ...

class InlineFortran:
    verbose: bool

    def __init__(self, globals: builtins.object = ...) -> None: ...
    def __call__(
        self, *args: builtins.object, **kwds: builtins.object
    ) -> _SageObject: ...
    def eval(
        self,
        x: builtins.object,
        globals: builtins.object = ...,
        locals: builtins.object = ...,
    ) -> _SageObject: ...
    def add_library(self, s: builtins.object) -> _SageObject: ...
    def add_library_path(self, s: builtins.object) -> _SageObject: ...

fortran: _SageObject
