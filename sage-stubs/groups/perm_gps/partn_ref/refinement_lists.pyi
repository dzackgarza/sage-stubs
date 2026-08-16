import builtins

class _SageObject: ...

def is_isomorphic(self, other: builtins.object) -> builtins.bool: ...
def all_list_children_are_equivalent(
    PS: builtins.object, S: builtins.object
) -> _SageObject: ...
def refine_list(
    PS: builtins.object,
    S: builtins.object,
    cells_to_refine_by: builtins.object,
    ctrb_len: builtins.object,
) -> _SageObject: ...
def compare_lists(
    gamma_1: builtins.object,
    gamma_2: builtins.object,
    S1: builtins.object,
    S2: builtins.object,
    degree: builtins.object,
) -> _SageObject: ...
