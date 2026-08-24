from collections.abc import Callable, Hashable, Iterable
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.free_module import FreeModule_generic
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


class QuotientModuleWithBasis(
    CombinatorialFreeModule,
    Generic[_Index, _Scalar],
):
    def __init__(
        self,
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
        category: Category,
        *args: object,
        **opts: object,
    ) -> None: ...
    def ambient(self) -> CombinatorialFreeModule: ...
    def lift(
        self,
        x: SubquotientElement[_Index, _Scalar],
    ) -> AmbientElement[_Scalar]: ...
    def retract(
        self,
        x: AmbientElement[_Scalar],
    ) -> SubquotientElement[_Index, _Scalar]: ...


class SubmoduleWithBasis(
    CombinatorialFreeModule,
    Generic[_Index, _Scalar],
):
    lift_on_basis: Callable[[_Index], AmbientElement[_Scalar]]
    lift: TriangularModuleMorphism[_Index, Hashable, _Scalar]
    reduce: ModuleMorphism[Hashable, Hashable, _Scalar]
    retract: ModuleMorphism[Hashable, _Index, _Scalar]

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
    def _support_key(self, x: Hashable) -> int: ...
    def is_submodule(
        self,
        other: CombinatorialFreeModule | SubmoduleWithBasis[Hashable, _Scalar],
    ) -> bool: ...
    def _common_submodules(
        self,
        other: SubmoduleWithBasis[Hashable, _Scalar],
    ) -> tuple[FreeModule_generic[_Scalar], FreeModule_generic[_Scalar]]: ...
    def is_equal_subspace(
        self,
        other: CombinatorialFreeModule | SubmoduleWithBasis[Hashable, _Scalar],
    ) -> bool: ...
    def __add__(
        self,
        other: SubmoduleWithBasis[Hashable, _Scalar],
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def subspace_sum(
        self,
        other: SubmoduleWithBasis[Hashable, _Scalar],
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def __and__(
        self,
        other: CombinatorialFreeModule | SubmoduleWithBasis[Hashable, _Scalar],
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def intersection(
        self,
        other: CombinatorialFreeModule | SubmoduleWithBasis[Hashable, _Scalar],
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def __rand__(
        self,
        other: CombinatorialFreeModule | SubmoduleWithBasis[Hashable, _Scalar],
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def subspace(
        self,
        gens: Iterable[SubquotientElement[_Index, _Scalar]],
        *args: object,
        **opts: object,
    ) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
