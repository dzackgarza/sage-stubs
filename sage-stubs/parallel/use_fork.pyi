import builtins

class _SageObject: ...

class WorkerData:
    failure: builtins.str

    def __init__(
        self,
        input_value: builtins.object,
        starttime: builtins.object = ...,
        failure: builtins.str = ...,
    ) -> None: ...

class p_iter_fork:
    worker_seed: None
    reseed_rng: builtins.bool
    reset_interfaces: builtins.bool
    verbose: builtins.bool
    timeout: float
    ncpus: int

    def __init__(
        self,
        ncpus: builtins.object,
        timeout: builtins.int = ...,
        verbose: builtins.bool = ...,
        reset_interfaces: builtins.bool = ...,
        reseed_rng: builtins.bool = ...,
    ) -> None: ...
    def __call__(self, f: builtins.object, inputs: builtins.object) -> _SageObject: ...
