from collections.abc import Callable, Iterable, Mapping, Sequence

from sage.matrix.matrix2 import Matrix
from sage.matrix.matrix_space import MatrixSpace, MatrixIndexKeys
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import Element, RingElement

type MatrixEntry = RingElement | Element | int | Integer
type MatrixEntries = Matrix | FreeModuleElement | Sequence[MatrixEntry] | Sequence[Sequence[MatrixEntry]] | Mapping[tuple[int, int], MatrixEntry] | Callable[[int, int], MatrixEntry]

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
) -> Matrix: ...
def identity_matrix(ring: Ring | None = None, n: int = 1) -> Matrix: ...
def zero_matrix(ring: Ring | None = None, nrows: int = 1, ncols: int = 1) -> Matrix: ...
def diagonal_matrix(arg0: MatrixEntries | Iterable[MatrixEntry], arg1: MatrixEntries | Iterable[MatrixEntry] | None = None) -> Matrix: ...
