from collections.abc import Hashable, Iterable, Iterator, Sequence
from typing import Generic, Protocol, TypeVar

from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.grossman_larson_algebras import (
    GrossmanLarsonAlgebra,
    GrossmanLarsonElement,
)
from sage.combinat.rooted_tree import LabelledRootedTree, RootedTree
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type PreLieTree = RootedTree | LabelledRootedTree
type PreLieNames = str | Sequence[Hashable] | int | Integer | object | None
type UnlabelledSortKey = tuple[int, ...]
type LabelledSortKey = tuple[tuple[int, object], ...]
type PreLieSortKey = UnlabelledSortKey | LabelledSortKey

class PreLieBilinearMap(
    Protocol,
    Generic[_Scalar],
):
    def __call__(
        self,
        left: FreePreLieElement[_Scalar],
        right: FreePreLieElement[_Scalar],
    ) -> FreePreLieElement[_Scalar]: ...

class FreePreLieElement(
    IndexedFreeModuleElement[PreLieTree, _Scalar],
    Generic[_Scalar],
):
    def parent(self) -> FreePreLieAlgebra[_Scalar]: ...
    def lift(self) -> GrossmanLarsonElement[_Scalar]: ...
    def valuation(self) -> int | PlusInfinity: ...

class FreePreLieAlgebra(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[FreePreLieElement[_Scalar]]
    element_class: type[FreePreLieElement[_Scalar]]
    pre_Lie_product: PreLieBilinearMap[_Scalar]
    nap_product: PreLieBilinearMap[_Scalar]

    @staticmethod
    def __classcall_private__(
        cls: type[FreePreLieAlgebra[_Scalar]],
        R: Ring,
        names: PreLieNames = ...,
    ) -> FreePreLieAlgebra[_Scalar]: ...
    def __init__(
        self,
        R: Ring,
        names: object | None = ...,
    ) -> None: ...
    def base_ring(self) -> Ring: ...
    def variable_names(self) -> object: ...
    def _repr_(self) -> str: ...
    def gen(
        self,
        i: int | Integer,
    ) -> FreePreLieElement[_Scalar]: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def change_ring(
        self,
        R: Ring,
    ) -> FreePreLieAlgebra[RingElement]: ...
    def gens(self) -> tuple[FreePreLieElement[_Scalar], ...]: ...
    def degree_on_basis(self, t: PreLieTree) -> int: ...
    def _an_element_(self) -> FreePreLieElement[_Scalar]: ...
    def some_elements(self) -> list[FreePreLieElement[_Scalar]]: ...
    def monomial(
        self,
        index: PreLieTree,
    ) -> FreePreLieElement[_Scalar]: ...
    def zero(self) -> FreePreLieElement[_Scalar]: ...
    def product_on_basis(
        self,
        x: PreLieTree,
        y: PreLieTree,
    ) -> FreePreLieElement[_Scalar]: ...
    pre_Lie_product_on_basis = product_on_basis
    def bracket_on_basis(
        self,
        x: PreLieTree,
        y: PreLieTree,
    ) -> FreePreLieElement[_Scalar]: ...
    def nap_product_on_basis(
        self,
        x: PreLieTree,
        y: PreLieTree,
    ) -> FreePreLieElement[_Scalar]: ...
    def corolla(
        self,
        x: FreePreLieElement[_Scalar],
        y: FreePreLieElement[_Scalar],
        n: int | Integer,
        N: int | Integer,
    ) -> FreePreLieElement[_Scalar]: ...
    def group_product(
        self,
        x: FreePreLieElement[_Scalar],
        y: FreePreLieElement[_Scalar],
        n: int | Integer,
        N: int | Integer = ...,
    ) -> FreePreLieElement[_Scalar]: ...
    def _element_constructor_(
        self,
        x: FreePreLieElement[_Scalar] | PreLieTree | object,
    ) -> FreePreLieElement[_Scalar]: ...
    def _coerce_map_from_(self, R: object) -> bool: ...
    def _construct_UEA(self) -> GrossmanLarsonAlgebra[_Scalar]: ...
    def construction(self) -> tuple[PreLieFunctor, Ring]: ...

class PreLieFunctor(ConstructionFunctor):
    rank: int
    vars: object

    def __init__(self, vars: object) -> None: ...
    def _apply_functor(
        self,
        R: Ring,
    ) -> FreePreLieAlgebra[RingElement]: ...
    def _apply_functor_to_morphism(
        self,
        f: Morphism[RingElement, RingElement],
    ) -> ModuleMorphism[
        PreLieTree,
        PreLieTree,
        RingElement,
    ]: ...
    def __eq__(self, other: object) -> bool: ...
    def __mul__(
        self,
        other: ConstructionFunctor,
    ) -> ConstructionFunctor: ...
    def merge(
        self,
        other: ConstructionFunctor,
    ) -> PreLieFunctor | None: ...
    def _repr_(self) -> str: ...

def tree_from_sortkey(
    ch: PreLieSortKey,
    labels: bool = ...,
) -> tuple[PreLieTree, PreLieSortKey]: ...
def corolla_gen(
    tx: PreLieTree,
    list_ty: Sequence[PreLieTree],
    labels: bool = ...,
) -> Iterator[PreLieTree]: ...
