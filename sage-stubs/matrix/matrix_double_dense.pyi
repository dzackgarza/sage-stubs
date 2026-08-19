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
    def norm(
        self,
        p: int | float | str = ...,
    ) -> RealDoubleElement: ...
    def condition(
        self,
        p: int | float | str = ...,
    ) -> RealDoubleElement: ...
    condition_number = condition
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
    def schur(self) -> tuple[Self, Self]: ...
    def exp(self) -> Self: ...
    def logarithm(self) -> Self: ...
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
