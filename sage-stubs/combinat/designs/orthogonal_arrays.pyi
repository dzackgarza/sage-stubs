import builtins

class _SageObject: ...

def transversal_design(
    self,
    n: builtins.int,
    resolvable: builtins.bool = ...,
    check: builtins.bool = ...,
    existence: builtins.bool = ...,
) -> _SageObject: ...

class TransversalDesign:
    def __init__(
        self,
        blocks: builtins.object,
        k: builtins.int = ...,
        n: builtins.int = ...,
        check: builtins.bool = ...,
        **kwds: builtins.object,
    ) -> None: ...

def is_transversal_design(
    self, k: builtins.int, n: builtins.int, verbose: builtins.bool = ...
) -> builtins.bool: ...
def wilson_construction(
    self,
    k: builtins.int,
    r: builtins.int,
    m: builtins.int,
    u: builtins.object,
    check: builtins.bool = ...,
    explain_construction: builtins.bool = ...,
) -> _SageObject: ...
def TD_product(
    self,
    TD1: builtins.object,
    n1: builtins.object,
    TD2: builtins.object,
    n2: builtins.object,
    check: builtins.bool = ...,
) -> _SageObject: ...
def orthogonal_array(
    self,
    n: builtins.int,
    t: builtins.int = ...,
    resolvable: builtins.bool = ...,
    check: builtins.bool = ...,
    existence: builtins.bool = ...,
    explain_construction: builtins.bool = ...,
) -> _SageObject: ...
def largest_available_k(self, t: builtins.int = ...) -> _SageObject: ...
def incomplete_orthogonal_array(
    self,
    n: builtins.int,
    holes: builtins.object,
    resolvable: builtins.bool = ...,
    existence: builtins.bool = ...,
) -> _SageObject: ...
def OA_find_disjoint_blocks(
    self,
    k: builtins.int,
    n: builtins.int,
    x: builtins.object,
    *,
    solver: builtins.object = ...,
    integrality_tolerance: builtins.float = ...,
) -> _SageObject: ...
def OA_relabel(
    self,
    k: builtins.int,
    n: builtins.int,
    blocks: builtins.object = ...,
    matrix: builtins.object = ...,
    symbol_list: builtins.object = ...,
) -> _SageObject: ...
def OA_standard_label(self) -> _SageObject: ...
def OA_n_times_2_pow_c_from_matrix(
    self,
    c: builtins.object,
    G: builtins.object,
    A: builtins.object,
    Y: builtins.object,
    check: builtins.bool = ...,
) -> _SageObject: ...
def OA_from_quasi_difference_matrix(
    self,
    G: builtins.object,
    add_col: builtins.bool = ...,
    fill_hole: builtins.bool = ...,
) -> _SageObject: ...
def OA_from_Vmt(self, t: builtins.object, V: builtins.object) -> _SageObject: ...
def QDM_from_Vmt(self, t: builtins.object, V: builtins.object) -> _SageObject: ...
def OA_from_PBD(
    self, n: builtins.int, PBD: builtins.object, check: builtins.bool = ...
) -> _SageObject: ...
def OA_from_wider_OA(self, k: builtins.int) -> _SageObject: ...

class OAMainFunctions:
    def __init__(self, *args: builtins.object, **kwds: builtins.object) -> None: ...
    largest_available_k: _SageObject

    @staticmethod
    def explain_construction(
        k: builtins.int, n: builtins.int, t: builtins.int = ...
    ) -> _SageObject: ...
    @staticmethod
    def build(
        k: builtins.int,
        n: builtins.int,
        t: builtins.int = ...,
        resolvable: builtins.bool = ...,
    ) -> _SageObject: ...
    @staticmethod
    def exists(
        k: builtins.int, n: builtins.int, t: builtins.int = ...
    ) -> _SageObject: ...
    @staticmethod
    def is_available(
        k: builtins.int, n: builtins.int, t: builtins.int = ...
    ) -> builtins.bool: ...
