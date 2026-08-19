from typing import TypeVar

from sage.matrix.matrix0 import Matrix
from sage.rings.integer import Integer
from sage.structure.element import FieldElement

_FieldScalar = TypeVar(
    "_FieldScalar",
    bound=FieldElement,
    default=FieldElement,
)


def symplectic_basis_over_field(
    M: Matrix[_FieldScalar],
) -> tuple[Matrix[_FieldScalar], Matrix[_FieldScalar]]: ...


def symplectic_basis_over_ZZ(
    M: Matrix[Integer],
) -> tuple[Matrix[Integer], Matrix[Integer]]: ...
