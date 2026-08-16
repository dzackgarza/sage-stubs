import builtins

class _SageObject: ...

def biplane(self, existence: builtins.bool = ...) -> _SageObject: ...
def balanced_incomplete_block_design(
    self,
    k: builtins.int,
    lambd: builtins.int = ...,
    existence: builtins.bool = ...,
    use_LJCR: builtins.bool = ...,
) -> _SageObject: ...
def BruckRyserChowla_check(
    self, k: builtins.int, lambd: builtins.object
) -> _SageObject: ...
def steiner_triple_system(self) -> _SageObject: ...
def BIBD_from_TD(
    self, k: builtins.int, existence: builtins.bool = ...
) -> _SageObject: ...
def BIBD_from_difference_family(
    self, D: builtins.object, lambd: builtins.object = ..., check: builtins.bool = ...
) -> _SageObject: ...
def v_4_1_BIBD(self, check: builtins.bool = ...) -> _SageObject: ...
def BIBD_from_PBD(
    self,
    v: builtins.object,
    k: builtins.int,
    check: builtins.bool = ...,
    base_cases: builtins.object = ...,
) -> _SageObject: ...
def PBD_4_5_8_9_12(self, check: builtins.bool = ...) -> _SageObject: ...

table_7_1: _SageObject

def v_5_1_BIBD(self, check: builtins.bool = ...) -> _SageObject: ...
def PBD_from_TD(self, t: builtins.object, u: builtins.object) -> _SageObject: ...
def BIBD_5q_5_for_q_prime_power(self) -> _SageObject: ...
def BIBD_from_arc_in_desarguesian_projective_plane(
    self, k: builtins.int, existence: builtins.bool = ...
) -> _SageObject: ...

class PairwiseBalancedDesign:
    def __init__(
        self,
        points: builtins.object,
        blocks: builtins.object,
        K: builtins.int = ...,
        lambd: builtins.int = ...,
        check: builtins.bool = ...,
        copy: builtins.bool = ...,
        **kwds: builtins.object,
    ) -> None: ...

class BalancedIncompleteBlockDesign:
    def __init__(
        self,
        points: builtins.object,
        blocks: builtins.object,
        k: builtins.int = ...,
        lambd: builtins.int = ...,
        check: builtins.bool = ...,
        copy: builtins.bool = ...,
        **kwds: builtins.object,
    ) -> None: ...
    def arc(
        self,
        s: builtins.int = ...,
        solver: builtins.object = ...,
        verbose: builtins.int = ...,
        *,
        integrality_tolerance: builtins.float = ...,
    ) -> _SageObject: ...

BIBD: _SageObject
