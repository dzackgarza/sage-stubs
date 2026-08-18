from collections.abc import Callable, Mapping, Sequence
from os import PathLike
from typing import Literal, Self, overload

from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.matrix.matrix_dense import Matrix_dense
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.vector_mod2_dense import Vector_mod2_dense
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.element import Element
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

type _GammaCertificate = tuple[int, int, int, int]
type _EntryRepresentation = Mapping[IntegerMod_abstract, str] | Callable[[IntegerMod_abstract], str]
type _MatrixEntries = (
    Element
    | Sequence[Element]
    | Sequence[Sequence[Element]]
    | None
)

class Matrix_mod2_dense(Matrix_dense[IntegerMod_abstract]):
    def __init__(
        self,
        parent: MatrixSpace,
        entries: _MatrixEntries = ...,
        copy: bool | None = ...,
        coerce: bool = ...,
    ) -> None: ...
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
        left_border: Sequence[object] | None = ...,
        right_border: Sequence[object] | None = ...,
        top_border: Sequence[object] | None = ...,
        bottom_border: Sequence[object] | None = ...,
    ) -> str | AsciiArt | UnicodeArt: ...
    def row(self, i: int, from_list: bool = ...) -> Vector_mod2_dense: ...
    @overload
    def columns(self, copy: Literal[True] = ...) -> list[Vector_mod2_dense]: ...
    @overload
    def columns(self, copy: Literal[False]) -> tuple[Vector_mod2_dense, ...]: ...
    def _add_(self, right: Matrix_mod2_dense) -> Matrix_mod2_dense: ...
    def _sub_(self, right: Matrix_mod2_dense) -> Matrix_mod2_dense: ...
    def _multiply_m4rm(
        self,
        right: Matrix_mod2_dense,
        k: int,
    ) -> Matrix_mod2_dense: ...
    def _multiply_strassen(
        self,
        right: Matrix_mod2_dense,
        cutoff: int,
    ) -> Matrix_mod2_dense: ...
    def _export_as_string(self) -> str: ...
    def __neg__(self) -> Self: ...
    def __invert__(self) -> Self: ...
    def __copy__(self) -> Self: ...
    def _list(self) -> list[IntegerMod_abstract]: ...
    def echelonize(
        self,
        algorithm: Literal["heuristic", "m4ri", "pluq", "classical"] = ...,
        cutoff: int = ...,
        reduced: bool = ...,
        **kwds: int,
    ) -> None | Self: ...
    def _pivots(self) -> list[int]: ...
    def randomize(self, density: float = ..., nonzero: bool = ...) -> None: ...
    def determinant(self) -> IntegerMod_abstract: ...
    def transpose(self) -> Self: ...
    def augment(
        self,
        right: Matrix_mod2_dense,
        subdivide: bool = ...,
    ) -> Matrix_mod2_dense: ...
    def submatrix(
        self,
        row: int = ...,
        col: int = ...,
        nrows: int = ...,
        ncols: int = ...,
    ) -> Matrix_mod2_dense: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[..., Matrix_mod2_dense],
        tuple[int, int, bytes | None, int, bool],
    ]: ...
    def density(self, approx: bool = ...) -> Rational | RealNumber: ...
    def rank(self, algorithm: Literal["ple", "m4ri"] = ...) -> int: ...
    def _solve_right_general(
        self,
        B: Matrix_mod2_dense,
        check: bool = ...,
    ) -> Matrix_mod2_dense: ...
    def _right_kernel_matrix(
        self,
        **kwds: object,
    ) -> tuple[Literal["computed-pluq"], Matrix_mod2_dense]: ...
    def doubly_lexical_ordering(
        self,
        inplace: bool = ...,
    ) -> tuple[PermutationGroupElement, PermutationGroupElement]: ...
    @overload
    def is_Gamma_free(self, certificate: Literal[False] = ...) -> bool: ...
    @overload
    def is_Gamma_free(
        self,
        certificate: Literal[True],
    ) -> tuple[bool, _GammaCertificate | None]: ...

def parity(a: int) -> int: ...
def unpickle_matrix_mod2_dense_v2(
    r: int,
    c: int,
    data: bytes | None,
    size: int,
    immutable: bool = ...,
) -> Matrix_mod2_dense: ...
def from_png(filename: str | PathLike[str]) -> Matrix_mod2_dense: ...
def to_png(
    A: Matrix_mod2_dense,
    filename: str | PathLike[str],
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
