from collections.abc import Hashable, Mapping
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.modules.with_basis.subquotient import QuotientModuleWithBasis
from sage.rings.integer import Integer
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type HochschildDegree = int | Integer
type HochschildModuleElement[_Scalar: RingElement] = (
    IndexedFreeModuleElement[Hashable, _Scalar]
)
type HochschildChainData[_Scalar: RingElement] = Mapping[
    HochschildDegree,
    HochschildModuleElement[_Scalar],
]
type HochschildDifferential[_Scalar: RingElement] = ModuleMorphism[
    Hashable,
    Hashable,
    _Scalar,
]
type HochschildHomology[_Scalar: RingElement] = QuotientModuleWithBasis[
    Hashable,
    _Scalar,
]


class HochschildComplex(
    UniqueRepresentation,
    Parent[HochschildComplex.Element],
    Generic[_Scalar],
):
    class Element(ModuleElement, Generic[_Scalar]):
        def __init__(
            self,
            parent: HochschildComplex[_Scalar],
            vectors: HochschildChainData[_Scalar],
        ) -> None: ...
        def parent(self) -> HochschildComplex[_Scalar]: ...
        def vector(
            self,
            degree: HochschildDegree,
        ) -> HochschildModuleElement[_Scalar]: ...
        def _repr_(self) -> str: ...
        def _add_(
            self,
            other: HochschildComplex.Element[_Scalar],
        ) -> HochschildComplex.Element[_Scalar]: ...
        def _lmul_(
            self,
            scalar: _Scalar,
        ) -> HochschildComplex.Element[_Scalar]: ...
        def _richcmp_(
            self,
            other: HochschildComplex.Element[_Scalar],
            op: int,
        ) -> bool: ...

    element_class: type[Element[_Scalar]]
    Element = Element

    def __init__(
        self,
        A: CombinatorialFreeModule,
        M: CombinatorialFreeModule,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def algebra(self) -> CombinatorialFreeModule: ...
    def coefficients(self) -> CombinatorialFreeModule: ...
    def module(
        self,
        d: HochschildDegree,
    ) -> CombinatorialFreeModule: ...
    def trivial_module(self) -> CombinatorialFreeModule: ...
    def boundary(
        self,
        d: HochschildDegree,
    ) -> HochschildDifferential[_Scalar]: ...
    differential = boundary
    def coboundary(
        self,
        d: HochschildDegree,
    ) -> HochschildDifferential[_Scalar]: ...
    def homology(
        self,
        d: HochschildDegree,
    ) -> HochschildHomology[_Scalar]: ...
    def cohomology(
        self,
        d: HochschildDegree,
    ) -> HochschildHomology[_Scalar]: ...
    def _element_constructor_(
        self,
        vectors: HochschildChainData[_Scalar]
        | HochschildComplex.Element[_Scalar]
        | int,
    ) -> HochschildComplex.Element[_Scalar]: ...
    def zero(self) -> HochschildComplex.Element[_Scalar]: ...
    def _an_element_(self) -> HochschildComplex.Element[_Scalar]: ...
