from collections.abc import Iterator, Sequence
from typing import Self, TypeVar
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_double import RealDoubleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

from sage.matrix.matrix2 import Matrix as _MatrixClass
from sage.matrix.matrix_space import MatrixSpace, MatrixIndexKeys

type MatrixEntry = RingElement | Element | int | Integer
type MatrixEntries = (
    _MatrixClass
    | FreeModuleElement
    | Sequence[MatrixEntry]
    | Sequence[Sequence[MatrixEntry]]
    | Mapping[tuple[int, int], MatrixEntry]
    | Callable[[int, int], MatrixEntry]
)

class _MatrixConstructor:
    def __call__(
        self,
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
    ) -> _MatrixClass: ...
    def diagonal(
        self,
        arg0: MatrixEntries | Iterable[MatrixEntry],
        arg1: MatrixEntries | Iterable[MatrixEntry] | None = None,
    ) -> _MatrixClass: ...
    def identity(self, ring: Ring | None = None, n: int = 1) -> _MatrixClass: ...
    def zero(
        self, ring: Ring | None = None, nrows: int = 1, ncols: int = 1
    ) -> _MatrixClass: ...
    def block(self, blocks: Iterable[MatrixEntries]) -> _MatrixClass: ...

matrix: _MatrixConstructor
Matrix: _MatrixConstructor

def identity_matrix(ring: Ring | None = None, n: int = 1) -> _MatrixClass: ...
def zero_matrix(
    ring: Ring | None = None, nrows: int = 1, ncols: int = 1
) -> _MatrixClass: ...
def diagonal_matrix(
    arg0: MatrixEntries | Iterable[MatrixEntry],
    arg1: MatrixEntries | Iterable[MatrixEntry] | None = None,
) -> _MatrixClass: ...
