from collections.abc import Sequence

from sage.matrix.matrix0 import Matrix
from sage.matrix.matrix_integer_sparse import Matrix_integer_sparse
from sage.matrix.matrix_rational_sparse import Matrix_rational_sparse
from sage.matrix.misc_flint import (
    matrix_integer_dense_rational_reconstruction as matrix_integer_dense_rational_reconstruction,
)
from sage.matrix.misc_mpfr import hadamard_row_bound_mpfr as hadamard_row_bound_mpfr
from sage.rings.integer import Integer
from sage.rings.rational import Rational

def matrix_integer_sparse_rational_reconstruction(
    A: Matrix_integer_sparse,
    N: Integer,
) -> Matrix_rational_sparse: ...
def matrix_rational_echelon_form_multimodular(
    self: Matrix[Rational],
    height_guess: int | Integer | None = ...,
    proof: bool | None = ...,
) -> tuple[Matrix[Rational], tuple[int, ...]]: ...
def cmp_pivots(x: Sequence[int], y: Sequence[int]) -> int: ...
