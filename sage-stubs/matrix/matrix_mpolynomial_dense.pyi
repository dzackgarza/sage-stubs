from typing import Literal, Self, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_generic_dense import Matrix_generic_dense
from sage.rings.fraction_field_element import FractionFieldElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.multi_polynomial import MPolynomial


type MPolynomialEchelonAlgorithm = Literal[
    "row_reduction",
    "bareiss",
]


class Matrix_mpolynomial_dense(Matrix_generic_dense[MPolynomial]):
    @overload
    def echelon_form(
        self,
        algorithm: Literal["frac"],
        **kwds: object,
    ) -> Matrix[FractionFieldElement]: ...
    @overload
    def echelon_form(
        self,
        algorithm: MPolynomialEchelonAlgorithm = ...,
        **kwds: object,
    ) -> Self: ...
    @overload
    def echelon_form(
        self,
        algorithm: str = ...,
        **kwds: object,
    ) -> Matrix[FractionFieldElement] | Self: ...
    def pivots(self) -> tuple[int, ...]: ...
    def echelonize(
        self,
        algorithm: MPolynomialEchelonAlgorithm = ...,
        **kwds: object,
    ) -> None: ...
    def _echelonize_gauss_bareiss(self) -> None: ...
    def _echelonize_row_reduction(self) -> None: ...
    def swapped_columns(
        self,
    ) -> tuple[int | Integer, ...] | None: ...
    def _fitting_ideal(
        self,
        i: int | Integer,
    ) -> Ideal_generic: ...
    def determinant(
        self,
        algorithm: str | None = ...,
    ) -> MPolynomial: ...
