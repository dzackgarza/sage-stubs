from collections.abc import Callable, Iterable, ItemsView, Iterator, Mapping, Sequence
from typing import Generic, Literal, Self, TypeVar, overload

from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.structure.element import Matrix as MatrixElement
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)
_OtherScalar = TypeVar("_OtherScalar", bound=RingElement)
_Polynomial = TypeVar("_Polynomial", bound=RingElement)

type _MatrixAxisIndex = int | Integer
type _MatrixIndexCollection = (
    list[_MatrixAxisIndex]
    | tuple[_MatrixAxisIndex, ...]
    | range
)
type _MatrixAxisSelection = _MatrixAxisIndex | slice | _MatrixIndexCollection
type _MatrixSingleSelection = _MatrixAxisIndex | slice | list[_MatrixAxisIndex]
type _MatrixEntryKey = tuple[_MatrixAxisIndex, _MatrixAxisIndex]
type _MatrixSelectionKey = (
    _MatrixSingleSelection
    | tuple[_MatrixAxisSelection, _MatrixAxisSelection]
)
type _MatrixAssignment = (
    ElementConstructorInput
    | Sequence[Sequence[ElementConstructorInput]]
)
type _EntryFormatter[_T: RingElement] = Mapping[_T, str] | Callable[[_T], str]
type _BorderLabels = Sequence[object] | None


