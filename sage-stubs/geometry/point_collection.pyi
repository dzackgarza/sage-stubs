from collections.abc import Iterable, Iterator
from typing import Generic, Literal, Self, TextIO, TypeVar, overload

from sage.geometry.toric_lattice import (
    ToricLattice_ambient,
    ToricLattice_generic,
)
from sage.geometry.toric_lattice_element import ToricLatticeElement
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.matrix.matrix0 import Matrix
from sage.rings.integer import Integer
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

_Point = TypeVar("_Point", bound=Element, default=Element)
_Module = TypeVar("_Module", bound=Parent, default=Parent)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)


type PointCollectionOutputFormat = Literal[
    "default",
    "tuple",
    "matrix",
    "column matrix",
    "separated column matrix",
]
type ToricPointCollection = PointCollection[
    ToricLatticeElement,
    ToricLattice_generic,
    Integer,
]


class PointCollection(
    SageObject,
    Generic[_Point, _Module, _Scalar],
):
    def __init__(
        self,
        points: Iterable[_Point],
        module: _Module | None = ...,
    ) -> None: ...
    def _sage_input_(
        self,
        sib: object,
        coerced: bool,
    ) -> object: ...
    def __add__(
        self,
        right: PointCollection[_Point, _Module, _Scalar],
    ) -> Self: ...
    @overload
    def __call__(self, indices: Iterable[int]) -> Self: ...
    @overload
    def __call__(self, *indices: int) -> Self: ...
    def __richcmp__(
        self,
        other: PointCollection,
        op: int,
    ) -> bool: ...
    @overload
    def __getitem__(self, n: int) -> _Point: ...
    @overload
    def __getitem__(self, n: slice) -> tuple[_Point, ...]: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[_Point]: ...
    def __len__(self) -> int: ...
    def __list__(self) -> list[_Point]: ...
    def __mul__(self, right: object) -> object: ...
    def __reduce__(
        self,
    ) -> tuple[type[PointCollection], tuple[tuple[_Point, ...], _Module]]: ...
    def __tuple__(self) -> tuple[_Point, ...]: ...
    def _latex_(self) -> str: ...
    @overload
    def _matrix_(self, ring: None = ...) -> Matrix[_Scalar]: ...
    @overload
    def _matrix_(
        self,
        ring: Parent[_NewScalar],
    ) -> Matrix[_NewScalar]: ...
    def _repr_(self) -> str: ...
    def basis(self) -> Self: ...
    def cardinality(self) -> int: ...
    def cartesian_product(
        self,
        other: PointCollection,
        module: Parent | None = ...,
    ) -> PointCollection[Element, Parent, RingElement]: ...
    def column_matrix(self) -> Matrix[_Scalar]: ...
    def dimension(self) -> int: ...
    dim = dimension
    def dual_module(self) -> Parent: ...
    def index(self, *args: object) -> int: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    def module(self) -> _Module: ...
    @staticmethod
    @overload
    def output_format(format: None = ...) -> str: ...
    @staticmethod
    @overload
    def output_format(format: PointCollectionOutputFormat) -> None: ...
    def set(self) -> frozenset[_Point]: ...
    def write_for_palp(self, f: TextIO) -> None: ...


@overload
def read_palp_point_collection(
    f: TextIO,
    lattice: ToricLattice_generic | None = ...,
    permutation: Literal[False] = ...,
) -> ToricPointCollection | None: ...
@overload
def read_palp_point_collection(
    f: TextIO,
    lattice: ToricLattice_generic | None = ...,
    permutation: Literal[True] = ...,
) -> tuple[ToricPointCollection, PermutationGroupElement] | None: ...
@overload
def read_palp_point_collection(
    f: TextIO,
    lattice: ToricLattice_generic | None = ...,
    permutation: bool = ...,
) -> (
    ToricPointCollection
    | tuple[ToricPointCollection, PermutationGroupElement]
    | None
): ...
