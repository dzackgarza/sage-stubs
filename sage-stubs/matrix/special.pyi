from collections.abc import Callable, Iterable, Sequence
from typing import TypeVar

from sage.matrix.matrix import Matrix
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


def identity_matrix(
    ring: Parent[_Scalar],
    n: int | Integer,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


def zero_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer | None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


def diagonal_matrix(
    ring: Parent[_Scalar],
    diagonal: Iterable[ElementConstructorInput],
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


def block_matrix(
    blocks: Sequence[Sequence[Matrix[_Scalar] | ElementConstructorInput | None]],
    subdivide: bool = ...,
    sparse: bool | None = ...,
) -> Matrix[_Scalar]: ...


def block_diagonal_matrix(
    *blocks: Matrix[_Scalar],
    subdivide: bool = ...,
) -> Matrix[_Scalar]: ...


def elementary_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    row1: int | None = ...,
    row2: int | None = ...,
    scale: ElementConstructorInput | None = ...,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


def companion_matrix(
    polynomial: RingElement,
    format: str = ...,
) -> Matrix[_Scalar]: ...


def jordan_block(
    eigenvalue: _Scalar,
    size: int | Integer,
    sparse: bool = ...,
) -> Matrix[_Scalar]: ...


def diagonal_matrix_from_blocks(
    blocks: Sequence[Matrix[_Scalar]],
) -> Matrix[_Scalar]: ...


def circulant(
    first_row: Sequence[_Scalar],
) -> Matrix[_Scalar]: ...


def toeplitz(
    first_column: Sequence[_Scalar],
    first_row: Sequence[_Scalar] | None = ...,
) -> Matrix[_Scalar]: ...


def vandermonde(
    entries: Sequence[_Scalar],
    ncols: int | Integer | None = ...,
) -> Matrix[_Scalar]: ...


def random_matrix(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer | None = ...,
    algorithm: str = ...,
    implementation: str | None = ...,
    density: float | None = ...,
    sparse: bool = ...,
    *args: object,
    **kwds: object,
) -> Matrix[_Scalar]: ...


def matrix_from_rows(
    rows: Sequence[Sequence[_Scalar]],
    ring: Parent[_Scalar] | None = ...,
) -> Matrix[_Scalar]: ...


def matrix_from_columns(
    columns: Sequence[Sequence[_Scalar]],
    ring: Parent[_Scalar] | None = ...,
) -> Matrix[_Scalar]: ...


def matrix_from_function(
    ring: Parent[_Scalar],
    nrows: int | Integer,
    ncols: int | Integer,
    function: Callable[[int, int], _Scalar],
) -> Matrix[_Scalar]: ...
