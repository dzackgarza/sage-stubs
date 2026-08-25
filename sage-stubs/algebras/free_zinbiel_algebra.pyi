from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Generic, Literal, TypeVar, overload

from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.combinat.free_module import (
    CombinatorialCoercionResult,
    CombinatorialFreeModule,
)
from sage.combinat.words.finite_word import FiniteWord_class
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

_Letter = TypeVar("_Letter", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_FunctorScalar = TypeVar("_FunctorScalar", bound=RingElement)
_SourceScalar = TypeVar("_SourceScalar", bound=RingElement)
_TargetScalar = TypeVar("_TargetScalar", bound=RingElement)

type ZinbielSide = Literal["<", ">"]
type ZinbielWord[_Letter: Hashable] = FiniteWord_class[_Letter]
type ZinbielElement[_Letter: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[
    ZinbielWord[_Letter], _Scalar
]
type ZinbielTensorElement[_Letter: Hashable, _Scalar: RingElement] = (
    IndexedFreeModuleElement[
        tuple[ZinbielWord[_Letter], ZinbielWord[_Letter]],
        _Scalar,
    ]
)
type ZinbielNames[_Letter: Hashable] = str | Sequence[_Letter] | None
type ZinbielIndexSet[_Letter: Hashable] = (
    int | Integer | Parent[_Letter] | Iterable[_Letter]
)
type ZinbielElementInput[_Letter: Hashable, _Scalar: RingElement] = (
    ZinbielElement[_Letter, _Scalar] | ZinbielWord[_Letter] | Iterable[_Letter]
)

class FreeZinbielAlgebra(
    CombinatorialFreeModule,
    Generic[_Letter, _Scalar],
):
    product_on_basis: Callable[
        [ZinbielWord[_Letter], ZinbielWord[_Letter]],
        ZinbielElement[_Letter, _Scalar],
    ]

    @staticmethod
    def __classcall_private__(
        class_: type[FreeZinbielAlgebra[_Letter, _Scalar]],
        R: Ring,
        n: ZinbielIndexSet[_Letter] | ZinbielNames[_Letter] = ...,
        names: ZinbielNames[_Letter] = ...,
        prefix: str | None = ...,
        side: ZinbielSide | None = ...,
    ) -> FreeZinbielAlgebra[_Letter, _Scalar]: ...
    def __init__(
        self,
        R: Ring,
        n: ZinbielIndexSet[_Letter],
        names: tuple[_Letter, ...] | None,
        prefix: str,
        side: ZinbielSide,
    ) -> None: ...
    def _repr_term(self, t: ZinbielWord[_Letter]) -> str: ...
    def _repr_(self) -> str: ...
    def side(self) -> ZinbielSide: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def change_ring(
        self,
        R: Parent,
    ) -> FreeZinbielAlgebra[_Letter, RingElement]: ...
    def gens(
        self,
    ) -> tuple[ZinbielElement[_Letter, _Scalar], ...] | AbstractFamily: ...
    def degree_on_basis(self, t: ZinbielWord[_Letter]) -> int: ...
    def product_on_basis_left(
        self,
        x: ZinbielWord[_Letter],
        y: ZinbielWord[_Letter],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def product_on_basis_right(
        self,
        x: ZinbielWord[_Letter],
        y: ZinbielWord[_Letter],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def coproduct_on_basis(
        self,
        w: ZinbielWord[_Letter],
    ) -> ZinbielTensorElement[_Letter, _Scalar]: ...
    def counit(self, S: ZinbielElement[_Letter, _Scalar]) -> _Scalar: ...
    def _element_constructor_(
        self,
        x: ZinbielElementInput[_Letter, _Scalar],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def _coerce_map_from_(
        self,
        R: Parent | type,
        /,
    ) -> CombinatorialCoercionResult: ...
    def construction(
        self,
    ) -> tuple[ZinbielFunctor[_Letter], Parent[_Scalar]]: ...

class ZinbielFunctor(
    ConstructionFunctor,
    Generic[_Letter],
):
    rank: int
    vars: Parent[_Letter] | Sequence[_Letter]

    def __init__(
        self,
        variables: Parent[_Letter] | Iterable[_Letter],
        side: ZinbielSide,
    ) -> None: ...
    def _apply_functor(
        self,
        R: Parent[_FunctorScalar],
    ) -> FreeZinbielAlgebra[_Letter, _FunctorScalar]: ...
    @overload
    def _apply_functor_to_morphism(
        self,
        f: Morphism[Element, Element],
    ) -> Morphism[Element, Element]: ...
    @overload
    def _apply_functor_to_morphism(
        self,
        f: Morphism[_SourceScalar, _TargetScalar],
    ) -> ModuleMorphism[
        ZinbielWord[_Letter],
        ZinbielWord[_Letter],
        RingElement,
    ]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __mul__(self, other: ConstructionFunctor) -> ConstructionFunctor: ...
    def merge(
        self,
        other: ConstructionFunctor,
    ) -> ZinbielFunctor[_Letter] | None: ...
    def _repr_(self) -> str: ...
