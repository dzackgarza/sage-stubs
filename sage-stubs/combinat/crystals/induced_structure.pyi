from collections.abc import Callable, Iterator
from typing import Generic, Literal, Protocol, Self, TypeVar, overload

from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.element_wrapper import ElementWrapper
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_SetElement = TypeVar("_SetElement")
_CrystalElement = TypeVar("_CrystalElement", bound="CrystalElementProtocol")
type CrystalIndex = int | Integer | str
type Cardinality = int | Integer | PlusInfinity

class CrystalElementProtocol(Protocol):
    def parent(self) -> Parent: ...
    def e(self, i: CrystalIndex) -> Self | None: ...
    def f(self, i: CrystalIndex) -> Self | None: ...
    def epsilon(self, i: CrystalIndex) -> int | Integer: ...
    def phi(self, i: CrystalIndex) -> int | Integer: ...
    def weight(self) -> Element: ...

class InducedCrystal(
    UniqueRepresentation,
    Parent[InducedCrystal.Element[_SetElement, _CrystalElement]],
    Generic[_SetElement, _CrystalElement],
):
    module_generators: InducedCrystal[_SetElement, _CrystalElement]

    class Element(
        ElementWrapper,
        Generic[_SetElement, _CrystalElement],
    ):
        value: _SetElement
        def parent(
            self,
        ) -> InducedCrystal[_SetElement, _CrystalElement]: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self | None: ...
        def epsilon(self, i: CrystalIndex) -> int | Integer: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def weight(self) -> Element: ...

    @overload
    @staticmethod
    def __classcall_private__(
        cls: type[InducedCrystal[_SetElement, _CrystalElement]],
        X: Parent[_SetElement],
        phi: Callable[[_SetElement], _CrystalElement],
        inverse: Callable[[_CrystalElement], _SetElement] | None = ...,
        from_crystal: Literal[False] = ...,
    ) -> InducedCrystal[_SetElement, _CrystalElement]: ...
    @overload
    @staticmethod
    def __classcall_private__(
        cls: type[InducedCrystal[_SetElement, _CrystalElement]],
        X: Parent[_CrystalElement],
        phi: Callable[[_CrystalElement], _SetElement],
        inverse: Callable[[_SetElement], _CrystalElement] | None = ...,
        from_crystal: Literal[True] = ...,
    ) -> InducedFromCrystal[_SetElement, _CrystalElement]: ...
    def __init__(
        self,
        X: Parent[_SetElement],
        phi: Callable[[_SetElement], _CrystalElement],
        inverse: Callable[[_CrystalElement], _SetElement] | None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: _SetElement | _CrystalElement,
    ) -> InducedCrystal.Element[_SetElement, _CrystalElement]: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(
        self,
    ) -> Iterator[InducedCrystal.Element[_SetElement, _CrystalElement]]: ...
    def cardinality(self) -> Cardinality: ...
    def cartan_type(self) -> CartanType_abstract: ...

class InducedFromCrystal(
    UniqueRepresentation,
    Parent[InducedFromCrystal.Element[_SetElement, _CrystalElement]],
    Generic[_SetElement, _CrystalElement],
):
    module_generators: tuple[
        InducedFromCrystal.Element[_SetElement, _CrystalElement],
        ...,
    ]

    class Element(
        ElementWrapper,
        Generic[_SetElement, _CrystalElement],
    ):
        value: _SetElement
        def parent(
            self,
        ) -> InducedFromCrystal[_SetElement, _CrystalElement]: ...
        def e(self, i: CrystalIndex) -> Self | None: ...
        def f(self, i: CrystalIndex) -> Self | None: ...
        def epsilon(self, i: CrystalIndex) -> int | Integer: ...
        def phi(self, i: CrystalIndex) -> int | Integer: ...
        def weight(self) -> Element: ...

    def __init__(
        self,
        X: Parent[_CrystalElement],
        phi: Callable[[_CrystalElement], _SetElement],
        inverse: Callable[[_SetElement], _CrystalElement] | None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: _SetElement | _CrystalElement,
    ) -> InducedFromCrystal.Element[_SetElement, _CrystalElement]: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(
        self,
    ) -> Iterator[InducedFromCrystal.Element[_SetElement, _CrystalElement]]: ...
    def cardinality(self) -> Cardinality: ...
    def cartan_type(self) -> CartanType_abstract: ...
