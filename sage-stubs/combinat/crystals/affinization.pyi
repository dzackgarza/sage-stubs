from typing import Generic, Self, TypeVar

from sage.combinat.crystals.direct_sum import (
    CrystalElementProtocol,
    CrystalIndex,
)
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_CrystalElement = TypeVar(
    "_CrystalElement",
    bound=CrystalElementProtocol,
)

class AffinizationOfCrystal(
    UniqueRepresentation,
    Parent[AffinizationOfCrystal.Element[_CrystalElement]],
    Generic[_CrystalElement],
):
    module_generators: tuple[
        AffinizationOfCrystal.Element[_CrystalElement],
        ...,
    ]

    class Element(Element, Generic[_CrystalElement]):
        _b: _CrystalElement
        _m: int | Integer

        def __init__(
            self,
            parent: AffinizationOfCrystal[_CrystalElement],
            b: _CrystalElement,
            m: int | Integer,
        ) -> None: ...
        def parent(self) -> AffinizationOfCrystal[_CrystalElement]: ...
        def _repr_(self) -> str: ...
        def _latex_(self) -> str: ...
        def __hash__(self) -> int: ...
        def _richcmp_(
            self,
            other: AffinizationOfCrystal.Element[_CrystalElement],
            op: int,
        ) -> bool: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self | None: ...
        def epsilon(self, i: CrystalIndex) -> int | Integer: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def weight(self) -> Element: ...

    Element: type[Element[_CrystalElement]]
    element_class: type[Element[_CrystalElement]]

    def __init__(self, B: Parent[_CrystalElement]) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        b: _CrystalElement,
        m: int | Integer = ...,
    ) -> Element[_CrystalElement]: ...
    def __contains__(self, x: object) -> bool: ...
    def cardinality(self) -> PlusInfinity: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[CrystalIndex, ...]: ...
    def weight_lattice_realization(self) -> Parent: ...
