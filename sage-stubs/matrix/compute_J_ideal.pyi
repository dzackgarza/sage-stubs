from collections.abc import Sequence

from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.rings.fraction_field_element import FractionFieldElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.sage_object import SageObject


def lifting(
    p: Integer,
    t: int | Integer,
    A: Matrix_polynomial_dense,
    G: Matrix_polynomial_dense | None,
) -> Matrix_polynomial_dense: ...


def p_part(
    f: Polynomial,
    p: Integer,
) -> Polynomial: ...


class ComputeMinimalPolynomials(SageObject):
    B: Matrix_integer_dense
    chi_B: Polynomial
    mu_B: Polynomial

    def __init__(self, B: Matrix_integer_dense) -> None: ...
    def find_monic_replacements(
        self,
        p: Integer,
        t: int | Integer,
        pt_generators: Sequence[Polynomial],
        prev_nu: Polynomial,
    ) -> list[Polynomial]: ...
    def current_nu(
        self,
        p: Integer,
        t: int | Integer,
        pt_generators: Sequence[Polynomial],
        prev_nu: Polynomial,
    ) -> Polynomial: ...
    def mccoy_column(
        self,
        p: Integer,
        t: int | Integer,
        nu: Polynomial,
    ) -> Matrix_polynomial_dense: ...
    def p_minimal_polynomials(
        self,
        p: Integer,
        s_max: int | Integer | None = ...,
    ) -> dict[int, Polynomial]: ...
    def null_ideal(
        self,
        b: int | Integer = ...,
    ) -> Ideal_generic: ...
    def prime_candidates(self) -> list[Integer]: ...
    def integer_valued_polynomials_generators(
        self,
    ) -> tuple[
        Polynomial,
        list[Polynomial | FractionFieldElement],
    ]: ...


from sage.matrix.matrix_polynomial_dense import Matrix_polynomial_dense
