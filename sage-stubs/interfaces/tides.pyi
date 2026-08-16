import builtins

class _SageObject: ...

def subexpressions_list(self, pars: builtins.object = ...) -> _SageObject: ...
def remove_repeated(self, l2: builtins.object) -> _SageObject: ...
def remove_constants(self, l2: builtins.object) -> _SageObject: ...
def genfiles_mintides(
    self,
    driver: builtins.object,
    f: builtins.object,
    ics: builtins.object,
    initial: builtins.object,
    final: builtins.object,
    delta: builtins.object,
    tolrel: builtins.float = ...,
    tolabs: builtins.float = ...,
    output: builtins.str = ...,
) -> _SageObject: ...
def genfiles_mpfr(
    self,
    driver: builtins.object,
    f: builtins.object,
    ics: builtins.object,
    initial: builtins.object,
    final: builtins.object,
    delta: builtins.object,
    parameters: builtins.object = ...,
    parameter_values: builtins.object = ...,
    dig: builtins.int = ...,
    tolrel: builtins.float = ...,
    tolabs: builtins.float = ...,
    output: builtins.str = ...,
) -> _SageObject: ...
