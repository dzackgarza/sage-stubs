import builtins

class _SageObject: ...

class LinearBinaryCodeStruct:
    def __cinit__(self, matrix: builtins.object) -> _SageObject: ...
    def run(self, partition: builtins.object = ...) -> _SageObject: ...
    def automorphism_group(self) -> _SageObject: ...
    def canonical_relabeling(self) -> _SageObject: ...
    def is_isomorphic(self, other: builtins.object) -> builtins.bool: ...
    def __dealloc__(self) -> _SageObject: ...

def ith_word_linear(self, i: builtins.object, word: builtins.object) -> _SageObject: ...

class NonlinearBinaryCodeStruct:
    def __cinit__(self, arg: builtins.object) -> _SageObject: ...
    def __dealloc__(self) -> _SageObject: ...
    def run(self, partition: builtins.object = ...) -> _SageObject: ...
    def automorphism_group(self) -> _SageObject: ...
    def canonical_relabeling(self) -> _SageObject: ...
    def is_isomorphic(self, other: builtins.object) -> builtins.bool: ...

def ith_word_nonlinear(
    self, i: builtins.object, word: builtins.object
) -> _SageObject: ...
def refine_by_bip_degree(
    col_ps: builtins.object,
    S: builtins.object,
    cells_to_refine_by: builtins.object,
    ctrb_len: builtins.object,
) -> _SageObject: ...
def compare_linear_codes(
    gamma_1: builtins.object,
    gamma_2: builtins.object,
    S1: builtins.object,
    S2: builtins.object,
    degree: builtins.object,
) -> _SageObject: ...
def compare_nonlinear_codes(
    gamma_1: builtins.object,
    gamma_2: builtins.object,
    S1: builtins.object,
    S2: builtins.object,
    degree: builtins.object,
) -> _SageObject: ...
def all_children_are_equivalent(
    col_ps: builtins.object, S: builtins.object
) -> _SageObject: ...
def word_degree(
    word_ps: builtins.object,
    BCS: builtins.object,
    entry: builtins.object,
    cell_index: builtins.object,
    col_ps: builtins.object,
) -> _SageObject: ...
def col_degree(
    col_ps: builtins.object,
    BCS: builtins.object,
    entry: builtins.object,
    cell_index: builtins.object,
    word_ps: builtins.object,
) -> _SageObject: ...
def sort_by_function_codes(
    PS: builtins.object,
    start: builtins.object,
    degrees: builtins.object,
    counts: builtins.object,
    output: builtins.object,
    count_max: builtins.object,
) -> _SageObject: ...
def random_tests(
    num: builtins.object = ...,
    n_max: builtins.object = ...,
    k_max: builtins.object = ...,
    nwords_max: builtins.object = ...,
    perms_per_code: builtins.object = ...,
    density_range: builtins.object = ...,
) -> _SageObject: ...
