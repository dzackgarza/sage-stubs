from collections.abc import Hashable
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.subquotient import SubmoduleWithBasis
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_CellIndex = TypeVar("_CellIndex", bound=Hashable, default=Hashable)
_BasisIndex = TypeVar("_BasisIndex", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class CellModuleElement(
    IndexedFreeModuleElement[_BasisIndex, _Scalar],
    Generic[_BasisIndex, _Scalar],
):
    pass


class CellModule(
    CombinatorialFreeModule,
    Generic[_CellIndex, _BasisIndex, _Scalar],
):
    Element: type[CellModuleElement[_BasisIndex, _Scalar]]
    def __init__(
        self,
        algebra: CombinatorialFreeModule,
        cell_index: _CellIndex,
        category: object | None = ...,
    ) -> None: ...
    def algebra(self) -> CombinatorialFreeModule: ...
    def cell_index(self) -> _CellIndex: ...
    def indices(self) -> object: ...
    def basis(self) -> AbstractFamily: ...
    def action(
        self,
        algebra_element: CombinatorialFreeModule.Element,
        module_element: CellModuleElement[_BasisIndex, _Scalar],
    ) -> CellModuleElement[_BasisIndex, _Scalar]: ...
    def bilinear_form(
        self,
        left: CellModuleElement[_BasisIndex, _Scalar],
        right: CellModuleElement[_BasisIndex, _Scalar],
    ) -> _Scalar: ...
    def gram_matrix(self) -> object: ...
    def radical(self) -> CellModuleSubmodule[_CellIndex, _BasisIndex, _Scalar]: ...
    def simple_module(self) -> CombinatorialFreeModule: ...


class CellModuleSubmodule(
    SubmoduleWithBasis[_BasisIndex, _Scalar],
    Generic[_CellIndex, _BasisIndex, _Scalar],
):
    def ambient(self) -> CellModule[_CellIndex, _BasisIndex, _Scalar]: ...
