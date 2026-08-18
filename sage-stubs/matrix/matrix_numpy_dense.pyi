from types import ModuleType
from typing import Self, TypeVar

import numpy as np
from numpy.typing import DTypeLike, NDArray

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.structure.element import Element, RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

numpy: ModuleType | None
scipy: ModuleType | None

class Matrix_numpy_dense(Matrix_dense[_Scalar]):
    def __create_matrix__(self) -> None: ...
    def __init__(
        self,
        parent: MatrixSpace,
        entries: Element | list[Element] | tuple[Element, ...] | None = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def transpose(self) -> Self: ...
    def is_symmetric(self, tol: float = ...) -> bool: ...
    def _is_lower_triangular(self, tol: float) -> bool: ...
    def numpy(self, dtype: DTypeLike | None = ...) -> NDArray[np.generic]: ...
    def _replace_self_with_numpy(
        self,
        numpy_matrix: NDArray[np.generic],
    ) -> None: ...
