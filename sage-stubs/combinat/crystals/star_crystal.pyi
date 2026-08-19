from typing import Generic, Self, TypeVar

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

_CrystalElement = TypeVar(
    "_CrystalElement",
    bound=CrystalElementProtocol,
)

class StarCrystal(
    UniqueRepresentation,
    Parent[StarCrystal.Element[_CrystalElement]],
    Generic[_CrystalElement],
):
    module_generators: tuple[StarCrystal.Element[_CrystalElement], ...]

    class Element(
        ElementWrapper,
        Generic[_CrystalElement],
    ):
        value: _CrystalElement
        def parent(self) -> StarCrystal[_CrystalElement]: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self: ...
        def weight(self) -> Element: ...
        def epsilon(self, i: CrystalIndex) -> int: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def jump(self, i: CrystalIndex) -> int | Integer: ...

    Element: type[Element[_CrystalElement]]
    element_class: type[Element[_CrystalElement]]

    def __init__(self, Binf: Parent[_CrystalElement]) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: _CrystalElement | Element[_CrystalElement],
    ) -> Element[_CrystalElement]: ...
    def highest_weight_vector(self) -> Element[_CrystalElement]: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def index_set(self) -> tuple[CrystalIndex, ...]: ...
    def weight_lattice_realization(self) -> Parent: ...
