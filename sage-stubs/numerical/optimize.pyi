import builtins

class _SageObject: ...

def find_root(
    self,
    a: builtins.object,
    b: builtins.object,
    xtol: builtins.float = ...,
    rtol: builtins.object = ...,
    maxiter: builtins.int = ...,
    full_output: builtins.bool = ...,
) -> _SageObject: ...
def find_local_maximum(
    self,
    a: builtins.object,
    b: builtins.object,
    tol: builtins.float = ...,
    maxfun: builtins.int = ...,
) -> _SageObject: ...
def find_local_minimum(
    self,
    a: builtins.object,
    b: builtins.object,
    tol: builtins.float = ...,
    maxfun: builtins.int = ...,
) -> _SageObject: ...
def minimize(
    self,
    x0: builtins.object,
    gradient: builtins.object = ...,
    hessian: builtins.object = ...,
    algorithm: builtins.str = ...,
    verbose: builtins.bool = ...,
    **args: builtins.object,
) -> _SageObject: ...
def minimize_constrained(
    self,
    cons: builtins.object,
    x0: builtins.object,
    gradient: builtins.object = ...,
    algorithm: builtins.str = ...,
    **args: builtins.object,
) -> _SageObject: ...
def find_fit(
    self,
    model: builtins.object,
    initial_guess: builtins.object = ...,
    parameters: builtins.object = ...,
    variables: builtins.object = ...,
    solution_dict: builtins.bool = ...,
) -> _SageObject: ...
def binpacking(
    self,
    maximum: builtins.int = ...,
    k: builtins.int = ...,
    solver: builtins.object = ...,
    verbose: builtins.int = ...,
    *,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
