import builtins

class _SageObject: ...

class MarkedOutput:
    random: _SageObject
    rel_tol: _SageObject
    abs_tol: _SageObject
    tol: _SageObject

    def update(self, **kwds: builtins.object) -> _SageObject: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...

def make_marked_output(self, D: builtins.object) -> _SageObject: ...
