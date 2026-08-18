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

from sage.matrix.matrix_space import MatrixSpace
from sage.matrix.matrix import Matrix

class SparseEntry:
    i: int
    j: int
    entry: object

    def __init__(self, i: int, j: int, entry: ElementConstructorInput) -> None: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...

class MatrixArgs:
    base: CommutativeRing | None
    nrows: int
    ncols: int
    entries: object
    sparse: int
    row_keys: object
    column_keys: object
    space: MatrixSpace | None
    kwds: dict[str, object]

    def __init__(
        self,
        *args: ElementConstructorInput,
        base_ring: CommutativeRing | None = None,
        nrows: int | None = None,
        ncols: int | None = None,
        entries: FreeModuleElement[_Scalar] | Sequence[_Scalar] = None,
        sparse: bool | None = None,
        row_keys: ElementConstructorInput = None,
        column_keys: ElementConstructorInput = None,
        space: MatrixSpace | None = None,
        **kwds: ElementConstructorInput,
    ) -> None: ...
    def __reduce__(self) -> ElementConstructorInput: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...
    def iter(
        self, convert: bool = True, sparse: bool = False
    ) -> ElementConstructorInput: ...
    def __len__(self) -> int: ...
    def finalized(self) -> MatrixArgs: ...
    def set_nrows(self, nrows: int) -> None: ...
    def set_ncols(self, ncols: int) -> None: ...
    def set_sparse(self, sparse: bool) -> None: ...
    def set_row_keys(self, row_keys: ElementConstructorInput) -> None: ...
    def set_column_keys(self, column_keys: ElementConstructorInput) -> None: ...
    def set_space(self, space: MatrixSpace) -> None: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    def list(self) -> tuple[_Scalar, ...]: ...
    def dict(self) -> ElementConstructorInput: ...
