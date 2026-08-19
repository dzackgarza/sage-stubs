from collections.abc import Iterable, Iterator
from typing import Generic, Protocol, Self, TypeVar

from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.integer import Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets
from sage.sets.family import AbstractFamily
from sage.structure.element import Element
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent

_CrystalElement = TypeVar("_CrystalElement", bound="CrystalElementProtocol")
type CrystalIndex = int | Integer | str

class CrystalElementProtocol(Protocol):
    def e(self, i: CrystalIndex) -> Self | None: ...
    def f(self, i: CrystalIndex) -> Self | None: ...
    def weight(self) -> Element: ...
    def phi(self, i: CrystalIndex) -> int | Integer: ...
    def epsilon(self, i: CrystalIndex) -> int | Integer: ...

class DirectSumOfCrystals(
    DisjointUnionEnumeratedSets,
    Generic[_CrystalElement],
):
    crystals: AbstractFamily
    module_generators: tuple[
        _CrystalElement | DirectSumOfCrystals.Element[_CrystalElement],
        ...,
    ]

    class Element(
        ElementWrapper,
        Generic[_CrystalElement],
    ):
        value: tuple[int, _CrystalElement]
        def parent(
            self,
        ) -> DirectSumOfCrystals[_CrystalElement]: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self | None: ...
        def weight(self) -> Element: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def epsilon(self, i: CrystalIndex) -> int | Integer: ...

    @staticmethod
    def __classcall_private__(
        cls: type[DirectSumOfCrystals[_CrystalElement]],
        crystals: Iterable[Parent[_CrystalElement]],
        facade: bool = ...,
        keepkey: bool = ...,
        category: object | None = ...,
    ) -> DirectSumOfCrystals[_CrystalElement]: ...
    def __init__(
        self,
        crystals: AbstractFamily,
        facade: bool,
        keepkey: bool,
        category: object,
        **options: object,
    ) -> None: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def weight_lattice_realization(self) -> Parent: ...
    def __iter__(
        self,
    ) -> Iterator[
        _CrystalElement | DirectSumOfCrystals.Element[_CrystalElement]
    ]: ...
    def cardinality(self) -> int | Integer: ...
