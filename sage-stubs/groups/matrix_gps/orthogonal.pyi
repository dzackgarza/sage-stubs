from sage.groups.matrix_gps.linear import LinearMatrixGroup_generic
from sage.matrix.matrix import Matrix
from sage.rings.ring import Ring

def normalize_args_e(self, ring: Ring, e: int | None) -> tuple[int, Ring, int]: ...
def _OG(
    self,
    R: Ring | int,
    special: bool,
    e: int | None = ...,
    var: str = ...,
    invariant_form: Matrix | None = ...,
) -> OrthogonalMatrixGroup_generic: ...
def GO(
    self,
    R: Ring | int,
    e: int | None = ...,
    var: str = ...,
    invariant_form: Matrix | None = ...,
) -> OrthogonalMatrixGroup_generic: ...
def SO(
    self,
    R: Ring | int,
    e: int | None = ...,
    var: str = ...,
    invariant_form: Matrix | None = ...,
) -> OrthogonalMatrixGroup_generic: ...

class OrthogonalMatrixGroup_generic(LinearMatrixGroup_generic):
    def invariant_bilinear_form(self) -> Matrix: ...
    def _check_matrix(self, x: Matrix, *args: object) -> None: ...
    def degree(self) -> int: ...
