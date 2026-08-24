from collections.abc import Hashable, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.morphism import Morphism
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.module import Module
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.subquotient import (
    QuotientModuleWithBasis,
    SubmoduleWithBasis,
)
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import ElementConstructorInput

_CellIndex = TypeVar("_CellIndex", bound=Hashable, default=Hashable)
_BasisIndex = TypeVar("_BasisIndex", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_SourceElement = TypeVar("_SourceElement", bound=ModuleElement)

type CellElement[_BasisIndex: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_BasisIndex, _Scalar]


class CellModule(
    CombinatorialFreeModule,
    Generic[_CellIndex, _BasisIndex, _Scalar],
):
    @staticmethod
    def __classcall_private__(
        class_: type[CellModule[_CellIndex, _BasisIndex, _Scalar]],
        A: CombinatorialFreeModule,
        mu: _CellIndex,
        **kwds: object,
    ) -> CellModule[_CellIndex, _BasisIndex, _Scalar]: ...
    def __init__(
        self,
        A: CombinatorialFreeModule,
        mu: _CellIndex,
        **kwds: object,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def cellular_algebra(self) -> CombinatorialFreeModule: ...
    def _action_basis(
        self,
        x: Hashable,
        s: _BasisIndex,
    ) -> CellElement[_BasisIndex, _Scalar]: ...
    def _bilinear_form_on_basis(
        self,
        s: _BasisIndex,
        t: _BasisIndex,
    ) -> _Scalar: ...
    def bilinear_form(
        self,
        x: CellElement[_BasisIndex, _Scalar],
        y: CellElement[_BasisIndex, _Scalar],
    ) -> _Scalar: ...
    def bilinear_form_matrix(
        self,
        ordering: Sequence[_BasisIndex] | None = ...,
    ) -> Matrix[_Scalar]: ...
    def nonzero_bilinear_form(self) -> bool: ...
    def radical_basis(
        self,
    ) -> tuple[CellElement[_BasisIndex, _Scalar], ...]: ...
    def radical(self) -> SubmoduleWithBasis[Hashable, _Scalar]: ...
    def simple_module(
        self,
    ) -> SimpleModule[_CellIndex, _BasisIndex, _Scalar]: ...

    class Element(CombinatorialFreeModule.Element):
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...
        def _lmul_(self, scalar: ElementConstructorInput) -> Self | None: ...
        def _rmul_(self, scalar: ElementConstructorInput) -> Self | None: ...


class SimpleModule(
    QuotientModuleWithBasis[_BasisIndex, _Scalar],
    Generic[_CellIndex, _BasisIndex, _Scalar],
):
    def __init__(
        self,
        submodule: SubmoduleWithBasis[Hashable, _Scalar],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _coerce_map_from_(
        self,
        M: Module[RingElement, _SourceElement],
    ) -> Morphism[_SourceElement, ModuleElement] | None: ...

    class Element(QuotientModuleWithBasis.Element):
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...
        def _lmul_(self, scalar: ElementConstructorInput) -> Self | None: ...
        def _rmul_(self, scalar: ElementConstructorInput) -> Self | None: ...
