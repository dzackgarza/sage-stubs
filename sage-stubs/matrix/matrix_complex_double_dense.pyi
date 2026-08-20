from collections.abc import Callable, Mapping, Sequence
from typing import Self

from numpy import ndarray

from sage.matrix.matrix_double_dense import Matrix_double_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.real_double import RealDoubleElement
from sage.structure.parent import ElementConstructorInput


type _ComplexMatrixEntries = (
    complex
    | ComplexDoubleElement
    | Sequence[complex | ComplexDoubleElement | ElementConstructorInput]
    | Sequence[Sequence[complex | ComplexDoubleElement | ElementConstructorInput]]
    | Mapping[
        tuple[int, int],
        complex | ComplexDoubleElement | ElementConstructorInput,
    ]
    | Callable[[int, int], complex | ComplexDoubleElement | ElementConstructorInput]
    | ElementConstructorInput
    | None
)


class Matrix_complex_double_dense(Matrix_double_dense[ComplexDoubleElement]):
    def __init__(
        self,
        parent: MatrixSpace[ComplexDoubleElement],
        entries: _ComplexMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[ComplexDoubleElement]: ...
    def list(self) -> list[ComplexDoubleElement]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[ComplexDoubleElement]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[ComplexDoubleElement]: ...
    def transpose(self) -> Self: ...
    def numpy(self) -> ndarray: ...
    def determinant(self, algorithm: str = ...) -> ComplexDoubleElement: ...
    det = determinant
    def trace(self) -> ComplexDoubleElement: ...
    def rank(self, eps: float | None = ...) -> int: ...
    def inverse(self) -> Self: ...
    __invert__ = inverse
    def conjugate(self) -> Self: ...
    def conjugate_transpose(self) -> Self: ...
    H = conjugate_transpose
    def is_hermitian(self, tol: float = ...) -> bool: ...
    def eigenvalues(
        self,
        algorithm: str = ...,
    ) -> list[ComplexDoubleElement]: ...
    def eigenmatrix_right(
        self,
        algorithm: str = ...,
    ) -> tuple[Self, Self]: ...
    def eigenmatrix_left(
        self,
        algorithm: str = ...,
    ) -> tuple[Self, Self]: ...
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
    def SVD(self) -> tuple[Self, Matrix_real_double_dense, Self]: ...
    def QR(self) -> tuple[Self, Self]: ...
    def schur(self) -> tuple[Self, Self]: ...
    def pseudoinverse(
        self,
        eps: float | None = ...,
    ) -> Self: ...
    def solve_right(
        self,
        B: Self | FreeModuleElement[ComplexDoubleElement],
    ) -> Self | FreeModuleElement[ComplexDoubleElement]: ...
    def solve_left(
        self,
        B: Self | FreeModuleElement[ComplexDoubleElement],
    ) -> Self | FreeModuleElement[ComplexDoubleElement]: ...
    def exp(self) -> Self: ...
    def logarithm(self) -> Self: ...


from sage.matrix.matrix_real_double_dense import Matrix_real_double_dense
