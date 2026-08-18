from typing import TypeVar

from numpy import ndarray

from sage.matrix.matrix import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


def vector_to_numpy(
    vector: FreeModuleElement[_Scalar],
    dtype: object | None = ...,
    copy: bool = ...,
) -> ndarray: ...


def matrix_to_numpy(
    matrix: Matrix[_Scalar],
    dtype: object | None = ...,
    copy: bool = ...,
) -> ndarray: ...


def numpy_to_vector(
    array: ndarray,
    ring: Parent[_Scalar] | None = ...,
) -> FreeModuleElement[_Scalar]: ...


def numpy_to_matrix(
    array: ndarray,
    ring: Parent[_Scalar] | None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...
