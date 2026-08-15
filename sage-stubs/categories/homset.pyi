from collections.abc import Callable
from typing import Generic, Literal, TypeVar, overload

from sage.matrix.matrix2 import Matrix
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.category import Category
from sage.categories.sets_cat import Sets
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
    X: Parent[_HomDomainElement],
    Y: Parent[_HomCodomainElement],
    category: Sets,
    check: bool = ...,
) -> Homset[
    SetMorphism[_HomDomainElement, _HomCodomainElement],
    _HomDomainElement,
    _HomCodomainElement,
]: ...
@overload
def Hom(
    X: Parent[_HomDomainElement],
    Y: Parent[_HomCodomainElement],
    category: Category | None = ...,
    check: bool = ...,
) -> Homset[
    Map[_HomDomainElement, _HomCodomainElement],
    _HomDomainElement,
    _HomCodomainElement,
]: ...

def hom(X: Parent, Y: Parent, f: HomsetCallInput) -> Morphism: ...

def End(X: Parent[_HomDomainElement], category: Category | None = None) -> Homset[Map[_HomDomainElement, _HomDomainElement], _HomDomainElement, _HomDomainElement]: ...

def end(X: Parent, f: HomsetCallInput) -> Morphism: ...

class Homset(Parent[_M], Generic[_M, _DomainElement, _CodomainElement]):
    def __init__(
        self,
        X: Parent[_DomainElement],
        Y: Parent[_CodomainElement],
        category: Category | None = None,
        base: Parent[ElementConstructorInput] | None = None,
        check: bool = True,
    ) -> None: ...
    def an_element(self) -> _M: ...
    @overload
    def __call__(self, x: HomsetCallInput = ..., check: bool | None = None) -> Morphism: ...
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
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __contains__(self, x: object) -> bool: ...
    def natural_map(self) -> Morphism: ...
    def identity(self) -> Morphism: ...
    def one(self) -> Morphism: ...

class HomsetWithBase(Homset[_M, _DomainElement, _CodomainElement]):
    ...
