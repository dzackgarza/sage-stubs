from collections.abc import Sequence
from typing import TypeVar

from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational

_FiniteElement = TypeVar(
    "_FiniteElement",
    bound=FiniteRingElement,
)


def lfsr_sequence(
    key: list[_FiniteElement],
    fill: list[_FiniteElement],
    n: int | Integer,
) -> list[_FiniteElement]: ...


def lfsr_autocorrelation(
    L: list[int | Integer | FiniteRingElement],
    p: int | Integer,
    k: int | Integer,
) -> Rational: ...


def lfsr_connection_polynomial(
    s: Sequence[_FiniteElement],
) -> Polynomial: ...
