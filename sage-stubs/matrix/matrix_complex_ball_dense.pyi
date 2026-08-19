from collections.abc import Callable, Mapping, Sequence
from typing import Literal, Self

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.complex_arb import ComplexBall
from sage.rings.polynomial.polynomial_complex_arb import Polynomial_complex_arb
from sage.structure.parent import ElementConstructorInput

type ComplexBallMatrixEntries = (
    ComplexBall
    | Sequence[ComplexBall | ElementConstructorInput]
    | Sequence[Sequence[ComplexBall | ElementConstructorInput]]
    | Mapping[tuple[int, int], ComplexBall | ElementConstructorInput]
    | Callable[[int, int], ComplexBall | ElementConstructorInput]
    | ElementConstructorInput
    | None
)
type ComplexBallEigenvector = tuple[
    ComplexBall,
    list[FreeModuleElement[ComplexBall]],
    Literal[1],
]


class Matrix_complex_ball_dense(Matrix_dense[ComplexBall]):
    def __init__(
        self,
        parent: MatrixSpace[ComplexBall],
        entries: ComplexBallMatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[ComplexBall]: ...
    def list(self) -> list[ComplexBall]: ...
    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[ComplexBall]: ...
    def column(
        self,
        j: int,
        from_list: bool = ...,
    ) -> FreeModuleElement[ComplexBall]: ...

    # Set-theoretic ball relations
    def identical(self, other: Self) -> bool: ...
    def overlaps(self, other: Self) -> bool: ...
    def contains(self, other: Self) -> bool: ...

    # Arithmetic and linear algebra
    def __neg__(self) -> Self: ...
    def _add_(self, other: Self) -> Self: ...
    def _sub_(self, other: Self) -> Self: ...
    def _lmul_(self, scalar: ComplexBall) -> Self: ...
    def _rmul_(self, scalar: ComplexBall) -> Self: ...
    def _multiply_classical(self, other: Self) -> Self: ...
    def _pow_int(self, n: int) -> Self: ...
    def __invert__(self) -> Self: ...
    inverse = __invert__
    def transpose(self) -> Self: ...
    def _solve_right_nonsingular_square(
        self,
        rhs: Self,
        check_rank: bool | None = ...,
    ) -> Self: ...
    def solve_right(
        self,
        B: Self | FreeModuleElement[ComplexBall],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> Self | FreeModuleElement[ComplexBall]: ...
    def solve_left(
        self,
        B: Self | FreeModuleElement[ComplexBall],
        check: bool = ...,
        *,
        extend: bool = ...,
    ) -> Self | FreeModuleElement[ComplexBall]: ...

    # Certified invariants and spectral enclosures
    def determinant(self) -> ComplexBall: ...
    det = determinant
    def trace(self) -> ComplexBall: ...
    def charpoly(
        self,
        var: str = ...,
        algorithm: str | None = ...,
    ) -> Polynomial_complex_arb: ...
    characteristic_polynomial = charpoly
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
