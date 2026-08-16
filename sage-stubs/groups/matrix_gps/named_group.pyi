import builtins

class _SageObject: ...

def normalize_args_vectorspace(
    self, *args: builtins.object, **kwds: builtins.object
) -> _SageObject: ...
def normalize_args_invariant_form(
    self, d: builtins.object, invariant_form: builtins.object
) -> _SageObject: ...

class NamedMatrixGroup_generic:
    def __init__(
        self,
        degree: builtins.int,
        base_ring: builtins.object,
        special: builtins.object,
        sage_name: builtins.str,
        latex_string: builtins.object,
        category: builtins.object = ...,
        invariant_form: builtins.object = ...,
    ) -> None: ...
    def __richcmp__(
        self, other: builtins.object, op: builtins.object
    ) -> _SageObject: ...
