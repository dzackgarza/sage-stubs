from collections.abc import Iterable, Iterator, Sized
from typing import Generic, Protocol, Self, TypeVar, overload

from sage.matrix.matrix2 import Matrix
from sage.rings.integer import Integer
from sage.structure.sage_object import SageObject
from sage.tensor.modules.format_utilities import FormattedExpansion

_Component = TypeVar("_Component")
_Formatted = TypeVar("_Formatted")
_FormatSpec = TypeVar("_FormatSpec")
_Component_contra = TypeVar("_Component_contra", contravariant=True)
_Formatted_co = TypeVar("_Formatted_co", covariant=True)
_FormatSpec_contra = TypeVar("_FormatSpec_contra", contravariant=True)
type _Index = int | Integer
type _IndexTuple = tuple[_Index, ...]
type _IndexList = list[_Index]
type _IndexBlock = Iterable[_Index]
type _Symmetry = _IndexBlock | Iterable[_IndexBlock] | None
type _ComponentValues[_Component] = (
    _Component
    | list[_Component]
    | list[list[_Component]]
    | list[list[list[_Component]]]
)
type _FormattedValues[_Formatted] = (
    _Formatted
    | list[_Formatted]
    | list[list[_Formatted]]
    | list[list[list[_Formatted]]]
)
type _Access = (
    _Index
    | slice
    | _IndexTuple
    | _IndexList
    | list[_IndexTuple]
    | list[_IndexList]
    | list[slice]
)

class _Ring(Protocol[_Component]):
    def __call__(self, value: _Component) -> _Component: ...
    def zero(self) -> _Ring: ...

class _Formatter1(Protocol[_Component_contra, _Formatted_co]):
    def __call__(self, value: _Component_contra) -> _Formatter1: ...

class _Formatter2(Protocol[_Component_contra, _FormatSpec_contra, _Formatted_co]):
    def __call__(
        self, value: _Component_contra, format_spec: _FormatSpec_contra
    ) -> _Formatter2: ...

type _Formatter[_Component, _Formatted, _FormatSpec] = (
    _Formatter1[_Component, _Formatted]
    | _Formatter2[_Component, _FormatSpec, _Formatted]
)

