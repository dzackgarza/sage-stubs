from collections.abc import Callable, Mapping, Sequence
from os import PathLike
from typing import Generic, Self, TypeVar

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.rings.finite_rings.element_base import FinitePolyExtElement, FiniteRingElement
from sage.rings.finite_rings.integer_mod import IntegerMod_int
from sage.structure.parent import ElementConstructorInput, Parent

_FieldElement = TypeVar(
    "_FieldElement",
    bound=FiniteRingElement,
    default=FinitePolyExtElement,
)

type MatrixGFPNEntries = (
    Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | ElementConstructorInput
    | None
)


class FieldConverter_class(Generic[_FieldElement]):
    field: Callable[[int], _FieldElement]
    zero_FEL: int

    def __init__(self, field: Parent[_FieldElement]) -> None: ...
    def fel_to_field(self, x: int) -> _FieldElement: ...
    def field_to_fel(self, x: _FieldElement) -> int: ...


class PrimeFieldConverter_class(FieldConverter_class[IntegerMod_int]):
    def __init__(self, field: Parent[IntegerMod_int]) -> None: ...
    def fel_to_field(self, x: int) -> IntegerMod_int: ...
    def field_to_fel(self, x: IntegerMod_int) -> int: ...


class Matrix_gfpn_dense(
    Matrix_dense[_FieldElement],
    Generic[_FieldElement],
):
    _converter: FieldConverter_class[_FieldElement]

    def __init__(
        self,
        parent: MatrixSpace[_FieldElement],
        entries: MatrixGFPNEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
        *,
        mutable: bool = ...,
    ) -> None: ...
    @staticmethod
    def from_filename(
        filename: str | bytes | PathLike[str],
    ) -> Matrix_gfpn_dense[FiniteRingElement]: ...
    def __copy__(self) -> Self: ...
    def randomize(
        self,
        density: float | None = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...
    def get_slice(self, i: int, j: int) -> Self: ...
    def _rowlist_(self, i: int, j: int = ...) -> list[int]: ...
    def _list(self) -> list[_FieldElement]: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def __neg__(self) -> Self: ...
    def _lmul_(self, right: _FieldElement) -> Self: ...
    def _multiply_classical(self, right: Self) -> Self: ...
    def _multiply_strassen(self, right: Self, cutoff: int = ...) -> Self: ...
    def __truediv__(self, scalar: ElementConstructorInput) -> Self: ...
    def __invert__(self) -> Self: ...
    def transpose(self) -> Self: ...
    def order(self) -> int: ...
    def left_kernel_matrix(self) -> Self: ...
    def _echelon_in_place(self, algorithm: str) -> tuple[int, ...]: ...
    def _echelon_in_place_classical(
        self,
        reduced: bool = ...,
        **kwds: object,
    ) -> tuple[int, ...]: ...
