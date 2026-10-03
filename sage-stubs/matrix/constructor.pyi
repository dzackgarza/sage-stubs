from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Literal, overload

from sage.matrix.matrix2 import Matrix
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_rational_dense import Matrix_rational_dense
from sage.matrix.matrix_space import MatrixIndexKeys, MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.rational_field import RationalField
from sage.rings.ring import Ring
from sage.structure.element import Element, RingElement


type MatrixEntry = RingElement | Element | int | Integer
type DenseMatrixEntries = (
    Matrix
    | Matrix_integer_dense
    | Matrix_rational_dense
    | FreeModuleElement
    | Sequence[MatrixEntry]
    | Sequence[Sequence[MatrixEntry]]
    | Iterable[MatrixEntry | Sequence[MatrixEntry]]
    | Callable[[int, int], MatrixEntry]
)
type MatrixEntries = DenseMatrixEntries | Mapping[tuple[int, int], MatrixEntry]


@overload
def matrix(
    ring: RationalField,
    nrows: DenseMatrixEntries,
    ncols: None = None,
    entries: MatrixEntry = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False] | None = None,
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_rational_dense: ...
@overload
def matrix(
    ring: RationalField,
    nrows: int | Integer,
    ncols: DenseMatrixEntries,
    entries: MatrixEntry = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False] | None = None,
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_rational_dense: ...
@overload
def matrix(
    ring: RationalField,
    nrows: int | Integer,
    ncols: int | Integer,
    entries: MatrixEntry | DenseMatrixEntries = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False] | None = None,
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_rational_dense: ...
@overload
def matrix(
    ring: RationalField,
    nrows: int | Integer | None = None,
    ncols: int | Integer | None = None,
    entries: MatrixEntry | MatrixEntries = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False],
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_rational_dense: ...
@overload
def matrix(
    ring: IntegerRing_class,
    nrows: DenseMatrixEntries,
    ncols: None = None,
    entries: MatrixEntry = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False] | None = None,
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_integer_dense: ...
@overload
def matrix(
    ring: IntegerRing_class,
    nrows: int | Integer,
    ncols: DenseMatrixEntries,
    entries: MatrixEntry = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False] | None = None,
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_integer_dense: ...
@overload
def matrix(
    ring: IntegerRing_class,
    nrows: int | Integer,
    ncols: int | Integer,
    entries: MatrixEntry | DenseMatrixEntries = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False] | None = None,
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_integer_dense: ...
@overload
def matrix(
    ring: IntegerRing_class,
    nrows: int | Integer | None = None,
    ncols: int | Integer | None = None,
    entries: MatrixEntry | MatrixEntries = 0,
    *,
    base_ring: None = None,
    sparse: Literal[False],
    row_keys: None = None,
    column_keys: None = None,
    space: None = None,
    immutable: bool = False,
) -> Matrix_integer_dense: ...
@overload
def matrix(
    ring: Ring | None = None,
    nrows: int | Integer | MatrixIndexKeys | MatrixEntries | None = None,
    ncols: int | Integer | MatrixIndexKeys | MatrixEntries | None = None,
    entries: MatrixEntry | MatrixEntries = 0,
    *,
    base_ring: Ring | None = None,
    sparse: bool | None = None,
    row_keys: MatrixIndexKeys | None = None,
    column_keys: MatrixIndexKeys | None = None,
    space: MatrixSpace | None = None,
    immutable: bool = False,
) -> Matrix | Matrix_integer_dense | Matrix_rational_dense: ...


def identity_matrix(ring: Ring | None = None, n: int = 1) -> Matrix: ...
def zero_matrix(ring: Ring | None = None, nrows: int = 1, ncols: int = 1) -> Matrix: ...
def diagonal_matrix(
    arg0: MatrixEntries | Iterable[MatrixEntry],
    arg1: MatrixEntries | Iterable[MatrixEntry] | None = None,
) -> Matrix: ...
