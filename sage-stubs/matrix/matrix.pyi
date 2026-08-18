from typing import Generic, TypeVar

from sage.matrix.matrix2 import Matrix as Matrix2
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Matrix(Matrix2[_Scalar], Generic[_Scalar]):
    pass
