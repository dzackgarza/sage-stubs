from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.rings.integer import Integer

def matrix_integer_dense_rational_reconstruction(
    A: Matrix_integer_dense,
    N: Integer,
) -> Matrix_rational_dense: ...
