from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.crystals.direct_sum import (
    CrystalElementProtocol,
    CrystalIndex,
)
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_AmbientElement = TypeVar(
    "_AmbientElement",
    bound=CrystalElementProtocol,
)
type CartanTypeInput = CartanType_abstract | Sequence[object] | str
type ContainmentPredicate[_AmbientElement] = (
    Callable[[_AmbientElement], bool]
    | Collection[_AmbientElement]
    | None
)
type VirtualizationInput = Mapping[
    CrystalIndex,
    Iterable[CrystalIndex],
]
type ScalingFactorsInput = Mapping[CrystalIndex, int | Integer]
type CrystalCardinality = int | Integer | PlusInfinity

class Subcrystal(
    UniqueRepresentation,
    Parent[Subcrystal.Element[_AmbientElement]],
    Generic[_AmbientElement],
):
    module_generators: tuple[Subcrystal.Element[_AmbientElement], ...]
    _ambient: Parent[_AmbientElement]
    _cartan_type: CartanType_abstract
    _index_set: tuple[CrystalIndex, ...]
    _containing: Callable[[_AmbientElement], bool]

    class Element(
        ElementWrapper,
        Generic[_AmbientElement],
    ):
        value: _AmbientElement
        def parent(self) -> Subcrystal[_AmbientElement]: ...
        def _richcmp_(
            self,
            other: Subcrystal.Element[_AmbientElement],
            op: int,
        ) -> bool: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self | None: ...
        def epsilon(self, i: CrystalIndex) -> int | Integer: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def weight(self) -> Element: ...

    Element: type[Element[_AmbientElement]]
    element_class: type[Element[_AmbientElement]]

    @staticmethod
    def __classcall_private__(
        cls: type[Subcrystal[_AmbientElement]],
        ambient: Parent[_AmbientElement],
        contained: ContainmentPredicate[_AmbientElement] = ...,
        generators: Iterable[_AmbientElement] | None = ...,
        virtualization: VirtualizationInput | None = ...,
        scaling_factors: ScalingFactorsInput | None = ...,
        cartan_type: CartanTypeInput | None = ...,
        index_set: Iterable[CrystalIndex] | None = ...,
        category: Category | None = ...,
    ) -> Subcrystal[_AmbientElement] | VirtualCrystal[_AmbientElement]: ...
    def __init__(
        self,
        ambient: Parent[_AmbientElement],
        contained: ContainmentPredicate[_AmbientElement],
        generators: tuple[_AmbientElement, ...],
        cartan_type: CartanType_abstract,
        index_set: tuple[CrystalIndex, ...],
        category: Category,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(
        self,
    ) -> Iterator[Subcrystal.Element[_AmbientElement]]: ...
    def list(self) -> list[Subcrystal.Element[_AmbientElement]]: ...
    def cardinality(self) -> CrystalCardinality: ...
    def index_set(self) -> tuple[CrystalIndex, ...]: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def weight_lattice_realization(self) -> Parent: ...

from sage.combinat.crystals.virtual_crystal import VirtualCrystal
