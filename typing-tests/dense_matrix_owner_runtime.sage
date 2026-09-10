"""Native dense backends preserve their direct method semantics."""

from sage.matrix.matrix_cyclo_dense import Matrix_cyclo_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense

integers = matrix(ZZ, [[2, 1], [0, 1]], sparse=False)
assert isinstance(integers, Matrix_integer_dense)
assert integers.charpoly() == integers.characteristic_polynomial()
assert integers.minpoly() == integers.minimal_polynomial()
assert integers.determinant(proof=False) == 2
H, U = integers.echelon_form(algorithm="flint", transformation=True)
assert U * integers == H
S, L, R = integers.smith_form()
assert L * integers * R == S
unit = matrix(ZZ, [[2, 1], [1, 1]], sparse=False)
assert unit.inverse_of_unit() * unit == identity_matrix(ZZ, 2)

rationals = integers.change_ring(QQ)
assert isinstance(rationals, Matrix_rational_dense)
assert rationals.echelon_form().base_ring() is QQ
assert rationals.charpoly(algorithm="flint") == rationals.characteristic_polynomial(
    algorithm="flint"
)
assert rationals.minpoly(algorithm="linbox") == rationals.minimal_polynomial(
    algorithm="linbox"
)

K.<z> = CyclotomicField(5)
cyclotomic = MatrixSpace(K, 2)([1, z, 0, 1])
assert isinstance(cyclotomic, Matrix_cyclo_dense)
assert cyclotomic.charpoly(algorithm="pari") == cyclotomic.characteristic_polynomial(
    algorithm="pari"
)
assert cyclotomic.echelon_form(algorithm="classical").base_ring() is K
assert cyclotomic._pickle()[1] == 0

print("PASS: integer, rational, and cyclotomic dense owners")
