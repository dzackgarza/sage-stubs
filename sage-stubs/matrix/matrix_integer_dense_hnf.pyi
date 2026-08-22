from collections.abc import Iterable, Sequence

from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.rings.integer import Integer

type _IntegerLike = int | Integer
type _PivotData = list[int] | tuple[int, ...]
type _OnesData = tuple[list[int], list[int], list[int], list[int]]
type _ExtractedOnesData = tuple[
    Matrix_integer_dense | None,
    Matrix_integer_dense | None,
    Matrix_rational_dense | None,
    list[int],
    list[int],
    list[int],
    list[int],
]


def max_det_prime(n: _IntegerLike) -> Integer: ...


def det_from_modp_and_divisor(
    A: Matrix_integer_dense,
    d: _IntegerLike,
    p: _IntegerLike,
    z_mod: list[_IntegerLike],
    moduli: list[_IntegerLike],
    z_so_far: _IntegerLike = ...,
    N_so_far: _IntegerLike = ...,
) -> tuple[Integer, Integer, Integer]: ...


def det_given_divisor(
    A: Matrix_integer_dense,
    d: _IntegerLike,
    proof: bool = ...,
    stabilize: int = ...,
) -> Integer: ...


def det_padic(
    A: Matrix_integer_dense,
    proof: bool = ...,
    stabilize: int = ...,
) -> Integer: ...


def double_det(
    A: Matrix_integer_dense,
    b: Matrix_integer_dense,
    c: Matrix_integer_dense,
    proof: bool,
) -> tuple[Integer, Integer]: ...


def add_column_fallback(
    B: Matrix_integer_dense,
    a: Matrix_integer_dense,
    proof: bool,
) -> Matrix_integer_dense: ...


def solve_system_with_difficult_last_row(
    B: Matrix_integer_dense,
    a: Matrix_integer_dense,
) -> Matrix_rational_dense: ...


def add_column(
    B: Matrix_integer_dense,
    H_B: Matrix_integer_dense,
    a: Matrix_integer_dense,
    proof: bool,
) -> Matrix_integer_dense: ...


def add_row(
    A: Matrix_integer_dense,
    b: Matrix_integer_dense,
    pivots: Sequence[int],
    include_zero_rows: bool,
) -> tuple[Matrix_integer_dense, list[int]]: ...


def pivots_of_hnf_matrix(
    H: Matrix_integer_dense,
) -> list[int]: ...


def hnf_square(
    A: Matrix_integer_dense,
    proof: bool,
) -> Matrix_integer_dense: ...


def interleave_matrices(
    A: Matrix_integer_dense,
    B: Matrix_integer_dense,
    cols1: Sequence[int],
    cols2: Sequence[int],
) -> Matrix_integer_dense: ...


def probable_pivot_rows(
    A: Matrix_integer_dense,
) -> tuple[int, ...]: ...


def probable_pivot_columns(
    A: Matrix_integer_dense,
) -> tuple[int, ...]: ...


def ones(
    H: Matrix_integer_dense,
    pivots: Sequence[int],
) -> _OnesData: ...


def extract_ones_data(
    H: Matrix_integer_dense,
    pivots: Sequence[int],
) -> _ExtractedOnesData: ...


def is_in_hnf_form(
    H: Matrix_integer_dense,
    pivots: Sequence[int],
) -> bool: ...


def probable_hnf(
    A: Matrix_integer_dense,
    include_zero_rows: bool,
    proof: bool,
) -> tuple[Matrix_integer_dense, _PivotData]: ...


def pad_zeros(
    A: Matrix_integer_dense,
    nrows: _IntegerLike,
) -> Matrix_integer_dense: ...


def hnf(
    A: Matrix_integer_dense,
    include_zero_rows: bool = ...,
    proof: bool = ...,
) -> tuple[Matrix_integer_dense, _PivotData]: ...


def hnf_with_transformation(
    A: Matrix_integer_dense,
    proof: bool = ...,
) -> tuple[Matrix_integer_dense, Matrix_integer_dense]: ...


def hnf_with_transformation_tests(
    n: int = ...,
    m: int = ...,
    trials: int = ...,
) -> None: ...


def benchmark_hnf(
    nrange: Iterable[_IntegerLike],
    bits: int = ...,
) -> None: ...


def benchmark_magma_hnf(
    nrange: Iterable[_IntegerLike],
    bits: int = ...,
) -> None: ...


def sanity_checks(
    times: int = ...,
    n: int = ...,
    m: int = ...,
    proof: bool = ...,
    stabilize: int = ...,
    check_using_magma: bool = ...,
) -> None: ...
