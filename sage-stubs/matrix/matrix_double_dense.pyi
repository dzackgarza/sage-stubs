from typing import Generic, Self, TypeVar

from numpy import ndarray

from sage.matrix.matrix_dense import Matrix_dense
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.real_double import RealDoubleElement

_DoubleScalar = TypeVar(
    "_DoubleScalar",
    RealDoubleElement,
    ComplexDoubleElement,
    default=RealDoubleElement,
)


class Matrix_double_dense(
    Matrix_dense[_DoubleScalar],
    Generic[_DoubleScalar],
):
    def numpy(self) -> ndarray: ...
    def determinant(self, algorithm: str = ...) -> _DoubleScalar: ...
    det = determinant
    def trace(self) -> _DoubleScalar: ...
    def rank(self, eps: float | None = ...) -> int: ...
    def inverse(self) -> Self: ...
    __invert__ = inverse
    def norm(
        self,
        p: int | float | str = ...,
    ) -> RealDoubleElement: ...
    def condition(
        self,
        p: int | float | str = ...,
    ) -> RealDoubleElement: ...
    condition_number = condition
    def eigenvalues(
        self,
        algorithm: str = ...,
    ) -> list[ComplexDoubleElement]: ...
    def eigenmatrix_right(
        self,
        algorithm: str = ...,
    ) -> tuple[
        Matrix_double_dense[ComplexDoubleElement],
        Matrix_double_dense[ComplexDoubleElement],
    ]: ...
    def eigenmatrix_left(
        self,
        algorithm: str = ...,
    ) -> tuple[
        Matrix_double_dense[ComplexDoubleElement],
        Matrix_double_dense[ComplexDoubleElement],
    ]: ...
    def eigenvectors_right(
        self,
        algorithm: str = ...,
    ) -> list[
        tuple[
            ComplexDoubleElement,
            list[FreeModuleElement[ComplexDoubleElement]],
            int,
        ]
    ]: ...
    def eigenvectors_left(
        self,
        algorithm: str = ...,
    ) -> list[
        tuple[
            ComplexDoubleElement,
            list[FreeModuleElement[ComplexDoubleElement]],
            int,
        ]
    ]: ...
    def singular_values(
        self,
        eps: float | None = ...,
    ) -> list[RealDoubleElement]: ...
    def SVD(
        self,
    ) -> tuple[
        Self,
        Matrix_double_dense[RealDoubleElement],
        Self,
    ]: ...
    def QR(self) -> tuple[Self, Self]: ...
    def schur(
        self,
    ) -> tuple[
        Matrix_double_dense[ComplexDoubleElement],
        Matrix_double_dense[ComplexDoubleElement],
    ]: ...
    def exp(self) -> Self: ...
    def logarithm(
        self,
    ) -> Matrix_double_dense[ComplexDoubleElement]: ...
    def pseudoinverse(
        self,
        eps: float | None = ...,
    ) -> Self: ...
    def solve_right(
        self,
        B: Self | FreeModuleElement[_DoubleScalar],
    ) -> Self | FreeModuleElement[_DoubleScalar]: ...
    def solve_left(
        self,
        B: Self | FreeModuleElement[_DoubleScalar],
    ) -> Self | FreeModuleElement[_DoubleScalar]: ...
    def least_squares(
        self,
        B: Self | FreeModuleElement[_DoubleScalar],
    ) -> Self | FreeModuleElement[_DoubleScalar]: ...
