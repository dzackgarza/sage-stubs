import builtins

class _SageObject: ...

def compute_G(self, F: builtins.object) -> _SageObject: ...
def low_weight_bases(
    self,
    p: builtins.int,
    m: builtins.int,
    NN: builtins.object,
    weightbound: builtins.object,
) -> _SageObject: ...
def random_low_weight_bases(
    self,
    p: builtins.int,
    m: builtins.int,
    NN: builtins.object,
    weightbound: builtins.object,
) -> _SageObject: ...
def low_weight_generators(
    self, p: builtins.int, m: builtins.int, NN: builtins.object
) -> _SageObject: ...
def random_solution(self, K: builtins.int) -> _SageObject: ...
def ech_form(self, p: builtins.int) -> _SageObject: ...
def random_new_basis_modp(
    self,
    p: builtins.int,
    k: builtins.int,
    LWBModp: builtins.object,
    TotalBasisModp: builtins.object,
    elldash: builtins.object,
    bound: builtins.object,
) -> _SageObject: ...
def complementary_spaces_modp(
    self,
    p: builtins.int,
    k0: builtins.object,
    n: builtins.int,
    elldash: builtins.object,
    LWBModp: builtins.object,
    bound: builtins.object,
) -> _SageObject: ...
def complementary_spaces(
    self,
    p: builtins.int,
    k0: builtins.object,
    n: builtins.int,
    mdash: builtins.object,
    elldashp: builtins.object,
    elldash: builtins.object,
    modformsring: builtins.object,
    bound: builtins.object,
) -> _SageObject: ...
def higher_level_katz_exp(
    self,
    N: builtins.int,
    k0: builtins.object,
    m: builtins.int,
    mdash: builtins.object,
    elldash: builtins.object,
    elldashp: builtins.object,
    modformsring: builtins.object,
    bound: builtins.object,
) -> _SageObject: ...
def compute_elldash(
    self, N: builtins.int, k0: builtins.object, n: builtins.int
) -> _SageObject: ...
def hecke_series_degree_bound(
    self, N: builtins.int, k: builtins.int, m: builtins.int
) -> _SageObject: ...
def higher_level_UpGj(
    self,
    N: builtins.int,
    klist: builtins.object,
    m: builtins.int,
    modformsring: builtins.object,
    bound: builtins.object,
    extra_data: builtins.bool = ...,
) -> _SageObject: ...
def compute_Wi(
    self,
    p: builtins.int,
    h: builtins.object,
    hj: builtins.object,
    E4: builtins.object,
    E6: builtins.object,
) -> _SageObject: ...
def katz_expansions(
    self,
    p: builtins.int,
    ellp: builtins.object,
    mdash: builtins.object,
    n: builtins.int,
) -> _SageObject: ...
def level1_UpGj(
    self, klist: builtins.object, m: builtins.int, extra_data: builtins.bool = ...
) -> _SageObject: ...
def is_valid_weight_list(self, p: builtins.int) -> None: ...
def hecke_series(
    self,
    N: builtins.int,
    klist: builtins.object,
    m: builtins.int,
    modformsring: builtins.bool = ...,
    weightbound: builtins.int = ...,
) -> _SageObject: ...
