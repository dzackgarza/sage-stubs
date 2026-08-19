from collections.abc import Iterable
from typing import Self

from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

type SegmentInput = tuple[int | Integer, int | Integer | IntegerMod_abstract]
type Segment = tuple[int | Integer, IntegerMod_abstract]
type MultisegmentInput = Iterable[SegmentInput]
type SignatureData = tuple[int | Integer | None, int | Integer | None, int]

class InfinityCrystalOfMultisegments(
    Parent[InfinityCrystalOfMultisegments.Element],
    UniqueRepresentation,
):
    _cartan_type: CartanType_abstract
    _Zn: IntegerModRing_generic
    module_generators: tuple[InfinityCrystalOfMultisegments.Element, ...]

    class Element(ElementWrapper):
        value: tuple[Segment, ...]

        def __init__(
            self,
            parent: InfinityCrystalOfMultisegments,
            value: MultisegmentInput,
        ) -> None: ...
        def parent(self) -> InfinityCrystalOfMultisegments: ...
        def _repr_(self) -> str: ...
        def _latex_(self) -> str: ...
        def _sig(
            self,
            i: int | Integer | IntegerMod_abstract,
        ) -> SignatureData: ...
        def e(
            self,
            i: int | Integer | IntegerMod_abstract,
        ) -> Self | None: ...
        def f(
            self,
            i: int | Integer | IntegerMod_abstract,
        ) -> Self: ...
        def epsilon(
            self,
            i: int | Integer | IntegerMod_abstract,
        ) -> int: ...
        def phi(
            self,
            i: int | Integer | IntegerMod_abstract,
        ) -> int | Integer: ...
        def weight(self) -> Element: ...

    Element: type[Element]
    element_class: type[Element]

    def __init__(self, n: int | Integer) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        value: MultisegmentInput | Element = ...,
    ) -> Element: ...
    def highest_weight_vector(self) -> Element: ...
    def weight_lattice_realization(self) -> Parent: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[int, ...]: ...
    def cardinality(self) -> PlusInfinity: ...
