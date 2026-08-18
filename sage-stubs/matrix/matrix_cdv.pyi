from typing import TypeVar

from sage.matrix.matrix_generic_dense import Matrix_generic_dense
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

def hessenbergize_cdvf(H: Matrix_generic_dense[_Scalar]) -> None: ...
