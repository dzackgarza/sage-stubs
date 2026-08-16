import builtins

class _SageObject: ...

class LoggingBackend:
    def __init__(
        self,
        backend: builtins.object,
        printing: builtins.bool = ...,
        doctest: builtins.object = ...,
        test_method: builtins.object = ...,
        base_ring: builtins.object = ...,
    ) -> None: ...
    def __getattr__(self, attr: builtins.object) -> _SageObject: ...
    def base_ring(self) -> _SageObject: ...

test_method_template: _SageObject

def LoggingBackendFactory(
    self=...,
    printing: builtins.bool = ...,
    doctest_file: builtins.object = ...,
    test_method_file: builtins.object = ...,
    test_method: builtins.object = ...,
    base_ring: builtins.object = ...,
) -> _SageObject: ...
