import builtins
from collections.abc import (
    Hashable,
)

from sage.structure.element import Element

class _SageObject: ...

def theta_series(
    self,
    Max: builtins.int = ...,
    var_str: builtins.str = ...,
    safe_flag: builtins.bool = ...,
) -> _SageObject: ...
def theta_by_pari(
    self,
    Max: builtins.object,
    var_str: builtins.str = ...,
    safe_flag: builtins.bool = ...,
) -> _SageObject: ...
def theta_by_cholesky(self, q_prec: builtins.object) -> _SageObject: ...
def theta_series_degree_2(self, prec: builtins.int) -> dict[Hashable, Element]: ...
