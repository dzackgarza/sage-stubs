from collections.abc import Callable
from typing import Generic, TypeVar, overload

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import IdentityMorphism, Morphism, SetMorphism
from sage.categories.sets_cat import Sets
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.parent import Parent, Set_generic

_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)
_MorphismType = TypeVar(
    "_MorphismType",
    bound=Map,
    default=Map,
    covariant=True,
)

@overload
def Hom(
    X: Parent[_DomainElement],
    Y: Parent[_CodomainElement],
    category: Sets,
    check: bool = True,
) -> Homset[
    SetMorphism[_DomainElement, _CodomainElement],
    _DomainElement,
    _CodomainElement,
]: ...
@overload
def Hom(
    X: Parent[_DomainElement],
    Y: Parent[_CodomainElement],
    category: Category | None = None,
    check: bool = True,
) -> Homset[
    Map[_DomainElement, _CodomainElement],
    _DomainElement,
    _CodomainElement,
]: ...

def hom(
    X: Parent[_DomainElement],
    Y: Parent[_CodomainElement],
    f: Map[_DomainElement, _CodomainElement]
    | Callable[[_DomainElement], _CodomainElement],
) -> Morphism[_DomainElement, _CodomainElement]: ...

def End(
    X: Parent[_DomainElement],
    category: Category | None = None,
) -> Homset[Map[_DomainElement, _DomainElement], _DomainElement, _DomainElement]: ...

def end(
    X: Parent[_DomainElement],
    f: Map[_DomainElement, _DomainElement]
    | Callable[[_DomainElement], _DomainElement],
) -> Morphism[_DomainElement, _DomainElement]: ...

class Homset(
    Set_generic,
    Generic[_MorphismType, _DomainElement, _CodomainElement],
):
    element_class: type[_MorphismType]

    def __init__(
        self,
        X: Parent[_DomainElement],
        Y: Parent[_CodomainElement],
        category: Category | None = None,
        base: Ring | None = None,
        check: bool = True,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def homset_category(self) -> Category: ...
    def _abstract_element_class(self) -> type[_MorphismType]: ...
    def element_class_set_morphism(
        self,
    ) -> type[SetMorphism[_DomainElement, _CodomainElement]]: ...
    @overload
    def __call__(
        self,
        x: _MorphismType,
        check: bool | None = None,
        **options: bool | int | str | None,
    ) -> _MorphismType: ...
    @overload
    def __call__(
        self,
        x: Callable[[_DomainElement], _CodomainElement],
        check: bool | None = None,
        **options: bool | int | str | None,
    ) -> SetMorphism[_DomainElement, _CodomainElement]: ...
    def _element_constructor_(
        self,
        x: _MorphismType | Callable[[_DomainElement], _CodomainElement],
        check: bool | None = None,
        **options: bool | int | str | None,
    ) -> _MorphismType | SetMorphism[_DomainElement, _CodomainElement]: ...
    def an_element(self) -> _MorphismType: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __contains__(self, x: object) -> bool: ...
    def natural_map(self) -> Morphism[_DomainElement, _CodomainElement]: ...
    def identity(self) -> IdentityMorphism[_DomainElement]: ...
    def one(self) -> IdentityMorphism[_DomainElement]: ...
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...
    def reversed(
        self,
    ) -> Homset[
        Map[_CodomainElement, _DomainElement],
        _CodomainElement,
        _DomainElement,
    ]: ...

class HomsetWithBase(
    Homset[_MorphismType, _DomainElement, _CodomainElement],
    Generic[_MorphismType, _DomainElement, _CodomainElement],
):
    def __init__(
        self,
        X: Parent[_DomainElement],
        Y: Parent[_CodomainElement],
        category: Category | None = None,
        check: bool = True,
        base: Ring | None = None,
    ) -> None: ...
