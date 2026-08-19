from sage.matrix.matrix_generic_dense import Matrix_generic_dense
from sage.matrix.matrix_mpolynomial_dense import Matrix_mpolynomial_dense
from sage.rings.ideal import Ideal_generic
from sage.rings.polynomial.laurent_polynomial_mpair import LaurentPolynomial_mpair


class Matrix_laurent_mpolynomial_dense(
    Matrix_generic_dense[LaurentPolynomial_mpair]
):
    def laurent_matrix_reduction(
        self,
    ) -> tuple[
        Matrix_laurent_mpolynomial_dense,
        Matrix_mpolynomial_dense,
        Matrix_laurent_mpolynomial_dense,
    ]: ...
    def _fitting_ideal(
        self,
        i: int,
    ) -> Ideal_generic: ...
