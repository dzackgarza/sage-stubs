import builtins

class _SageObject: ...

class WeierstrassTransformation:
    def __init__(
        self,
        domain: builtins.object,
        codomain: builtins.object,
        defining_polynomials: builtins.object,
        post_multiplication: builtins.object,
    ) -> None: ...
    def post_rescaling(self) -> _SageObject: ...

def WeierstrassTransformationWithInverse(
    self,
    codomain: builtins.object,
    defining_polynomials: builtins.object,
    post_multiplication: builtins.object,
    inv_defining_polynomials: builtins.object,
    inv_post_multiplication: builtins.object,
) -> _SageObject: ...

class WeierstrassTransformationWithInverse_class:
    def inverse(self) -> _SageObject: ...
