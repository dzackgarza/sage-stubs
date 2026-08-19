from collections.abc import Hashable, Iterable, Sequence
from typing import Generic, Protocol, TypeVar

from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.combinat.binary_tree import BinaryTree, LabelledBinaryTree
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.morphism import ModuleMorphism
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type DendriformTree = BinaryTree | LabelledBinaryTree
type DendriformElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    DendriformTree,
    _Scalar,
]
type DendriformTensorElement[_Scalar: RingElement] = IndexedFreeModuleElement[
    tuple[DendriformTree, DendriformTree],
    _Scalar,
]
type DendriformNames = str | Sequence[Hashable] | object | None

class DendriformBilinearMap(
    Protocol,
    Generic[_Scalar],
):
    def __call__(
        self,
        left: DendriformElement[_Scalar],
        right: DendriformElement[_Scalar],
    ) -> DendriformElement[_Scalar]: ...

class FreeDendriformAlgebra(
    CombinatorialFreeModule,
    Generic[_Scalar],
):
    Element: type[DendriformElement[_Scalar]]
    element_class: type[DendriformElement[_Scalar]]
    succ: DendriformBilinearMap[_Scalar]
    prec: DendriformBilinearMap[_Scalar]
    over: DendriformBilinearMap[_Scalar]
    under: DendriformBilinearMap[_Scalar]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeDendriformAlgebra[_Scalar]],
        R: Ring,
        names: DendriformNames = ...,
    ) -> FreeDendriformAlgebra[_Scalar]: ...
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
    ) -> DendriformElement[_Scalar]: ...
    def algebra_generators(self) -> AbstractFamily: ...
    def change_ring(
        self,
        R: Ring,
    ) -> FreeDendriformAlgebra[RingElement]: ...
    def gens(self) -> tuple[DendriformElement[_Scalar], ...]: ...
    def degree_on_basis(self, t: DendriformTree) -> int: ...
    def _an_element_(self) -> DendriformElement[_Scalar]: ...
    def some_elements(self) -> list[DendriformElement[_Scalar]]: ...
    def one_basis(self) -> DendriformTree: ...
    def one(self) -> DendriformElement[_Scalar]: ...
    def zero(self) -> DendriformElement[_Scalar]: ...
    def monomial(
        self,
        index: DendriformTree,
    ) -> DendriformElement[_Scalar]: ...
    def product_on_basis(
        self,
        x: DendriformTree,
        y: DendriformTree,
    ) -> DendriformElement[_Scalar]: ...
    def succ_product_on_basis(
        self,
        x: DendriformTree,
        y: DendriformTree,
    ) -> DendriformElement[_Scalar]: ...
    def prec_product_on_basis(
        self,
        x: DendriformTree,
        y: DendriformTree,
    ) -> DendriformElement[_Scalar]: ...
    def coproduct_on_basis(
        self,
        x: DendriformTree,
    ) -> DendriformTensorElement[_Scalar]: ...
    def _element_constructor_(
        self,
        x: DendriformElement[_Scalar]
        | DendriformTree
        | object,
    ) -> DendriformElement[_Scalar]: ...
    def _coerce_map_from_(self, R: object) -> bool: ...
    def construction(self) -> tuple[DendriformFunctor, Ring]: ...

class DendriformFunctor(ConstructionFunctor):
    rank: int
    vars: object

    def __init__(self, vars: object) -> None: ...
    def _apply_functor(
        self,
        R: Ring,
    ) -> FreeDendriformAlgebra[RingElement]: ...
    def _apply_functor_to_morphism(
        self,
        f: Morphism[RingElement, RingElement],
    ) -> ModuleMorphism[
        DendriformTree,
        DendriformTree,
        RingElement,
    ]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __mul__(
        self,
        other: ConstructionFunctor,
    ) -> ConstructionFunctor: ...
    def merge(
        self,
        other: ConstructionFunctor,
    ) -> DendriformFunctor | None: ...
    def _repr_(self) -> str: ...
