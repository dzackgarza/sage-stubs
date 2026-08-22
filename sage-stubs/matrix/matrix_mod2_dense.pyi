from collections.abc import Callable, Mapping, Sequence
from os import PathLike
from typing import Literal, Self, overload

from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.matrix.matrix0 import Matrix as Matrix_base
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.vector_mod2_dense import Vector_mod2_dense
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.parent import ElementConstructorInput
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt


type _GammaCertificate = tuple[int, int, int, int]
type _EntryRepresentation = (
    Mapping[IntegerMod_abstract, str]
    | Callable[[IntegerMod_abstract], str]
)
type _MatrixEntries = (
    ElementConstructorInput
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
    | None
)
type _BorderLabels = Sequence[object] | None


class Matrix_mod2_dense(Matrix_dense[IntegerMod_abstract]):
    def __init__(
        self,
        parent: MatrixSpace[IntegerMod_abstract],
        entries: _MatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...

    @overload
    def str(
        self,
        rep_mapping: _EntryRepresentation | None = ...,
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
        rep_mapping: _EntryRepresentation | None = ...,
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
        rep_mapping: _EntryRepresentation | None = ...,
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
        rep_mapping: _EntryRepresentation | None = ...,
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

    def row(
        self,
        i: int,
        from_list: bool = ...,
    ) -> Vector_mod2_dense: ...
    def columns(self, copy: bool = ...) -> list[Vector_mod2_dense]: ...
    def _add_(self, right: Self) -> Self: ...
    def _sub_(self, right: Self) -> Self: ...
    def _multiply_m4rm(
        self,
        right: Self,
        k: int,
    ) -> Self: ...
    def _multiply_classical(self, right: Self) -> Self: ...
    def _multiply_strassen(
        self,
        right: Self,
        cutoff: int,
    ) -> Self: ...
    def __neg__(self) -> Self: ...
    def __invert__(self) -> Self: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[IntegerMod_abstract]: ...
    def echelonize(
        self,
        algorithm: Literal[
            "heuristic",
            "m4ri",
            "pluq",
            "linbox",
            "classical",
        ] = ...,
        cutoff: int = ...,
        reduced: bool = ...,
        **kwds: object,
    ) -> None | Self: ...
    def _pivots(self) -> list[int]: ...
    def randomize(
        self,
        density: float = ...,
        nonzero: bool = ...,
    ) -> None: ...
    def _magma_init_(self, magma: object) -> str: ...
    def determinant(self) -> IntegerMod_abstract: ...
    def transpose(self) -> Self: ...
    def _richcmp_(self, right: Self, op: int) -> bool: ...
    def augment(
        self,
        right: (
            Matrix_base[IntegerMod_abstract]
            | FreeModuleElement[IntegerMod_abstract]
        ),
        subdivide: bool = ...,
    ) -> Self: ...
    def submatrix(
        self,
        row: int = ...,
        col: int = ...,
        nrows: int = ...,
        ncols: int = ...,
    ) -> Self: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Matrix_mod2_dense],
        tuple[int, int, bytes | None, int, bool],
    ]: ...
    def _export_as_string(self) -> str: ...
    @overload
    def density(self, approx: Literal[False] = ...) -> Rational: ...
    @overload
    def density(self, approx: Literal[True]) -> RealNumber: ...
    @overload
    def density(self, approx: bool = ...) -> Rational | RealNumber: ...
    def rank(
        self,
        algorithm: Literal["ple", "m4ri"] = ...,
    ) -> int: ...
    def _solve_right_general(
        self,
        B: Self,
        check: bool = ...,
    ) -> Self: ...
    def _right_kernel_matrix(
        self,
        **kwds: object,
    ) -> tuple[Literal["computed-pluq"], Self]: ...
    def doubly_lexical_ordering(
        self,
        inplace: bool = ...,
    ) -> tuple[PermutationGroupElement, PermutationGroupElement]: ...
    @overload
    def is_Gamma_free(
        self,
        certificate: Literal[False] = ...,
    ) -> bool: ...
    @overload
    def is_Gamma_free(
        self,
        certificate: Literal[True],
    ) -> tuple[bool, _GammaCertificate | None]: ...
    @overload
    def is_Gamma_free(
        self,
        certificate: bool = ...,
    ) -> bool | tuple[bool, _GammaCertificate | None]: ...


def parity(a: int) -> int: ...


def unpickle_matrix_mod2_dense_v2(
    r: int,
    c: int,
    data: bytes | Sequence[int] | None,
    size: int,
    immutable: bool = ...,
) -> Matrix_mod2_dense: ...


def from_png(
    filename: str | bytes | PathLike[str],
) -> Matrix_mod2_dense: ...


def to_png(
    A: Matrix_mod2_dense,
    filename: str | bytes | PathLike[str],
) -> None: ...


def pluq(
    A: Matrix_mod2_dense,
    algorithm: Literal["standard", "mmpf", "naive"] = ...,
    param: int = ...,
) -> tuple[Matrix_mod2_dense, list[int], list[int]]: ...


def ple(
    A: Matrix_mod2_dense,
    algorithm: Literal["standard", "russian", "naive"] = ...,
    param: int = ...,
) -> tuple[Matrix_mod2_dense, list[int], list[int]]: ...
