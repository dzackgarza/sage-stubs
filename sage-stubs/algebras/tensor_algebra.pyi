from collections.abc import Hashable, Iterable, Sequence
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.combinat.free_module import CombinatorialFreeModule
from sage.monoids.indexed_free_monoid import IndexedFreeMonoidElement
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.ring import CommutativeRing
from sage.sets.family import AbstractFamily
from sage.structure.element import CommutativeRingElement
from sage.typeset.ascii_art import AsciiArt

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_DomainIndex = TypeVar("_DomainIndex", bound=Hashable)
_CodomainIndex = TypeVar("_CodomainIndex", bound=Hashable)
_Scalar = TypeVar("_Scalar", bound=CommutativeRingElement, default=CommutativeRingElement)

type TensorWord[_Index: Hashable] = IndexedFreeMonoidElement[_Index]
type TensorElement[_Index: Hashable, _Scalar: CommutativeRingElement] = IndexedFreeModuleElement[TensorWord[_Index], _Scalar]
type TensorSquareElement[_Index: Hashable, _Scalar: CommutativeRingElement] = IndexedFreeModuleElement[tuple[TensorWord[_Index], TensorWord[_Index]], _Scalar]

class TensorAlgebra(CombinatorialFreeModule, Generic[_Index, _Scalar]):
    Element: type[TensorElement[_Index, _Scalar]]
    element_class: type[TensorElement[_Index, _Scalar]]
    def __init__(
        self,
        M: CombinatorialFreeModule,
        prefix: str = ...,
        category: Category | None = ...,
        **options: object,
    ) -> None: ...
    def base_ring(self) -> CommutativeRing: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, m: TensorWord[_Index]) -> str: ...
    def _latex_term(self, m: TensorWord[_Index]) -> str: ...
    def _ascii_art_term(self, m: TensorWord[_Index]) -> AsciiArt | str: ...
    def _element_constructor_(
        self,
        x: TensorElement[_Index, _Scalar]
        | IndexedFreeModuleElement[_Index, _Scalar]
        | Iterable[_Index]
        | _Index
        | object,
    ) -> TensorElement[_Index, _Scalar]: ...
    def _tensor_constructor_(
        self,
        elts: Sequence[IndexedFreeModuleElement[_Index, _Scalar]],
    ) -> TensorElement[_Index, _Scalar]: ...
    def _coerce_map_from_(self, R: object) -> bool | Morphism: ...
    def construction(self) -> tuple[TensorAlgebraFunctor, CombinatorialFreeModule]: ...
    def degree_on_basis(self, m: TensorWord[_Index]) -> int: ...
    def base_module(self) -> CombinatorialFreeModule: ...
    def one_basis(self) -> TensorWord[_Index]: ...
    def algebra_generators(self) -> AbstractFamily: ...
    gens = algebra_generators
    def product_on_basis(
        self,
        a: TensorWord[_Index],
        b: TensorWord[_Index],
    ) -> TensorElement[_Index, _Scalar]: ...
    def counit(self, x: TensorElement[_Index, _Scalar]) -> _Scalar: ...
    def antipode_on_basis(
        self,
        m: TensorWord[_Index],
    ) -> TensorElement[_Index, _Scalar]: ...
    def coproduct_on_basis(
        self,
        m: TensorWord[_Index],
    ) -> TensorSquareElement[_Index, _Scalar]: ...

class TensorAlgebraFunctor(ConstructionFunctor, Generic[_Scalar]):
    rank: int
    def __init__(self, base: object) -> None: ...
    def _repr_(self) -> str: ...
    def _apply_functor(self, M: CombinatorialFreeModule) -> TensorAlgebra: ...
    def _apply_functor_to_morphism(
        self,
        f: ModuleMorphism[_DomainIndex, _CodomainIndex, _Scalar],
    ) -> ModuleMorphism[TensorWord[_DomainIndex], TensorWord[_CodomainIndex], _Scalar]: ...

class BaseRingLift(
    Morphism[_Scalar, TensorElement[_Index, _Scalar]],
    Generic[_Index, _Scalar],
):
    def codomain(self) -> TensorAlgebra[_Index, _Scalar]: ...
    def _call_(self, x: _Scalar) -> TensorElement[_Index, _Scalar]: ...
