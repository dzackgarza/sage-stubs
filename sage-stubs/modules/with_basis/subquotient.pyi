from collections.abc import Hashable, Iterable, Sequence
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import (
    ModuleMorphism,
    TriangularModuleMorphism,
)
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type AmbientElement[_Scalar: RingElement] = IndexedFreeModuleElement[Hashable, _Scalar]
type SubquotientElement[_Index: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_Index, _Scalar]

class SubmoduleWithBasis(
    CombinatorialFreeModule,
    Generic[_Index, _Scalar],
):
    lift: TriangularModuleMorphism[_Index, Hashable, _Scalar]
    reduce: ModuleMorphism[Hashable, Hashable, _Scalar]
    retract: ModuleMorphism[Hashable, _Index, _Scalar]

    @staticmethod
    def __classcall_private__(
        class_: type[SubmoduleWithBasis[_Index, _Scalar]],
        basis: AbstractFamily | Iterable[AmbientElement[_Scalar]],
        support_order: Sequence[Hashable],
        ambient: CombinatorialFreeModule | None = ...,
        unitriangular: bool = ...,
        category: Category | None = ...,
        *args: object,
        **opts: object,
    ) -> SubmoduleWithBasis[_Index, _Scalar]: ...
    def __init__(
        self,
        basis: AbstractFamily,
        support_order: tuple[Hashable, ...],
        ambient: CombinatorialFreeModule,
        unitriangular: bool,
        category: Category,
        *args: object,
        **opts: object,
    ) -> None: ...
    def ambient(self) -> CombinatorialFreeModule: ...
    def basis(self) -> AbstractFamily: ...
    def lift_on_basis(self, index: _Index) -> AmbientElement[_Scalar]: ...
    def is_submodule(
        self,
        other: CombinatorialFreeModule | SubmoduleWithBasis[Hashable, _Scalar],
    ) -> bool: ...

class QuotientModuleWithBasis(
    CombinatorialFreeModule,
    Generic[_Index, _Scalar],
):
    @staticmethod
    def __classcall_private__(
        class_: type[QuotientModuleWithBasis[_Index, _Scalar]],
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
        category: Category | None = ...,
    ) -> QuotientModuleWithBasis[_Index, _Scalar]: ...
    def __init__(
        self,
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
        category: Category,
        *args: object,
        **opts: object,
    ) -> None: ...
    def ambient(self) -> CombinatorialFreeModule: ...
    def relations(self) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def lift(
        self,
        x: SubquotientElement[_Index, _Scalar],
    ) -> AmbientElement[_Scalar]: ...
    def retract(
        self,
        x: AmbientElement[_Scalar],
    ) -> SubquotientElement[_Index, _Scalar]: ...

class SubquotientModuleWithBasis(
    QuotientModuleWithBasis[_Index, _Scalar],
    Generic[_Index, _Scalar],
):
    def __init__(
        self,
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
        relations: SubmoduleWithBasis[Hashable, _Scalar],
        category: Category | None = ...,
    ) -> None: ...
