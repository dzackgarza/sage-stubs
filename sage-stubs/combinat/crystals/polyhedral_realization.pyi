from collections.abc import Iterable, Sequence
from typing import Self

from sage.combinat.crystals.direct_sum import CrystalIndex
from sage.combinat.crystals.elementary_crystals import ElementaryCrystal
from sage.combinat.crystals.tensor_product import (
    TensorProductOfCrystals,
    TensorProductOfCrystalsElement,
)
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

type CartanTypeInput = CartanType_abstract | Sequence[object] | str

class InfinityCrystalAsPolyhedralRealization(TensorProductOfCrystals):
    crystals: tuple[ElementaryCrystal, ...]
    module_generators: tuple[InfinityCrystalAsPolyhedralRealization.Element, ...]

    class Element(TensorProductOfCrystalsElement):
        def parent(self) -> InfinityCrystalAsPolyhedralRealization: ...
        def epsilon(self, i: CrystalIndex) -> int: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self: ...
        def truncate(
            self,
            k: int | Integer | None = ...,
        ) -> TensorProductOfCrystalsElement: ...

    Element: type[Element]
    element_class: type[Element]

    @staticmethod
    def __classcall_private__(
        cls: type[InfinityCrystalAsPolyhedralRealization],
        cartan_type: CartanTypeInput,
        seq: Iterable[CrystalIndex] | None = ...,
    ) -> InfinityCrystalAsPolyhedralRealization: ...
    def __init__(
        self,
        cartan_type: CartanType_abstract,
        seq: tuple[CrystalIndex, ...],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def finite_tensor_product(
        self,
        k: int | Integer,
    ) -> TensorProductOfCrystals: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[CrystalIndex, ...]: ...
    def weight_lattice_realization(self) -> Parent: ...
    def highest_weight_vector(self) -> Element: ...
    def cardinality(self) -> PlusInfinity: ...
