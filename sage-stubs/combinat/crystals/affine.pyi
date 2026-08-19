from collections.abc import Callable, Iterator, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.crystals.direct_sum import (
    CrystalElementProtocol,
    CrystalIndex,
)
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_ClassicalElement = TypeVar(
    "_ClassicalElement",
    bound=CrystalElementProtocol,
)
type CartanTypeInput = CartanType_abstract | Sequence[object] | str
type CrystalCardinality = int | Integer

class AffineCrystalFromClassical(
    UniqueRepresentation,
    Parent[AffineCrystalFromClassicalElement[_ClassicalElement]],
    Generic[_ClassicalElement],
):
    Element: type[AffineCrystalFromClassicalElement[_ClassicalElement]]
    element_class: type[AffineCrystalFromClassicalElement[_ClassicalElement]]
    classical_crystal: Parent[_ClassicalElement]
    module_generators: list[
        AffineCrystalFromClassicalElement[_ClassicalElement]
    ]

    @staticmethod
    def __classcall__(
        cls: type[AffineCrystalFromClassical[_ClassicalElement]],
        cartan_type: CartanTypeInput,
        *args: object,
        **options: object,
    ) -> AffineCrystalFromClassical[_ClassicalElement]: ...
    def __init__(
        self,
        cartan_type: CartanType_abstract,
        classical_crystal: Parent[_ClassicalElement],
        category: Category | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def cardinality(self) -> CrystalCardinality: ...
    def __iter__(
        self,
    ) -> Iterator[AffineCrystalFromClassicalElement[_ClassicalElement]]: ...
    def lift(
        self,
        affine_elt: AffineCrystalFromClassicalElement[_ClassicalElement],
    ) -> _ClassicalElement: ...
    def retract(
        self,
        classical_elt: _ClassicalElement,
    ) -> AffineCrystalFromClassicalElement[_ClassicalElement]: ...
    def _element_constructor_(
        self,
        *value: object,
        **options: object,
    ) -> AffineCrystalFromClassicalElement[_ClassicalElement]: ...
    def __contains__(self, x: object) -> bool: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[CrystalIndex, ...]: ...
    def weight_lattice_realization(self) -> Parent: ...

class AffineCrystalFromClassicalElement(
    ElementWrapper,
    Generic[_ClassicalElement],
):
    value: _ClassicalElement
    def parent(
        self,
    ) -> AffineCrystalFromClassical[_ClassicalElement]: ...
    def classical_weight(self) -> Element: ...
    def lift(self) -> _ClassicalElement: ...
    def pp(self) -> object: ...
    def e0(self) -> Self | None: ...
    def f0(self) -> Self | None: ...
    def e(self, i: CrystalIndex) -> Self | None: ...
    def f(self, i: CrystalIndex) -> Self | None: ...
    def epsilon0(self) -> int | Integer: ...
    def epsilon(self, i: CrystalIndex) -> int | Integer: ...
    def phi0(self) -> int | Integer: ...
    def phi(self, i: CrystalIndex) -> int | Integer: ...
    def weight(self) -> Element: ...
    def _richcmp_(
        self,
        other: AffineCrystalFromClassicalElement[_ClassicalElement],
        op: int,
    ) -> bool: ...

class AffineCrystalFromClassicalAndPromotion(
    AffineCrystalFromClassical[_ClassicalElement],
    Generic[_ClassicalElement],
):
    Element: type[
        AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement]
    ]
    element_class: type[
        AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement]
    ]
    p_automorphism: Callable[[_ClassicalElement], _ClassicalElement]
    p_inverse_automorphism: Callable[[_ClassicalElement], _ClassicalElement]
    dynkin_node: CrystalIndex

    def __init__(
        self,
        cartan_type: CartanType_abstract,
        classical_crystal: Parent[_ClassicalElement],
        p_automorphism: Callable[[_ClassicalElement], _ClassicalElement],
        p_inverse_automorphism: Callable[[_ClassicalElement], _ClassicalElement],
        dynkin_node: CrystalIndex,
        category: Category | None = ...,
    ) -> None: ...
    def retract(
        self,
        classical_elt: _ClassicalElement,
    ) -> AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement]: ...
    def automorphism(
        self,
        x: AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement],
    ) -> AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement]: ...
    def inverse_automorphism(
        self,
        x: AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement],
    ) -> AffineCrystalFromClassicalAndPromotionElement[_ClassicalElement]: ...

class AffineCrystalFromClassicalAndPromotionElement(
    AffineCrystalFromClassicalElement[_ClassicalElement],
    Generic[_ClassicalElement],
):
    def parent(
        self,
    ) -> AffineCrystalFromClassicalAndPromotion[_ClassicalElement]: ...
    def e0(self) -> Self | None: ...
    def f0(self) -> Self | None: ...
    def epsilon0(self) -> int | Integer: ...
    def phi0(self) -> int | Integer: ...
