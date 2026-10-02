from collections.abc import Callable, Mapping, Sequence
from typing import Literal, Protocol, TypeVar, overload

import sage.matrix.special
from cypari2.gen import Gen
from sage.matrix.matrix import Matrix as MatrixClass
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.matrix_space import MatrixIndexKeys, MatrixSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.integer import Integer
from sage.rings.integer_ring import IntegerRing_class
from sage.structure.element import RingElement
from sage.structure.global_options import GlobalOptions
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type MatrixEntries[_Scalar: RingElement] = (
    MatrixClass[_Scalar]
    | FreeModuleElement[_Scalar]
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
    | Mapping[tuple[int, int], ElementConstructorInput]
    | Callable[[int, int], ElementConstructorInput]
)

# A PARI object, or flat or nested sequences of integers, whose rows may be
# PARI vectors or dense integer vectors. args.pyx:1202 makes the matrix dense
# unless the entries are a mapping, a sparse matrix or sparse vectors
# (finalize_seq_seq); a PARI object is classified by pari_typ_to_entries_type,
# which never gives sparse entries.
type _IntegerScalar = int | Integer | Gen
type _IntegerEntries = (
    Gen
    | Sequence[_IntegerScalar]
    | Sequence[Sequence[_IntegerScalar] | Vector_integer_dense | Gen]
)

class options(GlobalOptions):
    max_cols: int
    max_rows: int
    precision: int | None
    format_numeric: str

