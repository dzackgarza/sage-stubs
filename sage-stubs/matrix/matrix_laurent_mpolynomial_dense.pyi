from collections.abc import Sequence
from typing import Self

from sage.matrix.matrix_generic_dense import Matrix_generic_dense
from sage.rings.polynomial.laurent_polynomial_mpair import LaurentPolynomial_mpair
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput, Parent


class Matrix_laurent_mpolynomial_dense(
    Matrix_generic_dense[LaurentPolynomial_mpair]
):
    def __init__(
        self,
        parent: Parent[Self],
        entries: Sequence[LaurentPolynomial_mpair | ElementConstructorInput]
        | ElementConstructorInput = ...,
        copy: bool = ...,
        coerce: bool = ...,
    ) -> None: ...
    def determinant(self, algorithm: str = ...) -> LaurentPolynomial_mpair: ...
    det = determinant
    def trace(self) -> LaurentPolynomial_mpair: ...
    def characteristic_polynomial(self, var: str = ...) -> Polynomial: ...
    charpoly = characteristic_polynomial
    def monomial_denominator(self) -> LaurentPolynomial_mpair: ...
