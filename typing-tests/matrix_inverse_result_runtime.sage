"""Native generic and dense inversion retain the actual coefficient rings."""

from sage.matrix.matrix0 import Matrix as Matrix0
from sage.matrix.matrix2 import Matrix as Matrix2
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense

from sage.structure.element import Element
from sage.structure.parent import Parent

assert Element(Parent()).base_ring() is None

integral = matrix(ZZ, [[2, 1], [0, 1]], sparse=False)
assert isinstance(integral, Matrix_integer_dense)
assert integral[0, 0] == 2
assert integral[0].parent().base_ring() is ZZ
assert integral[0, :] == matrix(ZZ, [[2, 1]])
assert integral[:, 0] == matrix(ZZ, [[2], [0]])
assert integral[:, :] == integral
assert integral[range(2), (0, 1)] == integral
expected = matrix(QQ, [[1/2, -1/2], [0, 1]], sparse=False)
for inverse in (~integral, integral.inverse(), Matrix2.inverse(integral), integral**-1):
    assert isinstance(inverse, Matrix_rational_dense)
    assert inverse.base_ring() is QQ
    assert inverse == expected
    assert inverse * integral == identity_matrix(QQ, 2)
    assert integral * inverse == identity_matrix(QQ, 2)
assert (integral**2).base_ring() is ZZ

rational = integral.change_ring(QQ)
assert rational.inverse(algorithm="flint") == expected
assert Matrix0.__invert__(rational) == expected

# Generic source behavior for the empty matrix must not be inferred from
# the specialized integer backend: the former returns its argument unchanged.
empty_integral = matrix(ZZ, 0, 0, sparse=False)
assert Matrix0.__invert__(empty_integral) is empty_integral
assert (~empty_integral).base_ring() is QQ

polynomials = PolynomialRing(QQ, "t")
t = polynomials.gen()
polynomial_matrix = matrix(polynomials, [[t, 1], [0, 1]], sparse=False)
polynomial_inverse = Matrix0.__invert__(polynomial_matrix)
assert polynomial_inverse.base_ring() is polynomials.fraction_field()
assert polynomial_inverse[0, 0] == 1/t
assert polynomial_inverse * polynomial_matrix == identity_matrix(polynomials.fraction_field(), 2)

# Over a ring with zero divisors the generic implementation takes the
# same-ring inverse_of_unit route, not a nonexistent fraction field.
residues = Zmod(2**100)
modular = matrix(residues, [[2, 1], [1, 1]], sparse=False)
modular_inverse = Matrix0.__invert__(modular)
assert modular_inverse.parent() is modular.parent()
assert modular_inverse * modular == identity_matrix(residues, 2)
assert modular * modular_inverse == identity_matrix(residues, 2)
print("PASS: integral, rational, polynomial, empty, and non-domain inverse coefficients")