class _MatrixConstructor(Protocol):
    options: type[options]

    # args.pyx:1210: row or column keys make the space a space of module
    # morphisms, and args.pyx:812 returns an element of that space.
    @overload
    def __call__(
        self,
        *args: object,
        row_keys: MatrixIndexKeys,
        column_keys: MatrixIndexKeys | None = ...,
        **kwds: object,
    ) -> ModuleMorphism: ...
    @overload
    def __call__(
        self,
        *args: object,
        row_keys: None = ...,
        column_keys: MatrixIndexKeys,
        **kwds: object,
    ) -> ModuleMorphism: ...
    @overload
    def __call__(
        self,
        *args: object,
        space: MatrixSpace[_Scalar],
        entries: MatrixEntries[_Scalar] | ElementConstructorInput = ...,
        row_keys: None = ...,
        column_keys: None = ...,
        immutable: bool = ...,
        **kwds: object,
    ) -> MatrixClass[_Scalar]: ...
    @overload
    def __call__(
        self,
        base_ring: IntegerRing_class,
        nrows: int | Integer | _IntegerEntries = ...,
        ncols: int | Integer | _IntegerEntries = ...,
        entries: _IntegerEntries = ...,
        *,
        sparse: Literal[False] = ...,
        row_keys: None = ...,
        column_keys: None = ...,
        immutable: bool = ...,
    ) -> Matrix_integer_dense: ...
    @overload
    def __call__(
        self,
        base_ring: Parent[_Scalar],
        nrows: int | Integer | MatrixIndexKeys | MatrixEntries[_Scalar] | None = ...,
        ncols: int | Integer | MatrixIndexKeys | MatrixEntries[_Scalar] | None = ...,
        entries: MatrixEntries[_Scalar] | ElementConstructorInput = ...,
        *,
        sparse: bool | None = ...,
        row_keys: None = ...,
        column_keys: None = ...,
        immutable: bool = ...,
        **kwds: object,
    ) -> MatrixClass[_Scalar]: ...
    @overload
    def __call__(
        self,
        entries: MatrixEntries[RingElement],
        *,
        base_ring: None = ...,
        nrows: int | Integer | MatrixIndexKeys | None = ...,
        ncols: int | Integer | MatrixIndexKeys | None = ...,
        sparse: bool | None = ...,
        row_keys: None = ...,
        column_keys: None = ...,
        immutable: bool = ...,
        **kwds: object,
    ) -> MatrixClass[RingElement]: ...
    @overload
    def __call__(
        self,
        nrows: int | Integer = ...,
        ncols: int | Integer | MatrixEntries[RingElement] | None = ...,
        entries: MatrixEntries[RingElement] | ElementConstructorInput = ...,
        *,
        base_ring: None = ...,
        sparse: bool | None = ...,
        row_keys: None = ...,
        column_keys: None = ...,
        immutable: bool = ...,
        **kwds: object,
    ) -> MatrixClass[RingElement]: ...
    def column(self, *args: object, **kwds: object) -> MatrixClass[RingElement]: ...
    def random(
        self,
        ring: Parent[_Scalar],
        nrows: int | Integer,
        ncols: int | Integer | None = ...,
        algorithm: str = ...,
        implementation: str | type[MatrixClass[_Scalar]] | None = ...,
        *args: object,
        **kwds: object,
    ) -> MatrixClass[_Scalar]: ...
    def diagonal(
        self,
        arg0: object = ...,
        arg1: object = ...,
        arg2: object = ...,
        sparse: bool = ...,
    ) -> MatrixClass[RingElement]: ...
    def identity(
        self,
        ring: Parent[_Scalar] | int | Integer,
        n: int | Integer = ...,
        sparse: bool = ...,
    ) -> MatrixClass[_Scalar]: ...
    def lehmer(
        self,
        ring: Parent[_Scalar] | int | Integer,
        n: int | Integer = ...,
    ) -> MatrixClass[_Scalar]: ...
    def zero(
        self,
        ring: Parent[_Scalar] | int | Integer,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        sparse: bool = ...,
    ) -> MatrixClass[_Scalar]: ...
    def ones(
        self,
        ring: Parent[_Scalar] | int | Integer,
        nrows: int | Integer | None = ...,
        ncols: int | Integer | None = ...,
        sparse: bool = ...,
    ) -> MatrixClass[_Scalar]: ...
    def elementary(
        self,
        arg0: MatrixSpace[_Scalar] | Parent[_Scalar] | int | Integer,
        arg1: int | Integer | None = ...,
        **kwds: ElementConstructorInput,
    ) -> MatrixClass[_Scalar]: ...
    def circulant(
        self,
        v: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        sparse: bool | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def block(self, *args: object, **kwds: object) -> MatrixClass[RingElement]: ...
    def block_diagonal(
        self,
        *sub_matrices: MatrixClass[_Scalar],
        **kwds: object,
    ) -> MatrixClass[_Scalar]: ...
    def jordan_block(
        self,
        eigenvalue: _Scalar,
        size: int | Integer,
        sparse: bool = ...,
    ) -> MatrixClass[_Scalar]: ...
    def companion(
        self, poly: RingElement, format: str = ...
    ) -> MatrixClass[RingElement]: ...
    def random_rref(
        self,
        parent: MatrixSpace[_Scalar],
        num_pivots: int | Integer,
    ) -> MatrixClass[_Scalar]: ...
    def random_echelonizable(
        self,
        parent: MatrixSpace[_Scalar],
        rank: int | Integer,
        upper_bound: int | Integer | None = ...,
        max_tries: int | Integer = ...,
    ) -> MatrixClass[_Scalar]: ...
    def random_subspaces(
        self,
        parent: MatrixSpace[_Scalar],
        rank: int | Integer | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def random_unimodular(
        self,
        parent: MatrixSpace[_Scalar],
        upper_bound: int | Integer | None = ...,
        max_tries: int | Integer = ...,
    ) -> MatrixClass[_Scalar]: ...
    def random_unitary(self, parent: MatrixSpace[_Scalar]) -> MatrixClass[_Scalar]: ...
    def random_bistochastic(
        self, parent: MatrixSpace[_Scalar]
    ) -> MatrixClass[_Scalar]: ...
    def random_diagonalizable(
        self,
        parent: MatrixSpace[_Scalar],
        eigenvalues: Sequence[_Scalar] | None = ...,
        dimensions: Sequence[int | Integer] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def vector_on_axis_rotation(
        self,
        v: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        i: int | Integer,
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def ith_to_zero_rotation(
        self,
        v: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        i: int | Integer,
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def hilbert(
        self,
        dim: int | Integer,
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def vandermonde(
        self,
        v: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def toeplitz(
        self,
        c: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        r: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...
    def hankel(
        self,
        c: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar],
        r: Sequence[ElementConstructorInput] | FreeModuleElement[_Scalar] | None = ...,
        ring: Parent[_Scalar] | None = ...,
    ) -> MatrixClass[_Scalar]: ...

matrix: _MatrixConstructor
Matrix = matrix

block_diagonal_matrix = sage.matrix.special.block_diagonal_matrix
block_matrix = sage.matrix.special.block_matrix
circulant = sage.matrix.special.circulant
column_matrix = sage.matrix.special.column_matrix
companion_matrix = sage.matrix.special.companion_matrix
diagonal_matrix = sage.matrix.special.diagonal_matrix
elementary_matrix = sage.matrix.special.elementary_matrix
hankel = sage.matrix.special.hankel
hilbert = sage.matrix.special.hilbert
identity_matrix = sage.matrix.special.identity_matrix
ith_to_zero_rotation_matrix = sage.matrix.special.ith_to_zero_rotation_matrix
jordan_block = sage.matrix.special.jordan_block
lehmer = sage.matrix.special.lehmer
matrix_method = sage.matrix.special.matrix_method
ones_matrix = sage.matrix.special.ones_matrix
random_bistochastic_matrix = sage.matrix.special.random_bistochastic_matrix
random_diagonalizable_matrix = sage.matrix.special.random_diagonalizable_matrix
random_echelonizable_matrix = sage.matrix.special.random_echelonizable_matrix
random_matrix = sage.matrix.special.random_matrix
random_rref_matrix = sage.matrix.special.random_rref_matrix
random_subspaces_matrix = sage.matrix.special.random_subspaces_matrix
random_unimodular_matrix = sage.matrix.special.random_unimodular_matrix
random_unitary_matrix = sage.matrix.special.random_unitary_matrix
toeplitz = sage.matrix.special.toeplitz
vandermonde = sage.matrix.special.vandermonde
vector_on_axis_rotation_matrix = sage.matrix.special.vector_on_axis_rotation_matrix
zero_matrix = sage.matrix.special.zero_matrix
