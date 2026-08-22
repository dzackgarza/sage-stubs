from collections.abc import Sequence
from typing import Literal, Self, overload

from sage.matrix.matrix import Matrix
from sage.matrix.matrix_generic_dense import Matrix_generic_dense
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import RingElement

type Degree = int | Integer
type DegreeData = Degree | list[Degree]
type ShiftData = Sequence[Degree] | FreeModuleElement[Integer] | None
type OrderData = Degree | list[Degree]
type InterpolationPoint = RingElement | int | Integer
type InterpolationPoints = (
    list[InterpolationPoint]
    | list[list[InterpolationPoint]]
)
type PolynomialVector = FreeModuleElement[Polynomial]


class Matrix_polynomial_dense(Matrix_generic_dense[Polynomial]):
    def _check_shift_dimension(
        self,
        shifts: ShiftData,
        row_wise: bool = ...,
    ) -> None: ...

    # Polynomial degree and coefficient structure
    def degree(self) -> int | Integer: ...
    def degree_matrix(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
    ) -> Matrix_integer_dense: ...
    def constant_matrix(self) -> Matrix[RingElement]: ...
    def is_constant(self) -> bool: ...
    def coefficient_matrix(
        self,
        d: DegreeData,
        row_wise: bool = ...,
    ) -> Matrix[RingElement]: ...
    def truncate(
        self,
        d: DegreeData,
        row_wise: bool = ...,
    ) -> Self: ...
    def shift(
        self,
        d: DegreeData,
        row_wise: bool = ...,
    ) -> Self: ...
    def reverse(
        self,
        degree: DegreeData | None = ...,
        row_wise: bool = ...,
        entry_wise: bool = ...,
    ) -> Self: ...

    # Truncated series inversion and linear solving
    def inverse_series_trunc(self, d: Degree) -> Self: ...

    @overload
    def solve_left_series_trunc(
        self,
        B: Self,
        d: Degree,
    ) -> Self: ...
    @overload
    def solve_left_series_trunc(
        self,
        B: PolynomialVector,
        d: Degree,
    ) -> PolynomialVector: ...

    @overload
    def solve_right_series_trunc(
        self,
        B: Self,
        d: Degree,
    ) -> Self: ...
    @overload
    def solve_right_series_trunc(
        self,
        B: PolynomialVector,
        d: Degree,
    ) -> PolynomialVector: ...

    # Shifted degrees and canonical pivot data
    def row_degrees(
        self,
        shifts: ShiftData = ...,
    ) -> list[int | Integer]: ...
    def column_degrees(
        self,
        shifts: ShiftData = ...,
    ) -> list[int | Integer]: ...
    def leading_matrix(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
    ) -> Matrix[RingElement]: ...
    def _is_empty_popov(
        self,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> bool: ...
    def is_reduced(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> bool: ...

    @overload
    def leading_positions(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        return_degree: Literal[False] = ...,
    ) -> list[int]: ...
    @overload
    def leading_positions(
        self,
        shifts: ShiftData,
        row_wise: bool,
        return_degree: Literal[True],
    ) -> tuple[list[int], list[int | Integer]]: ...
    @overload
    def leading_positions(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        return_degree: bool = ...,
    ) -> list[int] | tuple[list[int], list[int | Integer]]: ...

    def is_weak_popov(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        ordered: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> bool: ...
    def is_popov(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        up_to_permutation: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> bool: ...
    def is_hermite(
        self,
        row_wise: bool = ...,
        lower_echelon: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> bool: ...

    # Reduced, weak-Popov, Popov, and Hermite bases
    @overload
    def weak_popov_form(
        self,
        transformation: Literal[False] = ...,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        ordered: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> Self: ...
    @overload
    def weak_popov_form(
        self,
        transformation: Literal[True],
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        ordered: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> tuple[Self, Self]: ...
    @overload
    def weak_popov_form(
        self,
        transformation: bool = ...,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        ordered: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> Self | tuple[Self, Self]: ...

    @overload
    def _weak_popov_form(
        self,
        transformation: Literal[False] = ...,
        shifts: ShiftData = ...,
    ) -> None: ...
    @overload
    def _weak_popov_form(
        self,
        transformation: Literal[True],
        shifts: ShiftData = ...,
    ) -> Self: ...
    @overload
    def _weak_popov_form(
        self,
        transformation: bool = ...,
        shifts: ShiftData = ...,
    ) -> Self | None: ...

    @overload
    def popov_form(
        self,
        transformation: Literal[False] = ...,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> Self: ...
    @overload
    def popov_form(
        self,
        transformation: Literal[True],
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> tuple[Self, Self]: ...
    @overload
    def popov_form(
        self,
        transformation: bool = ...,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> Self | tuple[Self, Self]: ...

    @overload
    def reduced_form(
        self,
        transformation: Literal[False] | None = ...,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> Self: ...
    @overload
    def reduced_form(
        self,
        transformation: Literal[True],
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> tuple[Self, Self]: ...
    @overload
    def reduced_form(
        self,
        transformation: bool | None = ...,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        include_zero_vectors: bool = ...,
    ) -> Self | tuple[Self, Self]: ...

    @overload
    def hermite_form(
        self,
        include_zero_rows: bool = ...,
        transformation: Literal[False] = ...,
    ) -> Self: ...
    @overload
    def hermite_form(
        self,
        include_zero_rows: bool,
        transformation: Literal[True],
    ) -> tuple[Self, Self]: ...
    @overload
    def hermite_form(
        self,
        include_zero_rows: bool = ...,
        transformation: bool = ...,
    ) -> Self | tuple[Self, Self]: ...

    # Polynomial matrix quotient, remainder, and normal form
    def left_quo_rem(self, B: Self) -> tuple[Self, Self]: ...
    def right_quo_rem(self, B: Self) -> tuple[Self, Self]: ...
    def _right_quo_rem_reduced(
        self,
        B: Self,
    ) -> tuple[Self, Self]: ...
    def _right_quo_rem_solve(
        self,
        B: Self,
    ) -> tuple[Self, Self]: ...

    @overload
    def reduce(
        self,
        B: Self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        return_quotient: Literal[False] = ...,
    ) -> Self: ...
    @overload
    def reduce(
        self,
        B: Self,
        shifts: ShiftData,
        row_wise: bool,
        return_quotient: Literal[True],
    ) -> tuple[Self, Self]: ...
    @overload
    def reduce(
        self,
        B: Self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        return_quotient: bool = ...,
    ) -> Self | tuple[Self, Self]: ...

    # Approximant and interpolant bases
    def is_minimal_approximant_basis(
        self,
        pmat: Self,
        order: OrderData,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        normal_form: bool = ...,
    ) -> bool: ...
    def minimal_approximant_basis(
        self,
        order: OrderData,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        normal_form: bool = ...,
    ) -> Self: ...
    def _approximant_basis_iterative(
        self,
        order: list[Degree],
        shifts: Sequence[Degree],
    ) -> tuple[Self, list[int | Integer]]: ...
    def minimal_interpolant_basis(
        self,
        points: InterpolationPoints,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        normal_form: bool = ...,
    ) -> Self: ...
    def _interpolant_basis_iterative(
        self,
        points: list[list[InterpolationPoint]],
        shifts: Sequence[Degree],
    ) -> tuple[Self, list[int | Integer]]: ...

    # Minimal kernel and relation bases
    def is_minimal_kernel_basis(
        self,
        pmat: Self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        normal_form: bool = ...,
    ) -> bool: ...
    def minimal_kernel_basis(
        self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        normal_form: bool = ...,
    ) -> Self: ...
    def minimal_relation_basis(
        self,
        mod: Self,
        shifts: ShiftData = ...,
        row_wise: bool = ...,
        normal_form: bool = ...,
        reduced_input: bool = ...,
    ) -> Self: ...

    # Smith-form-preserving completion
    def _basis_completion_via_reversed_approx(self) -> Self: ...
    def basis_completion(
        self,
        row_wise: bool = ...,
        algorithm: Literal["approximant", "smith"] = ...,
    ) -> Self: ...
    def _is_basis_completion(
        self,
        mat: Self,
        row_wise: bool = ...,
    ) -> bool: ...
