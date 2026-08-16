import builtins

class _SageObject: ...

def group_divisible_design(
    self,
    K: builtins.int,
    G: builtins.object,
    existence: builtins.bool = ...,
    check: builtins.bool = ...,
) -> _SageObject: ...
def GDD_4_2(
    self, existence: builtins.bool = ..., check: builtins.bool = ...
) -> _SageObject: ...

class GroupDivisibleDesign:
    def __init__(
        self,
        points: builtins.object,
        groups: builtins.object,
        blocks: builtins.object,
        G: builtins.object = ...,
        K: builtins.int = ...,
        lambd: builtins.int = ...,
        check: builtins.bool = ...,
        copy: builtins.bool = ...,
        **kwds: builtins.object,
    ) -> None: ...
    def groups(self) -> _SageObject: ...
