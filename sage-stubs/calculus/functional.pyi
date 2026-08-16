import builtins

class _SageObject: ...

def simplify(
    self, algorithm: builtins.str = ..., **kwds: builtins.object
) -> _SageObject: ...
def derivative(
    self, *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...

diff: _SageObject

def integral(self, *args: builtins.object, **kwds: builtins.object) -> _SageObject: ...

integrate: _SageObject

def limit(
    self,
    dir: builtins.object = ...,
    taylor: builtins.bool = ...,
    **argv: builtins.object,
) -> _SageObject: ...

lim: _SageObject

def taylor(self, *args: builtins.object) -> _SageObject: ...
def expand(self, *args: builtins.object, **kwds: builtins.object) -> _SageObject: ...
