"""Polynomial wrappers retain the selected backend's call and result types."""

from typing import assert_type

from sage.matrix.matrix2 import Matrix
from sage.matrix.matrix_cyclo_dense import Matrix_cyclo_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial


def polynomial_dispatch(
    generic: Matrix[Integer],
    integers: Matrix_integer_dense,
    rationals: Matrix_rational_dense,
    cyclotomic: Matrix_cyclo_dense,
) -> None:
    assert_type(generic.charpoly("t", algorithm="df"), Polynomial)
    assert_type(generic.characteristic_polynomial("t", algorithm="df"), Polynomial)
    assert_type(Matrix.characteristic_polynomial(integers, "t", "flint"), Polynomial)
    assert_type(
        Matrix.characteristic_polynomial(rationals, var="t", algorithm="flint"),
        Polynomial,
    )
    assert_type(cyclotomic.characteristic_polynomial("t", "pari", True), Polynomial)
    assert_type(
        Matrix.characteristic_polynomial(
            cyclotomic, var="t", algorithm="pari", proof=True
        ),
        Polynomial,
    )
    assert_type(
        Matrix.minimal_polynomial(integers, "t", algorithm="linbox"), Polynomial
    )
    assert_type(
        Matrix.minimal_polynomial(rationals, "t", algorithm="linbox"), Polynomial
    )
    assert_type(
        Matrix.minimal_polynomial(cyclotomic, "t", algorithm="pari", proof=True),
        Polynomial,
    )
