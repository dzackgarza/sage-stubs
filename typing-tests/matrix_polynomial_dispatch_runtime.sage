"""Native polynomial forwarding, multiplicity, coefficient rings, and call shape."""

from sage.matrix.matrix2 import Matrix
from sage.matrix.matrix_cyclo_dense import Matrix_cyclo_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense

integers = diagonal_matrix(ZZ, [2, 2, 3], sparse=False)
rationals = diagonal_matrix(QQ, [1/2, 1/2, 3], sparse=False)
cyclotomic_field = CyclotomicField(5)
zeta = cyclotomic_field.gen()
cyclotomic = diagonal_matrix(cyclotomic_field, [zeta, zeta, 1], sparse=False)
assert isinstance(integers, Matrix_integer_dense)
assert isinstance(rationals, Matrix_rational_dense)
assert isinstance(cyclotomic, Matrix_cyclo_dense)

for A, repeated, other, characteristic_algorithm, minimal_algorithm in (
    (integers, ZZ(2), ZZ(3), "flint", "linbox"),
    (rationals, QQ(1/2), QQ(3), "flint", "linbox"),
    (cyclotomic, zeta, cyclotomic_field(1), "pari", "pari"),
):
    polynomials = PolynomialRing(A.base_ring(), "t")
    t = polynomials.gen()
    characteristic = (t - repeated)**2 * (t - other)
    minimal = (t - repeated) * (t - other)
    assert Matrix.characteristic_polynomial(A, "t", characteristic_algorithm) == characteristic
    assert A.characteristic_polynomial(var="t", algorithm=characteristic_algorithm) == characteristic
    assert Matrix.minimal_polynomial(A, "t", algorithm=minimal_algorithm) == minimal
    assert A.minimal_polynomial(var="t", algorithm=minimal_algorithm) == minimal
    assert A.charpoly("t", characteristic_algorithm).parent().base_ring() is A.base_ring()
    assert A.minpoly("t", algorithm=minimal_algorithm).parent().base_ring() is A.base_ring()
    assert characteristic(A) == A.parent().zero()
    assert minimal(A) == A.parent().zero()

    # The long name accepts only var positionally, unlike the integer and
    # rational minpoly implementations. It must not be modeled as their alias.
    try:
        Matrix.minimal_polynomial(A, "t", minimal_algorithm)
    except TypeError:
        pass
    else:
        raise AssertionError("minimal_polynomial accepted a second positional argument")

expected = (PolynomialRing(cyclotomic_field, "u").gen() - zeta)**2 * (
    PolynomialRing(cyclotomic_field, "u").gen() - 1
)
assert Matrix.characteristic_polynomial(cyclotomic, "u", "pari", True) == expected
assert cyclotomic.characteristic_polynomial("u", algorithm="pari", proof=True) == expected
print("PASS: matrix polynomial forwarding, distinct minimal polynomial, and native argument shapes")
