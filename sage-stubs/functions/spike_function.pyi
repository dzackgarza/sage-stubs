import builtins

class _SageObject: ...

class SpikeFunction:
    eps: builtins.float

    def __init__(self, v: builtins.object, eps: builtins.float = ...) -> None: ...
    def __call__(self, x: builtins.object) -> _SageObject: ...
    def plot_fft_abs(
        self,
        samples: builtins.object = ...,
        xmin: builtins.object = ...,
        xmax: builtins.object = ...,
        **kwds: builtins.object,
    ) -> _SageObject: ...
    def plot_fft_arg(
        self,
        samples: builtins.object = ...,
        xmin: builtins.object = ...,
        xmax: builtins.object = ...,
        **kwds: builtins.object,
    ) -> _SageObject: ...
    def vector(
        self,
        samples: builtins.object = ...,
        xmin: builtins.object = ...,
        xmax: builtins.object = ...,
    ) -> _SageObject: ...
    def plot(
        self,
        xmin: builtins.object = ...,
        xmax: builtins.object = ...,
        **kwds: builtins.object,
    ) -> _SageObject: ...

spike_function: _SageObject
