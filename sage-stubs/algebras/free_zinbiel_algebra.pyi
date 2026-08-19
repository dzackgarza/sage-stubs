from collections.abc import Callable, Hashable, Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.words.finite_word import FiniteWord_class
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
type ZinbielSide = Literal["<", ">"]
type ZinbielElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    FiniteWord_class,
    _Scalar,
]
type ZinbielTensorElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    tuple[FiniteWord_class, FiniteWord_class],
    _Scalar,
]
type ZinbielNames = str | Sequence[Hashable] | None
type ZinbielIndexSet = int | Integer | object

class FreeZinbielAlgebra(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[ZinbielElement[_Scalar]]
    element_class: type[ZinbielElement[_Scalar]]
    product_on_basis: Callable[
        [FiniteWord_class, FiniteWord_class],
        ZinbielElement[_Scalar],
    ]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeZinbielAlgebra[_Scalar]],
        R: Ring,
        n: ZinbielIndexSet | ZinbielNames = ...,
        names: ZinbielNames = ...,
        prefix: str | None = ...,
        side: ZinbielSide | None = ...,
    ) -> FreeZinbielAlgebra[_Scalar]: ...
    def __init__(
        self,
        R: Ring,
        n: ZinbielIndexSet,
        names: tuple[Hashable, ...] | None,
        prefix: str,
        side: ZinbielSide,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def _repr_term(self, t: FiniteWord_class) -> str: ...
    def _repr_(self) -> str: ...
    def side(self) -> ZinbielSide: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def change_ring(
        self,
        R: Ring,
    ) -> FreeZinbielAlgebra[RingElement]: ...
    def gens(
        self,
    ) -> tuple[ZinbielElement[_Scalar], ...] | AbstractFamily: ...
    def degree_on_basis(self, t: FiniteWord_class) -> int: ...
    def monomial(
        self,
        index: FiniteWord_class,
    ) -> ZinbielElement[_Scalar]: ...
    def zero(self) -> ZinbielElement[_Scalar]: ...
    def product_on_basis_left(
        self,
        x: FiniteWord_class,
        y: FiniteWord_class,
    ) -> ZinbielElement[_Scalar]: ...
    def product_on_basis_right(
        self,
        x: FiniteWord_class,
        y: FiniteWord_class,
    ) -> ZinbielElement[_Scalar]: ...
    def coproduct_on_basis(
        self,
        w: FiniteWord_class,
    ) -> ZinbielTensorElement[_Scalar]: ...
    def counit(self, S: ZinbielElement[_Scalar]) -> _Scalar: ...
    def _element_constructor_(
        self,
        x: ZinbielElement[_Scalar] | FiniteWord_class | object,
    ) -> ZinbielElement[_Scalar]: ...
    def _coerce_map_from_(
        self,
        R: object,
    ) -> bool | Morphism | None: ...
    def construction(self) -> tuple[ZinbielFunctor, Ring]: ...

class ZinbielFunctor(ConstructionFunctor):
    rank: int
    vars: object

    def __init__(
        self,
        variables: object,
        side: ZinbielSide,
    ) -> None: ...
    def _apply_functor(
        self,
        R: Ring,
    ) -> FreeZinbielAlgebra[RingElement]: ...
    def _apply_functor_to_morphism(
        self,
        f: Morphism[RingElement, RingElement],
    ) -> ModuleMorphism[
        FiniteWord_class,
        FiniteWord_class,
        RingElement,
    ]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __mul__(
        self,
        other: ConstructionFunctor,
    ) -> ConstructionFunctor: ...
    def merge(
        self,
        other: ConstructionFunctor,
    ) -> ZinbielFunctor | None: ...
    def _repr_(self) -> str: ...
