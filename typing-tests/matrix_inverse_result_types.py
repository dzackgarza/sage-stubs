"""Inversion and integral powers preserve coefficient changes and source owners."""

from typing import assert_type

from sage.matrix.matrix0 import Matrix as Matrix0
from sage.matrix.matrix2 import Matrix as Matrix2
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.parent import Parent


def generic_inverse_types(
    integral: Matrix0[Integer],
    rational: Matrix0[Rational],
    scalar: RingElement,
) -> None:
    assert_type(~scalar, RingElement)
    assert_type(integral.base_ring(), Parent[Integer])
    assert_type(integral[0, 0], Integer)
    assert_type(integral[0], FreeModuleElement[Integer])
    assert_type(integral[0, :], Matrix0[Integer])
    assert_type(integral[:, 0], Matrix0[Integer])
    assert_type(integral[:, :], Matrix0[Integer])
    assert_type(integral[range(2), (0, 1)], Matrix0[Integer])
    # The generic implementation returns the original empty matrix; a
    # nonempty integral matrix instead has rational inverse coefficients.
    assert_type(~integral, Matrix0[Integer] | Matrix0[Rational])
    assert_type(~rational, Matrix0[Rational])
    assert_type(integral**2, Matrix0[Integer] | Matrix0[Rational])
    assert_type(integral**-1, Matrix0[Integer] | Matrix0[Rational])
    assert_type(rational**-1, Matrix0[Rational])


def dense_inverse_types(
    integral: Matrix_integer_dense,
    rational: Matrix_rational_dense,
) -> None:
    assert_type(~integral, Matrix_rational_dense)
    assert_type(~rational, Matrix_rational_dense)
    assert_type(Matrix2.inverse(integral), Matrix_rational_dense)
    assert_type(Matrix2.inverse(rational), Matrix_rational_dense)
    assert_type(integral.inverse(), Matrix_rational_dense)
    assert_type(rational.inverse(algorithm="flint"), Matrix_rational_dense)
    assert_type(integral**-1, Matrix_integer_dense | Matrix_rational_dense)
