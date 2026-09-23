"""Generic owners preserve coefficient types and native determinant dispatch."""

from typing import assert_type

from sage.matrix.matrix2 import Matrix
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.modules.free_module import FreeModule_generic
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.parent import Parent


def generic_owners(
    integers: Matrix[Integer],
    rationals: Matrix[Rational],
    rational_parent: Parent[Rational],
) -> None:
    assert_type(integers.rank(), int)
    assert_type(integers.determinant(), Integer)
    assert_type(integers.det(), Integer)
    assert_type(rationals.det(algorithm="df"), Rational)
    assert_type(integers.row_module(), FreeModule_generic[Integer])
    assert_type(integers.row_space(), FreeModule_generic[Integer])
    assert_type(integers.row_module(rational_parent), FreeModule_generic[Rational])
    assert_type(integers.row_space(base_ring=rational_parent), FreeModule_generic[Rational])
    assert_type(integers.column_module(), FreeModule_generic[Integer])
    assert_type(integers.column_space(), FreeModule_generic[Integer])


def native_dispatch(rationals: Matrix_rational_dense) -> None:
    # The unbound base wrapper must retain the concrete backend's keyword
    # arguments and result, not the generic determinant's smaller signature.
    assert_type(Matrix.det(rationals, algorithm="pari", proof=True), Rational)
