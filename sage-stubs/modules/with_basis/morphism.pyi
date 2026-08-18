from collections.abc import Callable, Hashable
from typing import Generic, TypeVar

from sage.categories.morphism import Morphism
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.structure.element import RingElement

_DomainIndex = TypeVar("_DomainIndex", bound=Hashable, default=Hashable)
_CodomainIndex = TypeVar("_CodomainIndex", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class ModuleMorphismByLinearity(
    Morphism[
        IndexedFreeModuleElement[_DomainIndex, _Scalar],
        IndexedFreeModuleElement[_CodomainIndex, _Scalar],
    ],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        parent: object,
        on_basis: Callable[
            [_DomainIndex],
            IndexedFreeModuleElement[_CodomainIndex, _Scalar],
        ],
        position: int = ...,
        zero: object | None = ...,
    ) -> None: ...
    def on_basis(
        self,
        index: _DomainIndex,
    ) -> IndexedFreeModuleElement[_CodomainIndex, _Scalar]: ...
    def _call_(
        self,
        x: IndexedFreeModuleElement[_DomainIndex, _Scalar],
    ) -> IndexedFreeModuleElement[_CodomainIndex, _Scalar]: ...


class DiagonalModuleMorphism(
    ModuleMorphismByLinearity[_DomainIndex, _DomainIndex, _Scalar],
    Generic[_DomainIndex, _Scalar],
):
    def __init__(
        self,
        parent: object,
        diagonal: Callable[[_DomainIndex], _Scalar],
    ) -> None: ...
    def diagonal(self, index: _DomainIndex) -> _Scalar: ...
    def inverse(self) -> DiagonalModuleMorphism[_DomainIndex, _Scalar]: ...
    __invert__ = inverse


class TriangularModuleMorphism(
    ModuleMorphismByLinearity[_DomainIndex, _CodomainIndex, _Scalar],
    Generic[_DomainIndex, _CodomainIndex, _Scalar],
):
    def __init__(
        self,
        parent: object,
        on_basis: Callable[
            [_DomainIndex],
            IndexedFreeModuleElement[_CodomainIndex, _Scalar],
        ],
        triangular: str = ...,
        unitriangular: bool = ...,
        key: Callable[[_CodomainIndex], object] | None = ...,
        inverse_on_support: Callable[[_CodomainIndex], _DomainIndex] | None = ...,
    ) -> None: ...
    def triangular(self) -> str: ...
    def is_unitriangular(self) -> bool: ...
    def preimage(
        self,
        x: IndexedFreeModuleElement[_CodomainIndex, _Scalar],
    ) -> IndexedFreeModuleElement[_DomainIndex, _Scalar]: ...
    def section(
        self,
    ) -> TriangularModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar]: ...
    def inverse(self) -> TriangularModuleMorphism[_CodomainIndex, _DomainIndex, _Scalar]: ...
    __invert__ = inverse
