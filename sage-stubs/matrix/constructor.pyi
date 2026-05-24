from collections.abc import Callable, Mapping, Sequence

from sage.matrix.matrix2 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import RingElement

type MatrixEntry = RingElement | int | Integer
type MatrixEntries = Matrix | FreeModuleElement | Sequence[MatrixEntry] | Sequence[Sequence[MatrixEntry]] | Mapping[tuple[int, int], MatrixEntry] | Callable[[int, int], MatrixEntry]

def matrix(ring: Ring | None = None, nrows: int | Integer | MatrixEntries | None = None, ncols: int | Integer | MatrixEntries | None = None, entries: MatrixEntry | MatrixEntries = 0) -> Matrix: ...
def identity_matrix(ring: Ring | None = None, n: int = 1) -> Matrix: ...
def zero_matrix(ring: Ring | None = None, nrows: int = 1, ncols: int = 1) -> Matrix: ...
def diagonal_matrix(arg0: MatrixEntries, arg1: MatrixEntries | None = None) -> Matrix: ...
