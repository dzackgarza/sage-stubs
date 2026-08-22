from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.rings.integer import Integer

type _IntegerLike = int | Integer


def p_saturation(
    A: Matrix_integer_dense,
    p: _IntegerLike,
    proof: bool = ...,
) -> Matrix_integer_dense: ...


def random_sublist_of_size(
    k: int,
    n: int,
) -> list[int]: ...


def solve_system_with_difficult_last_row(
    B: Matrix_integer_dense,
    A: Matrix_integer_dense,
) -> Matrix_rational_dense: ...


def saturation(
    A: Matrix_integer_dense,
    proof: bool = ...,
    p: _IntegerLike = ...,
    max_dets: int = ...,
) -> Matrix_integer_dense: ...


def index_in_saturation(
    A: Matrix_integer_dense,
    proof: bool = ...,
) -> Integer: ...
