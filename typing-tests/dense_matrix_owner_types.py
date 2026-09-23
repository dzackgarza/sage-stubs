"""Dense matrix backends retain their source-owned call and result types."""

from collections.abc import Sequence
from typing import assert_type

from sage.matrix.matrix_cyclo_dense import Matrix_cyclo_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational


def integer_dense(matrix: Matrix_integer_dense) -> None:
    assert_type(matrix.row(0), FreeModuleElement[Integer])
    assert_type(matrix.charpoly(), Polynomial)
    assert_type(matrix.minpoly(algorithm="linbox"), Polynomial)
    assert_type(matrix.determinant(proof=False), Integer)
    assert_type(matrix.echelon_form(), Matrix_integer_dense)
    assert_type(
        matrix.echelon_form(
            algorithm="flint",
            proof=True,
            include_zero_rows=True,
            transformation=True,
        ),
        tuple[Matrix_integer_dense, Matrix_integer_dense],
    )
    assert_type(
        matrix.smith_form(),
        tuple[Matrix_integer_dense, Matrix_integer_dense, Matrix_integer_dense],
    )
    assert_type(matrix.inverse_of_unit(), Matrix_integer_dense)


def rational_dense(matrix: Matrix_rational_dense) -> None:
    assert_type(matrix.echelon_form(), Matrix_rational_dense)
    assert_type(matrix.charpoly(algorithm="flint"), Polynomial)
    assert_type(matrix.minpoly(algorithm="linbox"), Polynomial)
    assert_type(
        matrix.decomposition(),
        Sequence[tuple[FreeModule_generic[Rational], bool]],
    )


def cyclotomic_dense(matrix: Matrix_cyclo_dense) -> None:
    assert_type(matrix.charpoly(algorithm="pari", proof=False), Polynomial)
    assert_type(matrix.echelon_form(algorithm="classical"), Matrix_cyclo_dense)
