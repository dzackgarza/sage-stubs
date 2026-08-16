import builtins

class _SageObject: ...

class TreeNode:
    number_of_descendants: int
    label: builtins.str

    def __init__(
        self,
        parent: builtins.object = ...,
        children: builtins.object = ...,
        label: builtins.str = ...,
    ) -> None: ...
    def compute_number_of_descendants(self) -> _SageObject: ...
    def compute_depth_of_self_and_children(self) -> _SageObject: ...
    def append_child(self, child: builtins.object) -> _SageObject: ...

def minimal_schnyder_wood(
    self,
    root_edge: builtins.object = ...,
    minimal: builtins.bool = ...,
    check: builtins.bool = ...,
) -> _SageObject: ...
