from typing import Generic, Literal, Self, TypeVar, overload

import numpy as np
from numpy.typing import NDArray

from sage.matrix.matrix_numpy_dense import Matrix_numpy_dense
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.complex_double import ComplexDoubleElement, ComplexDoubleField_class
from sage.rings.infinity import MinusInfinity, PlusInfinity
from sage.rings.integer import Integer
from sage.rings.real_double import RealDoubleElement, RealDoubleField_class

_DoubleScalar = TypeVar(
    "_DoubleScalar",
    RealDoubleElement,
    ComplexDoubleElement,
    default=RealDoubleElement,
)

type _NormOrder = int | Integer | str | PlusInfinity | MinusInfinity
type _EigenAlgorithm = Literal["default", "symmetric", "hermitian"]
type _HermitianAlgorithm = Literal["naive", "orthonormal"]
type _Tolerance = float | RealDoubleElement
type _Eigenvalue = RealDoubleElement | ComplexDoubleElement
type _EigenvalueResult = (
    _Eigenvalue
    | tuple[_Eigenvalue, int]
    | tuple[_Eigenvalue, _Eigenvalue]
)
type _Eigenvector = FreeModuleElement[ComplexDoubleElement]
type _EigenvectorData = tuple[
    ComplexDoubleElement,
    list[_Eigenvector],
    Literal[1],
]
type _HomogeneousEigenvectorData = tuple[
    tuple[ComplexDoubleElement, ComplexDoubleElement],
    list[_Eigenvector],
    Literal[1],
]
type _AnyEigenvectorData = _EigenvectorData | _HomogeneousEigenvectorData


