from typing import Literal, overload

from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.rings.integer import Integer


@overload
def hnf(
    A: Matrix_integer_dense,
    proof: bool | None = ...,
    include_zero_rows: bool = ...,
    transformation: Literal[False] = ...,
) -> Matrix_integer_dense: ...
@overload
def hnf(
    A: Matrix_integer_dense,
    proof: bool | None,
    include_zero_rows: bool,
    transformation: Literal[True],
) -> tuple[Matrix_integer_dense, Matrix_integer_dense]: ...


def hnf_mod(
    A: Matrix_integer_dense,
    modulus: int | Integer,
) -> Matrix_integer_dense: ...


def hnf_padic(
    A: Matrix_integer_dense,
    prime: int | Integer,
    precision: int | Integer,
) -> Matrix_integer_dense: ...
