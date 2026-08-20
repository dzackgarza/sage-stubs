from collections.abc import Callable, Mapping, Sequence
from types import ModuleType
from typing import Generic, Self, TypeVar, overload

import numpy as np
from numpy.typing import NDArray

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.real_double import RealDoubleElement
from sage.structure.parent import ElementConstructorInput

_NumpyScalar = TypeVar(
    "_NumpyScalar",
    RealDoubleElement,
    ComplexDoubleElement,
    default=RealDoubleElement,
)

type _RealArray = NDArray[np.float64]
type _ComplexArray = NDArray[np.complex128]
type _NumpyArray = _RealArray | _ComplexArray
type _NumpyMatrixEntries = (
    float
    | complex
    | RealDoubleElement
    | ComplexDoubleElement
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | ElementConstructorInput
    | None
)

numpy: ModuleType | None
scipy: ModuleType | None


class Matrix_numpy_dense(
    Matrix_dense[_NumpyScalar],
    Generic[_NumpyScalar],
):
    def __create_matrix__(self) -> None: ...
    def __init__(
        self,
        parent: MatrixSpace[_NumpyScalar],
        entries: _NumpyMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[_NumpyScalar]: ...
    def list(self) -> list[_NumpyScalar]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[_NumpyScalar]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[_NumpyScalar]: ...
    def transpose(self) -> Self: ...
    def is_symmetric(self, tol: float = ...) -> bool: ...
    def _is_lower_triangular(self, tol: float) -> bool: ...
    @overload
    def numpy(
        self: Matrix_numpy_dense[RealDoubleElement],
    ) -> _RealArray: ...
    @overload
    def numpy(
        self: Matrix_numpy_dense[ComplexDoubleElement],
    ) -> _ComplexArray: ...
    @overload
    def numpy(self) -> _NumpyArray: ...
    def _replace_self_with_numpy(
        self,
        numpy_matrix: _NumpyArray,
    ) -> None: ...
