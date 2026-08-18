from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.rings.integer import Integer


def saturation(
    A: Matrix_integer_dense,
    p: int | Integer = ...,
    proof: bool | None = ...,
    max_dets: int = ...,
) -> Matrix_integer_dense: ...


def index_in_saturation(
    A: Matrix_integer_dense,
    proof: bool | None = ...,
) -> Integer: ...


def p_saturation(
    A: Matrix_integer_dense,
    p: int | Integer,
    proof: bool | None = ...,
) -> Matrix_integer_dense: ...
