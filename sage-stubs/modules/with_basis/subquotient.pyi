from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import TriangularModuleMorphism
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class SubmoduleWithBasis(
    CombinatorialFreeModule,
    Generic[_Index, _Scalar],
):
    def __init__(
        self,
        basis: AbstractFamily,
        support_order: object | None = ...,
        ambient: CombinatorialFreeModule | None = ...,
        unitriangular: bool = ...,
        category: object | None = ...,
    ) -> None: ...
    def ambient(self) -> CombinatorialFreeModule: ...
    def basis(self) -> AbstractFamily: ...
    def lift(
        self,
        x: IndexedFreeModuleElement[_Index, _Scalar],
    ) -> IndexedFreeModuleElement[Hashable, _Scalar]: ...
    def retract(
        self,
        x: IndexedFreeModuleElement[Hashable, _Scalar],
    ) -> IndexedFreeModuleElement[_Index, _Scalar]: ...
    def lift_morphism(self) -> TriangularModuleMorphism: ...
    def retract_morphism(self) -> TriangularModuleMorphism: ...
    def is_submodule(self, other: CombinatorialFreeModule) -> bool: ...


class QuotientModuleWithBasis(
    CombinatorialFreeModule,
    Generic[_Index, _Scalar],
):
    def __init__(
        self,
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
        category: object | None = ...,
    ) -> None: ...
    def ambient(self) -> CombinatorialFreeModule: ...
    def relations(self) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def lift(
        self,
        x: IndexedFreeModuleElement[_Index, _Scalar],
    ) -> IndexedFreeModuleElement[Hashable, _Scalar]: ...
    def retract(
        self,
        x: IndexedFreeModuleElement[Hashable, _Scalar],
    ) -> IndexedFreeModuleElement[_Index, _Scalar]: ...
    def quotient_map(self) -> TriangularModuleMorphism: ...
    def lift_map(self) -> TriangularModuleMorphism: ...


class SubquotientModuleWithBasis(
    QuotientModuleWithBasis[_Index, _Scalar],
    Generic[_Index, _Scalar],
):
    def __init__(
        self,
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
        relations: SubmoduleWithBasis[Hashable, _Scalar],
        category: object | None = ...,
    ) -> None: ...