class Matrix_double_dense(
    Matrix_numpy_dense[_DoubleScalar],
    Generic[_DoubleScalar],
):
    def LU_valid(self) -> bool: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def __neg__(self) -> Self: ...
    def __invert__(self) -> Self: ...
    def condition(
        self,
        p: _NormOrder = ...,
    ) -> RealDoubleElement | PlusInfinity: ...
    def norm(
        self,
        p: _NormOrder = ...,
    ) -> RealDoubleElement: ...
    def singular_values(
        self,
        eps: _Tolerance | Literal["auto"] | None = ...,
    ) -> list[RealDoubleElement]: ...
    def LU(self) -> tuple[Self, Self, Self]: ...

    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["default"] = ...,
        tol: None = ...,
        homogeneous: Literal[False] = ...,
    ) -> list[ComplexDoubleElement]: ...
    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["symmetric", "hermitian"],
        tol: None = ...,
        homogeneous: Literal[False] = ...,
    ) -> list[RealDoubleElement]: ...
    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["default"] = ...,
        tol: _Tolerance,
        homogeneous: Literal[False] = ...,
    ) -> list[tuple[ComplexDoubleElement, int]]: ...
    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["symmetric", "hermitian"],
        tol: _Tolerance,
        homogeneous: Literal[False] = ...,
    ) -> list[tuple[RealDoubleElement, int]]: ...
    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["default"] = ...,
        tol: _Tolerance | None = ...,
        homogeneous: Literal[True],
    ) -> list[tuple[ComplexDoubleElement, ComplexDoubleElement]]: ...
    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["symmetric", "hermitian"],
        tol: _Tolerance | None = ...,
        homogeneous: Literal[True],
    ) -> list[tuple[RealDoubleElement, RealDoubleElement]]: ...
    @overload
    def eigenvalues(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: _EigenAlgorithm = ...,
        tol: _Tolerance | None = ...,
        homogeneous: bool = ...,
    ) -> list[_EigenvalueResult]: ...

    @overload
    def eigenvectors_left(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["scipy"] | None = ...,
        homogeneous: Literal[False] = ...,
    ) -> list[_EigenvectorData] | tuple[list[_EigenvectorData], Self]: ...
    @overload
    def eigenvectors_left(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["scipy"] | None = ...,
        homogeneous: Literal[True],
    ) -> (
        list[_HomogeneousEigenvectorData]
        | tuple[list[_HomogeneousEigenvectorData], Self]
    ): ...
    @overload
    def eigenvectors_left(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        algorithm: Literal["scipy"] | None = ...,
        homogeneous: bool = ...,
    ) -> list[_AnyEigenvectorData] | tuple[list[_AnyEigenvectorData], Self]: ...
    left_eigenvectors = eigenvectors_left

    @overload
    def eigenvectors_right(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        homogeneous: Literal[False] = ...,
    ) -> list[_EigenvectorData] | tuple[list[_EigenvectorData], Self]: ...
    @overload
    def eigenvectors_right(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        homogeneous: Literal[True],
    ) -> (
        list[_HomogeneousEigenvectorData]
        | tuple[list[_HomogeneousEigenvectorData], Self]
    ): ...
    @overload
    def eigenvectors_right(
        self,
        other: (
            Matrix_double_dense[RealDoubleElement]
            | Matrix_double_dense[ComplexDoubleElement]
            | None
        ) = ...,
        *,
        homogeneous: bool = ...,
    ) -> list[_AnyEigenvectorData] | tuple[list[_AnyEigenvectorData], Self]: ...
    right_eigenvectors = eigenvectors_right

    def _solve_right_nonsingular_square(
        self,
        B: Matrix_double_dense[_DoubleScalar],
        check_rank: bool = ...,
    ) -> Self: ...
    def _solve_right_general(
        self,
        B: Matrix_double_dense[_DoubleScalar],
        check: bool = ...,
    ) -> Self: ...
    def determinant(self) -> _DoubleScalar: ...
    def log_determinant(self) -> RealDoubleElement: ...
    def conjugate(self) -> Self: ...
    def SVD(self) -> tuple[Self, Self, Self]: ...
    def QR(self) -> tuple[Self, Self]: ...
    def is_unitary(
        self,
        tol: _Tolerance = ...,
        algorithm: _HermitianAlgorithm = ...,
    ) -> bool: ...
    def _is_hermitian_orthonormal(
        self,
        tol: _Tolerance = ...,
        skew: bool = ...,
    ) -> bool: ...
    def is_hermitian(
        self,
        tol: _Tolerance = ...,
        algorithm: _HermitianAlgorithm = ...,
    ) -> bool: ...
    def is_skew_hermitian(
        self,
        tol: _Tolerance = ...,
        algorithm: _HermitianAlgorithm = ...,
    ) -> bool: ...
    def is_normal(
        self,
        tol: _Tolerance = ...,
        algorithm: _HermitianAlgorithm = ...,
    ) -> bool: ...

    @overload
    def schur(
        self,
        base_ring: None = ...,
    ) -> tuple[Self, Self]: ...
    @overload
    def schur(
        self,
        base_ring: RealDoubleField_class,
    ) -> tuple[
        Matrix_double_dense[RealDoubleElement],
        Matrix_double_dense[RealDoubleElement],
    ]: ...
    @overload
    def schur(
        self,
        base_ring: ComplexDoubleField_class,
    ) -> tuple[
        Matrix_double_dense[ComplexDoubleElement],
        Matrix_double_dense[ComplexDoubleElement],
    ]: ...
    @overload
    def schur(
        self,
        base_ring: (
            RealDoubleField_class
            | ComplexDoubleField_class
            | None
        ) = ...,
    ) -> tuple[
        Matrix_double_dense[RealDoubleElement]
        | Matrix_double_dense[ComplexDoubleElement],
        Matrix_double_dense[RealDoubleElement]
        | Matrix_double_dense[ComplexDoubleElement],
    ]: ...

    def cholesky(self) -> Self: ...
    def is_positive_definite(self) -> bool: ...
    def _replace_self_with_numpy32(
        self,
        numpy_matrix: NDArray[np.generic],
    ) -> None: ...
    def _hadamard_row_bound(self) -> int: ...
    def exp(self) -> Self: ...
    def zero_at(
        self,
        eps: _Tolerance,
    ) -> Self: ...
    def round(
        self,
        ndigits: int | Integer = ...,
    ) -> Self: ...
    def _normalize_columns(self) -> Self: ...
    def _normalize_rows(self) -> Self: ...
