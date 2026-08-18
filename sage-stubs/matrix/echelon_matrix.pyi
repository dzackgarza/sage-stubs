from collections.abc import Iterator
from typing import TypeVar

from sage.matrix.matrix import Matrix
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement)


def reduced_echelon_matrix_iterator(
    K: Parent[_Scalar],
    k: int | Integer,
    n: int | Integer,
    sparse: bool = ...,
    copy: bool = ...,
    set_immutable: bool = ...,
) -> Iterator[Matrix[_Scalar]]: ...
