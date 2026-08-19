from collections.abc import Iterable, Iterator, Sequence
from typing import Generic, Literal, TextIO, TypeVar, overload

from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

_Point = TypeVar("_Point", bound=ModuleElement, default=ModuleElement)
_Module = TypeVar(
    "_Module",
    bound=Parent[ModuleElement],
    default=Parent[ModuleElement],
)

PointIndex = int | Integer
PointIndices = Iterable[PointIndex]
PointCollectionFormat = Literal[
    "default",
    "tuple",
    "matrix",
    "column matrix",
    "separated column matrix",
]


class PointCollection(
    SageObject,
    Sequence[_Point],
    Generic[_Point, _Module],
):
    def __init__(
        self,
        points: Iterable[_Point],
        module: _Module | None = ...,
    ) -> None: ...
    def __add__(
        self,
        right: PointCollection[_Point, _Module],
    ) -> PointCollection[_Point, _Module]: ...
    def __call__(
        self,
        *indices: PointIndex | PointIndices,
    ) -> PointCollection[_Point, _Module]: ...
    def __richcmp__(
        self,
        other: PointCollection[_Point, _Module],
        op: int,
    ) -> bool: ...
    @overload
    def __getitem__(self, n: PointIndex) -> _Point: ...
    @overload
    def __getitem__(self, n: slice) -> tuple[_Point, ...]: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[_Point]: ...
    def __len__(self) -> int: ...
    def __list__(self) -> list[_Point]: ...
    def __tuple__(self) -> tuple[_Point, ...]: ...
    def __mul__(self, right: object) -> object: ...
    def __rmul__(self, left: object) -> object: ...
    def __reduce__(
        self,
    ) -> tuple[type[PointCollection], tuple[tuple[_Point, ...], _Module]]: ...
    def _latex_(self) -> str: ...
    def _matrix_(self, ring: Ring | None = ...) -> Matrix[RingElement]: ...
    def _repr_(self) -> str: ...
    def basis(self) -> PointCollection[_Point, _Module]: ...
    def cardinality(self) -> int: ...
    def cartesian_product(
        self,
        other: PointCollection,
        module: Parent[ModuleElement] | None = ...,
    ) -> PointCollection[ModuleElement, Parent[ModuleElement]]: ...
    def column_matrix(self) -> Matrix[RingElement]: ...
    def dimension(self) -> int: ...
    dim = dimension
    def dual_module(self) -> FreeModule_generic[RingElement]: ...
    def index(
        self,
        point: _Point,
        start: PointIndex = ...,
        stop: PointIndex = ...,
    ) -> int: ...
    def matrix(self) -> Matrix[RingElement]: ...
    def module(self) -> _Module: ...
    @staticmethod
    @overload
    def output_format(format: None = ...) -> PointCollectionFormat: ...
    @staticmethod
    @overload
    def output_format(format: PointCollectionFormat) -> None: ...
    def set(self) -> frozenset[_Point]: ...
    def write_for_palp(self, f: TextIO) -> None: ...


@overload
def read_palp_point_collection(
    f: TextIO,
    lattice: _Module | None = ...,
    permutation: Literal[False] = ...,
) -> PointCollection[FreeModuleElement[RingElement], _Module] | None: ...
@overload
def read_palp_point_collection(
    f: TextIO,
    lattice: _Module | None = ...,
    permutation: Literal[True] = ...,
) -> tuple[
    PointCollection[FreeModuleElement[RingElement], _Module],
    tuple[int, ...],
] | None: ...
