import builtins

class _SageObject: ...

class VirtualCrystal:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        ambient: builtins.object,
        virtualization: builtins.object,
        scaling_factors: builtins.object,
        contained: builtins.object = ...,
        generators: builtins.object = ...,
        cartan_type: builtins.object = ...,
        index_set: builtins.object = ...,
        category: builtins.object = ...,
    ) -> _SageObject: ...
    def __init__(
        self,
        ambient: builtins.object,
        virtualization: builtins.object,
        scaling_factors: builtins.object,
        contained: builtins.object,
        generators: builtins.object,
        cartan_type: builtins.object,
        index_set: builtins.object,
        category: builtins.object,
    ) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    def virtualization(self) -> _SageObject: ...
    def scaling_factors(self) -> _SageObject: ...

    class Element:
        def e(self, i: builtins.int) -> _SageObject: ...
        def f(self, i: builtins.int) -> _SageObject: ...
        def epsilon(self, i: builtins.int) -> _SageObject: ...
        def phi(self, i: builtins.int) -> _SageObject: ...
        def weight(self) -> _SageObject: ...
