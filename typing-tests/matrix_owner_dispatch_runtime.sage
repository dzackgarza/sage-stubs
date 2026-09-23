"""Complete native consumers for generic owners and backend dispatch."""

from sage.matrix.matrix0 import Matrix as Matrix0
from sage.matrix.matrix2 import Matrix as Matrix2


integers = matrix(ZZ, [[2, 0], [0, 3]])
rationals = integers.change_ring(QQ)

assert "rank" in Matrix0.__dict__
assert "rank" not in Matrix2.__dict__
assert Matrix0.rank(integers) == 2
assert Matrix2.det is not Matrix2.determinant
assert Matrix2.row_space is not Matrix2.row_module
assert Matrix2.column_space is not Matrix2.column_module

assert Matrix2.determinant(integers) == 6
assert Matrix2.det(integers, algorithm="flint", proof=True) == 6
assert Matrix2.det(rationals, algorithm="pari", proof=True) == 6
assert Matrix2.det(integers).parent() is ZZ
assert Matrix2.det(rationals).parent() is QQ

integer_rows = Matrix2.row_space(integers)
rational_rows = Matrix2.row_space(integers, base_ring=QQ)
assert integer_rows.base_ring() is ZZ
assert rational_rows.base_ring() is QQ
assert integer_rows == Matrix2.row_module(integers)
assert rational_rows == Matrix2.row_module(integers, base_ring=QQ)
assert vector(ZZ, [1, 0]) not in integer_rows
assert vector(QQ, [1, 0]) in rational_rows

for method in (Matrix2.column_module, Matrix2.column_space):
    columns = method(integers)
    assert columns.base_ring() is ZZ
    assert columns == integers.transpose().row_module()
    try:
        method(integers, base_ring=QQ)
    except TypeError:
        pass
    else:
        raise AssertionError("column-space methods do not accept base_ring")

try:
    Matrix2.determinant(integers, proof=True)
except TypeError:
    pass
else:
    raise AssertionError("proof is a backend option, not a generic determinant argument")

try:
    Matrix0.rank(integers, algorithm="modp")
except TypeError:
    pass
else:
    raise AssertionError("the generic rank method takes no algorithm argument")
