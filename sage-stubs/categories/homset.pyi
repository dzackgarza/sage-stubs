from collections.abc import Callable
from typing import Generic, Literal, TypeVar, overload

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets
from sage.matrix.matrix2 import Matrix
from sage.structure.element import Element
from sage.structure.parent import ElementConstructorInput, Parent, ParentCallInput

_DomainElement = TypeVar("_DomainElement", default=Element, covariant=True)
_CodomainElement = TypeVar("_CodomainElement", default=Element, covariant=True)
_M = TypeVar("_M", bound=Element, default=Element, covariant=True)
_HomDomainElement = TypeVar("_HomDomainElement")
_HomCodomainElement = TypeVar("_HomCodomainElement")
type HomsetCallInput = Morphism | Callable[..., Element] | ParentCallInput

@overload
def Hom(
    self, Y: Parent[_HomCodomainElement], category: Sets, check: bool = ...
) -> Homset[
    SetMorphism[_HomDomainElement, _HomCodomainElement],
    _HomDomainElement,
    _HomCodomainElement,
]: ...
@overload
def Hom(
    self,
    Y: Parent[_HomCodomainElement],
    category: Category | None = ...,
    check: bool = ...,
) -> Homset[DomainElementT, CodomainElementT]: ...
def hom(self, Y: Parent, f: HomsetCallInput) -> Morphism: ...
def End(self, category: Category | None = None) -> Homset[Map[Hom, Hom], Hom, Hom]: ...
def end(self, f: HomsetCallInput) -> Morphism: ...

class Homset(Parent[_M], Generic[_M, _DomainElement, _CodomainElement]):
    def __init__(
        self,
        X: Parent[_DomainElement],
        Y: Parent[_CodomainElement],
        category: Category | None = None,
        base: Parent[ElementConstructorInput] | None = None,
        check: bool = True,
    ) -> None: ...
    def an_element(self) -> Element: ...
    @overload
    def __call__(
        self, x: HomsetCallInput = ..., check: bool | None = None
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        on_basis: Callable[..., Element],
        codomain: Parent | None = None,
        category: Category | None = None,
        zero: Element | None = None,
        position: int = 0,
        triangular: Literal["upper", "lower"] | None = None,
        unitriangular: bool = False,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        function: Callable[..., Element],
        codomain: Parent | None = None,
        category: Category | None = None,
        triangular: Literal["upper", "lower"] | None = None,
        unitriangular: bool = False,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        diagonal: Callable[..., Element],
        codomain: Parent | None = None,
        category: Category | None = None,
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    @overload
    def __call__(
        self,
        *,
        matrix: Matrix,
        codomain: Parent | None = None,
        category: Category | None = None,
        side: Literal["left", "right"] = "left",
        base_map: Morphism | None = None,
    ) -> Morphism: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def homset_category(self) -> Category: ...
    def domain(self) -> DomainElementT: ...
    def codomain(self) -> CodomainElementT: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __contains__(self, x: object) -> bool: ...
    def natural_map(self) -> Morphism: ...
    def identity(self) -> Morphism: ...
    def one(self) -> Morphism: ...

class HomsetWithBase(Homset[_M, _DomainElement, _CodomainElement]): ...
