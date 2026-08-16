import builtins

class _SageObject: ...

class KnownKeywords:
    frobenius_algebra: _SageObject
    root: _SageObject
    equivariant: _SageObject
    reduced: _SageObject
    code: _SageObject

def check_kwds(self, **kwds: builtins.object) -> _SageObject: ...
def khoca_interface(self, **kwds: builtins.object) -> _SageObject: ...
def khoca_raw_data(
    self, ring: builtins.object, red_typ: builtins.bool = ..., **kwds: builtins.object
) -> _SageObject: ...

Khoca: _SageObject
