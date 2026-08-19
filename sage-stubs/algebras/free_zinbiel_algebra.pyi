from collections.abc import Hashable, Iterable, Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.category import Category
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
from sage.structure.parent import ElementConstructorInput, Parent

_Letter = TypeVar("_Letter", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type ZinbielSide = Literal["<", ">"]
type ZinbielElement[
    _Letter: Hashable,
    _Scalar: RingElement,
] = IndexedFreeModuleElement[FiniteWord_class[_Letter], _Scalar]
type ZinbielTensorElement[
    _Letter: Hashable,
    _Scalar: RingElement,
] = IndexedFreeModuleElement[
    tuple[FiniteWord_class[_Letter], FiniteWord_class[_Letter]],
    _Scalar,
]
type ZinbielNames[_Letter: Hashable] = (
    str
    | Sequence[_Letter]
    | Parent[_Letter]
    | None
)
type ZinbielIndexSet[_Letter: Hashable] = (
    int
    | Integer
    | Parent[_Letter]
    | Iterable[_Letter]
)


class FreeZinbielAlgebra(
    CombinatorialFreeModule,
    Generic[_Letter, _Scalar],
):
    Element: type[ZinbielElement[_Letter, _Scalar]]
    element_class: type[ZinbielElement[_Letter, _Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeZinbielAlgebra[_Letter, _Scalar]],
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
    def base_ring(self) -> Ring: ...
    def variable_names(self) -> tuple[_Letter, ...] | Parent[_Letter]: ...
    def _repr_term(self, t: FiniteWord_class[_Letter]) -> str: ...
    def _repr_(self) -> str: ...
    def side(self) -> ZinbielSide: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def change_ring(
        self,
        R: Ring,
    ) -> FreeZinbielAlgebra[_Letter, RingElement]: ...
    def gens(
        self,
    ) -> tuple[ZinbielElement[_Letter, _Scalar], ...] | AbstractFamily: ...
    def gen(self, i: int | Integer) -> ZinbielElement[_Letter, _Scalar]: ...
    def degree_on_basis(self, t: FiniteWord_class[_Letter]) -> int: ...
    def monomial(
        self,
        index: FiniteWord_class[_Letter],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def zero(self) -> ZinbielElement[_Letter, _Scalar]: ...
    def product_on_basis_left(
        self,
        x: FiniteWord_class[_Letter],
        y: FiniteWord_class[_Letter],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def product_on_basis_right(
        self,
        x: FiniteWord_class[_Letter],
        y: FiniteWord_class[_Letter],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def product_on_basis(
        self,
        x: FiniteWord_class[_Letter],
        y: FiniteWord_class[_Letter],
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def coproduct_on_basis(
        self,
        w: FiniteWord_class[_Letter],
    ) -> ZinbielTensorElement[_Letter, _Scalar]: ...
    def counit(self, S: ZinbielElement[_Letter, _Scalar]) -> _Scalar: ...
    def _element_constructor_(
        self,
        x: ZinbielElement[_Letter, _Scalar]
        | FiniteWord_class[_Letter]
        | Iterable[_Letter]
        | _Scalar
        | ElementConstructorInput,
    ) -> ZinbielElement[_Letter, _Scalar]: ...
    def _coerce_map_from_(
        self,
        R: Ring | FreeZinbielAlgebra,
    ) -> bool | Morphism | None: ...
    def construction(
        self,
    ) -> tuple[ZinbielFunctor[_Letter], Ring]: ...


class ZinbielFunctor(
    ConstructionFunctor,
    Generic[_Letter],
):
    rank: int
    vars: Parent[_Letter] | tuple[_Letter, ...]

    def __init__(
        self,
        variables: Parent[_Letter] | Iterable[_Letter],
        side: ZinbielSide,
    ) -> None: ...
    def _apply_functor(
        self,
        R: Ring,
    ) -> FreeZinbielAlgebra[_Letter, RingElement]: ...
    def _apply_functor_to_morphism(
        self,
        f: Morphism[RingElement, RingElement],
    ) -> ModuleMorphism[
        FiniteWord_class[_Letter],
        FiniteWord_class[_Letter],
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
    ) -> ZinbielFunctor[_Letter] | None: ...
    def _repr_(self) -> str: ...
