from typing import Self

from sage.matrix.matrix_sparse import Matrix_sparse
from sage.rings.real_double import RealDoubleElement


class Matrix_double_sparse(Matrix_sparse[RealDoubleElement]):
    def transpose(self) -> Self: ...
    def norm(self, p: int | float | str = ...) -> float: ...
    def density(self) -> float: ...
    def dense_matrix(self) -> Matrix_real_double_dense: ...


from sage.matrix.matrix_real_double_dense import Matrix_real_double_dense
