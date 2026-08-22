from typing import TypeVar

from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement)


def berlekamp_massey(
    a: list[_Scalar | int] | tuple[_Scalar | int, ...],
) -> Polynomial: ...
