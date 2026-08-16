import builtins

class _SageObject: ...

def rational_param_as_tuple(self) -> _SageObject: ...

class Hypergeometric:
    def __init__(self) -> None: ...
    def __call__(
        self,
        a: builtins.object,
        b: builtins.object,
        z: builtins.object,
        **kwargs: builtins.object,
    ) -> _SageObject: ...

    class EvaluationMethods:
        def sorted_parameters(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> _SageObject: ...
        def eliminate_parameters(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> _SageObject: ...
        def is_termwise_finite(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> builtins.bool: ...
        def is_terminating(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> builtins.bool: ...
        def is_absolutely_convergent(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> builtins.bool: ...
        def terms(
            self,
            a: builtins.object,
            b: builtins.object,
            z: builtins.object,
            n: builtins.int = ...,
        ) -> _SageObject: ...
        def deflated(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> _SageObject: ...

hypergeometric: _SageObject

def closed_form(self) -> _SageObject: ...

class Hypergeometric_M:
    def __init__(self) -> None: ...

    class EvaluationMethods:
        def generalized(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> _SageObject: ...

hypergeometric_M: _SageObject

class Hypergeometric_U:
    def __init__(self) -> None: ...

    class EvaluationMethods:
        def generalized(
            self, a: builtins.object, b: builtins.object, z: builtins.object
        ) -> _SageObject: ...

hypergeometric_U: _SageObject
