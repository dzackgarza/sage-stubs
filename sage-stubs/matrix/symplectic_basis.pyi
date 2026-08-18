from typing import TypeVar

from sage.matrix.matrix0 import Matrix
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

def symplectic_basis_over_field(
    M: Matrix[_Scalar],
) -> tuple[Matrix[_Scalar], Matrix[_Scalar]]: ...
def symplectic_basis_over_ZZ(
    M: Matrix[_Scalar],
) -> tuple[Matrix[_Scalar], Matrix[_Scalar]]: ...
