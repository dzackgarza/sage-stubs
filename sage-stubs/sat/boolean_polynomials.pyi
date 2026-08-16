import builtins

class _SageObject: ...

def solve(
    self,
    converter: builtins.object = ...,
    solver: builtins.object = ...,
    n: builtins.int = ...,
    target_variables: builtins.object = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
def learn(
    self,
    converter: builtins.object = ...,
    solver: builtins.object = ...,
    max_learnt_length: builtins.int = ...,
    interreduction: builtins.bool = ...,
    **kwds: builtins.object,
) -> _SageObject: ...
