from collections.abc import Iterable
from typing import Generic, Protocol, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.crystals.direct_sum import (
    CrystalElementProtocol,
    CrystalIndex,
)
from sage.combinat.crystals.subcrystal import (
    CartanTypeInput,
    ContainmentPredicate,
    ScalingFactorsInput,
    Subcrystal,
    VirtualizationInput,
)
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import Element
from sage.structure.parent import Parent

class VirtualizableCrystalElement(CrystalElementProtocol, Protocol):
    def e_string(
        self,
        indices: Iterable[CrystalIndex],
    ) -> Self | None: ...
    def f_string(
        self,
        indices: Iterable[CrystalIndex],
    ) -> Self | None: ...

_AmbientElement = TypeVar(
    "_AmbientElement",
    bound=VirtualizableCrystalElement,
)

class VirtualCrystal(
    Subcrystal[_AmbientElement],
    Generic[_AmbientElement],
):
    _virtualization: AbstractFamily
    _scaling_factors: AbstractFamily

    class Element(
        Subcrystal.Element[_AmbientElement],
        Generic[_AmbientElement],
    ):
        value: _AmbientElement
        def parent(self) -> VirtualCrystal[_AmbientElement]: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self | None: ...
        def epsilon(self, i: CrystalIndex) -> int | Integer: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def weight(self) -> Element: ...

    Element: type[Element[_AmbientElement]]
    element_class: type[Element[_AmbientElement]]

    @staticmethod
    def __classcall_private__(
        cls: type[VirtualCrystal[_AmbientElement]],
        ambient: Parent[_AmbientElement],
        virtualization: VirtualizationInput,
        scaling_factors: ScalingFactorsInput,
        contained: ContainmentPredicate[_AmbientElement] = ...,
        generators: Iterable[_AmbientElement] | None = ...,
        cartan_type: CartanTypeInput | None = ...,
        index_set: Iterable[CrystalIndex] | None = ...,
        category: Category | None = ...,
    ) -> VirtualCrystal[_AmbientElement]: ...
    def __init__(
        self,
        ambient: Parent[_AmbientElement],
        virtualization: AbstractFamily,
        scaling_factors: AbstractFamily,
        contained: ContainmentPredicate[_AmbientElement],
        generators: tuple[_AmbientElement, ...],
        cartan_type: CartanType_abstract,
        index_set: tuple[CrystalIndex, ...],
        category: Category,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: object) -> bool: ...
    def virtualization(self) -> AbstractFamily: ...
    def scaling_factors(self) -> AbstractFamily: ...
