from collections.abc import Iterable, Protocol
from typing import Self, TypeVar

from sage.combinat.crystals.direct_sum import (
    CrystalElementProtocol,
    CrystalIndex,
)
from sage.combinat.crystals.tensor_product import TensorProductOfCrystals
from sage.combinat.crystals.tensor_product_element import (
    TensorProductOfCrystalsElement,
    TensorProductOfRegularCrystalsElement,
)
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

class PerfectCrystalElement(CrystalElementProtocol, Protocol):
    def Epsilon(self) -> Element: ...
    def Phi(self) -> Element: ...

_PerfectElement = TypeVar(
    "_PerfectElement",
    bound=PerfectCrystalElement,
)

type PerfectCrystal = Parent[_PerfectElement]
type PerfectCrystalInput = PerfectCrystal | Iterable[PerfectCrystal]

class KyotoPathModel(TensorProductOfCrystals):
    crystals: tuple[PerfectCrystal, ...]
    module_generators: tuple[KyotoPathModel.Element, ...]

    class Element(TensorProductOfRegularCrystalsElement):
        def parent(self) -> KyotoPathModel: ...
        def epsilon(self, i: CrystalIndex) -> int: ...
        def phi(self, i: CrystalIndex) -> int: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self: ...
        def weight(self) -> Element: ...
        def truncate(
            self,
            k: int | Integer | None = ...,
        ) -> TensorProductOfCrystalsElement: ...

    Element: type[Element]
    element_class: type[Element]

    @staticmethod
    def __classcall_private__(
        cls: type[KyotoPathModel],
        crystals: PerfectCrystalInput,
        weight: Element,
        P: Parent | None = ...,
    ) -> KyotoPathModel: ...
    def __init__(
        self,
        crystals: tuple[PerfectCrystal, ...],
        weight: Element,
        P: Parent,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def finite_tensor_product(
        self,
        k: int | Integer,
    ) -> TensorProductOfCrystals: ...
    def weight_lattice_realization(self) -> Parent: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[CrystalIndex, ...]: ...
    def highest_weight_vector(self) -> Element: ...
    def cardinality(self) -> PlusInfinity: ...