class Matrix(MatrixElement[_Scalar], Generic[_Scalar]):
    def list(self) -> list[_Scalar]: ...
    def dense_coefficient_list(
        self,
        order: Iterable[_MatrixEntryKey] | None = ...,
    ) -> list[_Scalar]: ...
    def dict(self, copy: bool = ...) -> dict[tuple[int, int], _Scalar]: ...
    monomial_coefficients = dict
    def items(self) -> ItemsView[tuple[int, int], _Scalar]: ...

    def set_immutable(self) -> None: ...
    def is_immutable(self) -> bool: ...
    def is_mutable(self) -> bool: ...

    def add_to_entry(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        elt: ElementConstructorInput,
    ) -> None: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...
    @overload
    def __getitem__(self, key: _MatrixEntryKey) -> _Scalar: ...
    @overload
    def __getitem__(self, key: _MatrixAxisIndex) -> FreeModuleElement[_Scalar]: ...
    @overload
    def __getitem__(
        self,
        key: slice | list[_MatrixAxisIndex],
    ) -> Self: ...
    @overload
    def __getitem__(
        self,
        key: tuple[_MatrixAxisSelection, _MatrixAxisSelection],
    ) -> Self: ...
    def __setitem__(self, key: _MatrixSelectionKey, value: _MatrixAssignment) -> None: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Self],
        tuple[
            type[Self],
            Parent[Self],
            bool,
            dict[str, object] | None,
            object,
            int,
        ],
    ]: ...

    def base_ring(self) -> Parent[_Scalar]: ...
    def change_ring(self, ring: Parent[_NewScalar]) -> Matrix[_NewScalar]: ...
    @overload
    def _matrix_(self, R: None = ...) -> Self: ...
    @overload
    def _matrix_(self, R: Parent[_NewScalar]) -> Matrix[_NewScalar]: ...

    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    @overload
    def str(
        self,
        rep_mapping: _EntryFormatter[_Scalar] | None = ...,
        zero: str | None = ...,
        plus_one: str | None = ...,
        minus_one: str | None = ...,
        *,
        unicode: bool = ...,
        shape: Literal["square", "round"] | None = ...,
        character_art: Literal[False] = ...,
        left_border: _BorderLabels = ...,
        right_border: _BorderLabels = ...,
        top_border: _BorderLabels = ...,
        bottom_border: _BorderLabels = ...,
    ) -> str: ...
    @overload
    def str(
        self,
        rep_mapping: _EntryFormatter[_Scalar] | None = ...,
        zero: str | None = ...,
        plus_one: str | None = ...,
        minus_one: str | None = ...,
        *,
        unicode: Literal[False] = ...,
        shape: Literal["square", "round"] | None = ...,
        character_art: Literal[True],
        left_border: _BorderLabels = ...,
        right_border: _BorderLabels = ...,
        top_border: _BorderLabels = ...,
        bottom_border: _BorderLabels = ...,
    ) -> AsciiArt: ...
    @overload
    def str(
        self,
        rep_mapping: _EntryFormatter[_Scalar] | None = ...,
        zero: str | None = ...,
        plus_one: str | None = ...,
        minus_one: str | None = ...,
        *,
        unicode: Literal[True],
        shape: Literal["square", "round"] | None = ...,
        character_art: Literal[True],
        left_border: _BorderLabels = ...,
        right_border: _BorderLabels = ...,
        top_border: _BorderLabels = ...,
        bottom_border: _BorderLabels = ...,
    ) -> UnicodeArt: ...
    @overload
    def str(
        self,
        rep_mapping: _EntryFormatter[_Scalar] | None = ...,
        zero: str | None = ...,
        plus_one: str | None = ...,
        minus_one: str | None = ...,
        *,
        unicode: bool = ...,
        shape: Literal["square", "round"] | None = ...,
        character_art: bool = ...,
        left_border: _BorderLabels = ...,
        right_border: _BorderLabels = ...,
        top_border: _BorderLabels = ...,
        bottom_border: _BorderLabels = ...,
    ) -> str | AsciiArt | UnicodeArt: ...
    def _ascii_art_(self) -> AsciiArt: ...
    def _unicode_art_(self) -> UnicodeArt: ...
    def _latex_(self) -> str: ...

    def ncols(self) -> int: ...
    def nrows(self) -> int: ...
    def dimensions(self) -> tuple[int, int]: ...

    def act_on_polynomial(self, f: _Polynomial) -> _Polynomial: ...
    def __call__(self, *args: object, **kwargs: object) -> Matrix[RingElement]: ...
    def commutator(self, other: Matrix[_OtherScalar]) -> Matrix[RingElement]: ...
    def anticommutator(self, other: Matrix[_OtherScalar]) -> Matrix[RingElement]: ...

    def swap_columns(self, c1: _MatrixAxisIndex, c2: _MatrixAxisIndex) -> None: ...
    def with_swapped_columns(
        self,
        c1: _MatrixAxisIndex,
        c2: _MatrixAxisIndex,
    ) -> Self: ...
    def permute_columns(self, permutation: PermutationGroupElement) -> None: ...
    def with_permuted_columns(self, permutation: PermutationGroupElement) -> Self: ...
    def swap_rows(self, r1: _MatrixAxisIndex, r2: _MatrixAxisIndex) -> None: ...
    def with_swapped_rows(
        self,
        r1: _MatrixAxisIndex,
        r2: _MatrixAxisIndex,
    ) -> Self: ...
    def permute_rows(self, permutation: PermutationGroupElement) -> None: ...
    def with_permuted_rows(self, permutation: PermutationGroupElement) -> Self: ...
    def permute_rows_and_columns(
        self,
        row_permutation: PermutationGroupElement,
        column_permutation: PermutationGroupElement,
    ) -> None: ...
    def with_permuted_rows_and_columns(
        self,
        row_permutation: PermutationGroupElement,
        column_permutation: PermutationGroupElement,
    ) -> Self: ...

    def add_multiple_of_row(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_col: _MatrixAxisIndex = ...,
        end_col: _MatrixAxisIndex = ...,
    ) -> None: ...
    def with_added_multiple_of_row(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_col: _MatrixAxisIndex = ...,
        end_col: _MatrixAxisIndex = ...,
    ) -> Matrix[RingElement]: ...
    def add_multiple_of_column(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_row: _MatrixAxisIndex = ....,
        end_row: _MatrixAxisIndex = ...,
    ) -> None: ...
    def with_added_multiple_of_column(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_row: _MatrixAxisIndex = ...,
        end_row: _MatrixAxisIndex = ...,
    ) -> Matrix[RingElement]: ...
    def rescale_row(
        self,
        i: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_col: _MatrixAxisIndex = ..,
    ) -> None: ...
    def with_rescaled_row(
        self,
        i: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_col: _MatrixAxisIndex = ...,
    ) -> Matrix[RingElement]: ...
    def rescale_col(
        self,
        i: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_row: _MatrixAxisIndex = ...,
    ) -> None: ...
    def with_rescaled_col(
        self,
        i: _MatrixAxisIndex,
        s: ElementConstructorInput,
        start_row: _MatrixAxisIndex = ...,
    ) -> Matrix[RingElement]: ...
    def set_row_to_multiple_of_row(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
    ) -> None: ...
    def with_row_set_to_multiple_of_row(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
    ) -> Matrix[RingElement]: ...
    def set_col_to_multiple_of_col(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
    ) -> None: ...
    def with_col_set_to_multiple_of_col(
        self,
        i: _MatrixAxisIndex,
        j: _MatrixAxisIndex,
        s: ElementConstructorInput,
    ) -> Matrix[RingElement]: ...
    def reverse_rows_and_columns(self) -> None: ...
    def mutate(self, k: _MatrixAxisIndex) -> None: ...

    def linear_combination_of_rows(
        self,
        v: Iterable[ElementConstructorInput],
    ) -> FreeModuleElement[RingElement]: ...
    def linear_combination_of_columns(
        self,
        v: Iterable[ElementConstructorInput],
    ) -> FreeModuleElement[RingElement]: ...

    def is_symmetric(self) -> bool: ...
    def is_hermitian(self) -> bool: ...
    def is_skew_hermitian(self) -> bool: ...
    def is_skew_symmetric(self) -> bool: ...
    def is_alternating(self) -> bool: ...
    @overload
    def is_symmetrizable(
        self,
        return_diag: Literal[False] = ...,
        positive: bool = ...,
    ) -> bool: ...
    @overload
    def is_symmetrizable(
        self,
        return_diag: Literal[True],
        positive: bool = ...,
    ) -> list[RingElement] | Literal[False]: ...
    @overload
    def is_symmetrizable(
        self,
        return_diag: bool = ...,
        positive: bool = ...,
    ) -> bool | list[RingElement]: ...
    @overload
    def is_skew_symmetrizable(
        self,
        return_diag: Literal[False] = ...,
        positive: bool = ...,
    ) -> bool: ...
    @overload
    def is_skew_symmetrizable(
        self,
        return_diag: Literal[True],
        positive: bool = ...,
    ) -> list[RingElement] | Literal[False]: ...
    @overload
    def is_skew_symmetrizable(
        self,
        return_diag: bool = ...,
        positive: bool = ...,
    ) -> bool | list[RingElement]: ...
    def is_dense(self) -> bool: ...
    def is_sparse(self) -> bool: ...
    def is_square(self) -> bool: ...
    def is_invertible(self) -> bool: ...
    is_unit = is_invertible
    def is_singular(self) -> bool: ...

    def pivots(self) -> tuple[int, ...]: ...
    def rank(self) -> int: ...
    def nonpivots(self) -> tuple[int, ...]: ...
    def nonzero_positions(
        self,
        copy: bool = ...,
        column_order: bool = ...,
    ) -> list[tuple[int, int]]: ...
    def nonzero_positions_in_column(self, i: _MatrixAxisIndex) -> list[int]: ...
    def nonzero_positions_in_row(self, i: _MatrixAxisIndex) -> list[int]: ...
    def multiplicative_order(self) -> Integer | PlusInfinity: ...
    def iterates(
        self,
        v: FreeModuleElement[RingElement] | Sequence[ElementConstructorInput],
        n: _MatrixAxisIndex,
        rows: bool = ...,
    ) -> Matrix[_Scalar]: ...

    def _add_(self, right: Matrix[_Scalar]) -> Self: ...
    def _sub_(self, right: Matrix[_Scalar]) -> Self: ...
    def __mod__(self, p: ElementConstructorInput) -> Self: ...
    def mod(self, p: ElementConstructorInput) -> Matrix[RingElement]: ...
    def _rmul_(self, left: Element) -> Self: ...
    def _lmul_(self, right: Element) -> Self: ...
    def __neg__(self) -> Self: ...
    def __invert__(self) -> Matrix[RingElement]: ...
    def inverse_of_unit(self, algorithm: Literal["df"] | None = ...) -> Self: ...
    def __pos__(self) -> Self: ...
    @overload
    def __pow__(
        self,
        n: int | Integer,
        ignored: None = ...,
    ) -> Matrix[RingElement]: ...
    @overload
    def __pow__(
        self,
        n: Expression,
        ignored: None = ...,
    ) -> Matrix[Expression]: ...
    def __hash__(self) -> int: ...
    def _richcmp_(self, right: object, op: int) -> bool: ...
    def __bool__(self) -> bool: ...


def unpickle[_T: RingElement](
    cls: type[Matrix[_T]],
    parent: Parent[Matrix[_T]],
    immutability: bool,
    cache: dict[str, object] | None,
    data: object,
    version: int,
) -> Matrix[_T]: ...
