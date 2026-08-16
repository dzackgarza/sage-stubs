import builtins

class _SageObject: ...

python_min: _SageObject
python_max: _SageObject

def gauss_sum(
    self,
    p: builtins.int,
    f: builtins.object,
    prec: builtins.int = ...,
    factored: builtins.bool = ...,
    algorithm: builtins.str = ...,
    parent: builtins.object = ...,
) -> _SageObject: ...
def min(self, *L: builtins.object) -> _SageObject: ...
def max(self, *L: builtins.object) -> _SageObject: ...
def precprint(self, prec_cap: builtins.object, p: builtins.int) -> _SageObject: ...
def trim_zeros(self) -> _SageObject: ...
