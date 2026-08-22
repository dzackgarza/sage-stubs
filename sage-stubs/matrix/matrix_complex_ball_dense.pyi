from collections.abc import Sequence
from typing import Literal, Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.complex_arb import ComplexBall
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_complex_arb import Polynomial_complex_arb


type ComplexBallEigenvector = tuple[
    ComplexBall,
    list[FreeModuleElement[ComplexBall]],
    Literal[1],
]


class Matrix_complex_ball_dense(Matrix_dense[ComplexBall]):
    def __init__(
        self,
        parent: MatrixSpace[ComplexBall],
        entries: MatrixData[ComplexBall] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def _richcmp_(
        self,
        right: Self,
        op: int,
    ) -> bool: ...
    def identical(self, other: Self) -> bool: ...
    def overlaps(self, other: Self) -> bool: ...
    def contains(self, other: Self) -> bool: ...
    def __neg__(self) -> Self: ...
    def _add_(self, other: Self) -> Self: ...
    def _sub_(self, other: Self) -> Self: ...
    def _lmul_(self, scalar: ComplexBall) -> Self: ...
    def _rmul_(self, scalar: ComplexBall) -> Self: ...
    def _pow_int(self, n: int | Integer) -> Self: ...
    def __invert__(self) -> Self: ...
    def transpose(self) -> Self: ...
    def _solve_right_nonsingular_square(
        self,
        rhs: Self,
        check_rank: bool | None = ...,
    ) -> Self: ...
    def determinant(self) -> ComplexBall: ...
    def trace(self) -> ComplexBall: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial_complex_arb: ...
    def eigenvalues(
        self,
        other: Self | None = ...,
        *,
        extend: bool | None = ...,
    ) -> Sequence[ComplexBall]: ...
    def eigenvectors_right_approx(
        self,
        other: Self | None = ...,
        *,
        extend: bool | None = ...,
    ) -> list[ComplexBallEigenvector]: ...
    def eigenvectors_right(
        self,
        other: Self | None = ...,
        *,
        extend: bool | None = ...,
    ) -> list[ComplexBallEigenvector]: ...
    def eigenvectors_left_approx(
        self,
        other: Self | None = ...,
        *,
        extend: bool | None = ...,
    ) -> list[ComplexBallEigenvector]: ...
    def eigenvectors_left(
        self,
        other: Self | None = ...,
        *,
        extend: bool = ...,
    ) -> list[ComplexBallEigenvector]: ...
    def exp(self) -> Self: ...