class Components(SageObject, Generic[_Component, _Formatted, _FormatSpec]):
    def __init__(
        self,
        ring: _Ring[_Component],
        frame: Sized,
        nb_indices: int,
        start_index: int = ...,
        output_formatter: _Formatter[_Component, _FormatSpec, _Formatted] | None = ...,
    ) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def __getitem__(
        self, args: slice | list[slice]
    ) -> _ComponentValues[_Component] | _FormattedValues[_Formatted] | Matrix: ...
    @overload
    def __getitem__(
        self, args: tuple[_Index | slice | _FormatSpec, ...]
    ) -> _Component | _FormattedValues[_Formatted] | Matrix: ...
    @overload
    def __getitem__(self, args: _Access) -> _ComponentValues[Components] | Matrix: ...
    def __setitem__(
        self,
        args: _Access | tuple[_Index | slice | _FormatSpec, ...],
        value: _ComponentValues[_Component],
    ) -> None: ...
    def items(self) -> Iterator: ...
    def display(
        self,
        symbol: str,
        latex_symbol: str | None = ...,
        index_positions: str | None = ...,
        index_labels: list[str] | None = ...,
        index_latex_labels: list[str] | None = ...,
        format_spec: _FormatSpec | None = ...,
        only_nonzero: bool = ...,
        only_nonredundant: bool = ...,
    ) -> FormattedExpansion: ...
    def swap_adjacent_indices(self, pos1: int, pos2: int, pos3: int) -> Self: ...
    def is_zero(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __pos__(self) -> Self: ...
    def __neg__(self) -> Self: ...
    def __add__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def __radd__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def __sub__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def __rsub__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def __mul__(
        self, other: Components[_Component, _Formatted, _FormatSpec]
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def __rmul__(self, other: _Component) -> Self: ...
    def __truediv__(self, other: _Component) -> Self: ...
    def trace(
        self, pos1: int, pos2: int
    ) -> Components | Components[Components, Components, Components]: ...
    def contract(
        self, *args: int | Components[_Component, _Formatted, _FormatSpec]
    ) -> _Component | Components[_Component, _Formatted, _FormatSpec]: ...
    def index_generator(self) -> Iterator: ...
    def non_redundant_index_generator(self) -> Iterator: ...
    def symmetrize(
        self, *pos: int
    ) -> CompWithSym[Components, Components, Components]: ...
    def antisymmetrize(
        self, *pos: int
    ) -> CompWithSym[Components, Components, Components]: ...

class CompWithSym(Components[_Component, _Formatted, _FormatSpec]):
    def __init__(
        self,
        ring: _Ring[_Component],
        frame: Sized,
        nb_indices: int,
        start_index: int = ...,
        output_formatter: _Formatter[_Component, _FormatSpec, _Formatted] | None = ...,
        sym: _Symmetry = ...,
        antisym: _Symmetry = ...,
    ) -> None: ...
    @overload
    def __getitem__(
        self, args: slice | list[slice]
    ) -> _ComponentValues[_Component] | _FormattedValues[_Formatted] | Matrix: ...
    @overload
    def __getitem__(
        self, args: tuple[_Index | slice | _FormatSpec, ...]
    ) -> _Component | _FormattedValues[_Formatted] | Matrix: ...
    @overload
    def __getitem__(self, args: _Access) -> _ComponentValues[CompWithSym] | Matrix: ...
    def __setitem__(
        self,
        args: _Access | tuple[_Index | slice | _FormatSpec, ...],
        value: _ComponentValues[_Component],
    ) -> None: ...
    def swap_adjacent_indices(self, pos1: int, pos2: int, pos3: int) -> Self: ...
    def __add__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def __mul__(
        self, other: Components[_Component, _Formatted, _FormatSpec]
    ) -> CompWithSym[_Component, _Formatted, _FormatSpec]: ...
    def trace(
        self, pos1: int, pos2: int
    ) -> CompWithSym | Components[CompWithSym, CompWithSym, CompWithSym]: ...
    def non_redundant_index_generator(self) -> Iterator: ...
    def symmetrize(
        self, *pos: int
    ) -> CompWithSym[CompWithSym, CompWithSym, CompWithSym]: ...
    def antisymmetrize(
        self, *pos: int
    ) -> CompWithSym[CompWithSym, CompWithSym, CompWithSym]: ...

class CompFullySym(CompWithSym[_Component, _Formatted, _FormatSpec]):
    def __init__(
        self,
        ring: _Ring[_Component],
        frame: Sized,
        nb_indices: int,
        start_index: int = ...,
        output_formatter: _Formatter[_Component, _FormatSpec, _Formatted] | None = ...,
    ) -> None: ...
    @overload
    def __getitem__(
        self, args: slice | list[slice]
    ) -> _ComponentValues[_Component] | _FormattedValues[_Formatted] | Matrix: ...
    @overload
    def __getitem__(
        self, args: tuple[_Index | slice | _FormatSpec, ...]
    ) -> _Component | _FormattedValues[_Formatted] | Matrix: ...
    @overload
    def __getitem__(self, args: _Access) -> _ComponentValues[CompFullySym] | Matrix: ...
    def __setitem__(
        self,
        args: _Access | tuple[_Index | slice | _FormatSpec, ...],
        value: _ComponentValues[_Component],
    ) -> None: ...
    def __add__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...

class CompFullyAntiSym(CompWithSym[_Component, _Formatted, _FormatSpec]):
    def __init__(
        self,
        ring: _Ring[_Component],
        frame: Sized,
        nb_indices: int,
        start_index: int = ...,
        output_formatter: _Formatter[_Component, _FormatSpec, _Formatted] | None = ...,
    ) -> None: ...
    def __add__(
        self, other: Components[_Component, _Formatted, _FormatSpec] | int | Integer
    ) -> Components[_Component, _Formatted, _FormatSpec]: ...
    def interior_product(
        self, other: CompFullyAntiSym[_Component, _Formatted, _FormatSpec]
    ) -> _Component | Components[_Component, _Formatted, _FormatSpec]: ...

class KroneckerDelta(CompFullySym[_Component, _Formatted, _FormatSpec]):
    def __init__(
        self,
        ring: _Ring[_Component],
        frame: Sized,
        start_index: int = ...,
        output_formatter: _Formatter[_Component, _FormatSpec, _Formatted] | int | None = ...,
    ) -> None: ...
    def __setitem__(
        self,
        args: _Access | tuple[_Index | slice | _FormatSpec, ...],
        value: _ComponentValues[_Component],
    ) -> None: ...
