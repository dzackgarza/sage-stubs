from collections.abc import Iterable, Iterator
from typing import Generic, Literal, Self, TypeVar, overload

from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.unique_representation import UniqueRepresentation
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule_abstract
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm
from sage.tensor.modules.free_module_automorphism import FreeModuleAutomorphism
from sage.tensor.modules.free_module_element import FiniteRankFreeModuleElement

type _Index = int | Integer
type _Symbol = str | tuple[str, ...] | list[str]
type _Indices = tuple[str, ...] | list[str] | None
type _BasisElement = FiniteRankFreeModuleElement | FreeModuleAltForm
_BasisKey = TypeVar("_BasisKey")
_BasisValue = TypeVar("_BasisValue")

class Basis_abstract(UniqueRepresentation, AbstractFamily, Generic[_BasisKey, _BasisValue]):
    def __init__(
        self,
        fmodule: FiniteRankFreeModule_abstract,
        symbol: _Symbol,
        latex_symbol: _Symbol | None,
        indices: _Indices,
        latex_indices: _Indices,
    ) -> None: ...
    def keys(self) -> Iterator[_BasisKey]: ...
    def values(self) -> Iterable[_BasisValue]: ...
    def _element_constructor_(self, x: _BasisValue) -> _BasisValue: ...
    def __iter__(self) -> Iterator[_BasisValue]: ...
    def __len__(self) -> int: ...
    def cardinality(self) -> Integer: ...
    def __getitem__(self, index: _BasisKey) -> _BasisValue: ...
    def _latex_(self) -> str: ...
    def free_module(self) -> FiniteRankFreeModule_abstract: ...
    def set_name(
        self,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
        index_position: Literal["down", "up"] = ...,
    ) -> None: ...

class FreeModuleCoBasis(Basis_abstract[_Index, FreeModuleAltForm]):
    def __init__(
        self,
        basis: FreeModuleBasis,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...

class FreeModuleBasis(Basis_abstract[_Index, _BasisElement]):
    _cobasis_class: type[FreeModuleCoBasis]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeModuleBasis],
        fmodule: FiniteRankFreeModule_abstract,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
        symbol_dual: _Symbol | None = ...,
        latex_symbol_dual: _Symbol | None = ...,
    ) -> FreeModuleBasis: ...
    def __init__(
        self,
        fmodule: FiniteRankFreeModule_abstract,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
        symbol_dual: _Symbol | None = ...,
        latex_symbol_dual: _Symbol | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    @overload
    def __getitem__(self, index: slice) -> tuple[_BasisElement, ...]: ...
    @overload
    def __getitem__(self, index: _Index) -> _BasisElement: ...
    def _new_instance(
        self,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
        symbol_dual: _Symbol | None = ...,
        latex_symbol_dual: _Symbol | None = ...,
    ) -> Self: ...
    def _init_from_family(self, family: Iterable[FiniteRankFreeModuleElement]) -> None: ...
    def module(self) -> FiniteRankFreeModule_abstract: ...
    def dual_basis(self) -> FreeModuleCoBasis: ...
    def new_basis(
        self,
        change_of_basis: FreeModuleAutomorphism,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
        symbol_dual: _Symbol | None = ...,
        latex_symbol_dual: _Symbol | None = ...,
    ) -> Self: ...
