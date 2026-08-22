from collections.abc import Callable
from typing import Generic, Literal, Self, TypeVar, overload

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixData, MatrixSpace
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.finite_rings.integer_mod import IntegerMod_int
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput, Parent

_FieldElement = TypeVar(
    "_FieldElement",
    bound=FiniteRingElement,
    default=FiniteRingElement,
)

type MeatAxePickleParent[_T: FiniteRingElement] = MatrixSpace[_T] | Literal[0]


class FieldConverter_class(Generic[_FieldElement]):
    field: Callable[[int], _FieldElement] | Parent[_FieldElement]
    zero_FEL: int

    def __init__(self, field: Parent[_FieldElement]) -> None: ...
    def fel_to_field(self, x: int) -> _FieldElement: ...
    def field_to_fel(self, x: _FieldElement) -> int: ...


class PrimeFieldConverter_class(FieldConverter_class[IntegerMod_int]):
    field: Parent[IntegerMod_int]

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
        entries: MatrixData[_FieldElement] = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
        *,
        mutable: bool = ...,
    ) -> None: ...
    @staticmethod
    def from_filename(
        filename: str | bytes,
    ) -> Matrix_gfpn_dense[FiniteRingElement]: ...
    def __copy__(self) -> Self: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Matrix_gfpn_dense[_FieldElement]],
        tuple[
            MeatAxePickleParent[_FieldElement],
            int,
            int,
            bytes | str,
            bool,
        ],
    ]: ...
    def randomize(
        self,
        density: float | None = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...
    def get_slice(
        self,
        i: int | Integer,
        j: int | Integer,
    ) -> Self: ...
    def _rowlist_(
        self,
        i: int | Integer,
        j: int | Integer = ...,
    ) -> list[int]: ...
    def _list(self) -> list[_FieldElement]: ...
    def _richcmp_(self, right: Self, op: int) -> bool: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def __neg__(self) -> Self: ...
    def _lmul_(self, right: _FieldElement) -> Self: ...
    def _multiply_strassen(
        self,
        right: Self,
        cutoff: int | Integer = ...,
    ) -> Self: ...
    def __truediv__(
        self,
        scalar: ElementConstructorInput,
    ) -> Self: ...
    def __invert__(self) -> Self: ...
    def transpose(self) -> Self: ...
    def order(self) -> int: ...
    def left_kernel_matrix(self) -> Self: ...
    def _echelon_in_place(
        self,
        algorithm: str,
    ) -> tuple[int, ...]: ...
    def _echelon_in_place_classical(
        self,
        reduced: bool = ...,
        **kwds: object,
    ) -> tuple[int, ...]: ...


@overload
def mtx_unpickle[
    _T: FiniteRingElement,
](
    field_or_space: MatrixSpace[_T],
    nrows: int | Integer,
    ncols: int | Integer,
    data: bytes | str,
    mutable: bool,
) -> Matrix_gfpn_dense[_T]: ...
@overload
def mtx_unpickle(
    field_or_space: int | Integer,
    nrows: int | Integer,
    ncols: int | Integer,
    data: bytes | str,
    mutable: bool,
) -> Matrix_gfpn_dense[FiniteRingElement]: ...
