from collections.abc import Callable, Mapping, Sequence
from typing import Generic, Literal, Self, TypeVar

from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_mod2_dense import Matrix_mod2_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.element_base import FinitePolyExtElement
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_FieldElement = TypeVar(
    "_FieldElement",
    bound=FinitePolyExtElement,
    default=FinitePolyExtElement,
)

type MatrixGF2EEntries = (
    Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | ElementConstructorInput
    | None
)


class M4RIE_finite_field:
    """Internal owner of an M4RIE finite-field representation."""


class Matrix_gf2e_dense(
    Matrix_dense[_FieldElement],
    Generic[_FieldElement],
):
    def __init__(
        self,
        parent: MatrixSpace[_FieldElement],
        entries: MatrixGF2EEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __bool__(self) -> bool: ...
    def _list(self) -> list[_FieldElement]: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _multiply_classical(self, right: Self) -> Self: ...
    def _multiply_newton_john(self, right: Self) -> Self: ...
    def _multiply_karatsuba(self, right: Self) -> Self: ...
    def _multiply_strassen(self, right: Self, cutoff: int = ...) -> Self: ...
    def _lmul_(self, right: _FieldElement) -> Self: ...
    def __neg__(self) -> Self: ...
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
        *args: object,
        **kwds: object,
    ) -> None: ...
    def echelonize(
        self,
        algorithm: Literal[
            "heuristic",
            "newton_john",
            "ple",
            "naive",
            "builtin",
        ] = ...,
        reduced: bool = ...,
        **kwds: object,
    ) -> None | Self: ...
    def _pivots(self) -> list[int]: ...
    def rank(self) -> int: ...
    def is_invertible(self) -> bool: ...
    def __invert__(self) -> Self: ...
    def augment(
        self,
        right: Self | FreeModuleElement[RingElement],
    ) -> Self: ...
    def submatrix(
        self,
        row: int = ...,
        col: int = ...,
        nrows: int = ...,
        ncols: int = ...,
    ) -> Self: ...
    def slice(self) -> tuple[Matrix_mod2_dense, ...] | None: ...
    def cling(self, *components: Matrix_mod2_dense) -> None: ...
    def determinant(self) -> _FieldElement: ...
