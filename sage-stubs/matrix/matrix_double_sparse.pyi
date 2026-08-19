from typing import Generic, Self, TypeVar

from sage.matrix.matrix_generic_sparse import Matrix_generic_sparse
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.real_double import RealDoubleElement

_DoubleScalar = TypeVar(
    "_DoubleScalar",
    RealDoubleElement,
    ComplexDoubleElement,
    default=RealDoubleElement,
)


class Matrix_double_sparse(
    Matrix_generic_sparse[_DoubleScalar],
    Generic[_DoubleScalar],
):
    def is_hermitian(
        self,
        tolerance: float = ...,
    ) -> bool: ...
    def is_skew_hermitian(
        self,
        tolerance: float = ...,
    ) -> bool: ...
    def cholesky(self) -> Self: ...
