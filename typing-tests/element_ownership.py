"""Native element parents and matrix scalar outputs retain their own types."""

from typing import assert_type

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import (
    Element,
    Matrix,
    MultiplicativeGroupElement,
    RingElement,
)
from sage.structure.parent import Parent


def element_parents(
    element: Element,
    multiplicative: MultiplicativeGroupElement,
    ring_element: RingElement,
) -> None:
    assert_type(element.parent(), Parent[Element])
    assert_type(multiplicative.parent(), Parent[MultiplicativeGroupElement])
    assert_type(ring_element.parent(), Parent[RingElement])


def integer_matrix_arithmetic(matrix: Matrix[Integer], scalar: Integer) -> None:
    assert_type(matrix * scalar, Matrix[Integer])
    assert_type(scalar * matrix, Matrix[Integer])
    assert_type(2 * matrix, Matrix[Integer])
    assert_type(matrix / scalar, Matrix[Rational])
