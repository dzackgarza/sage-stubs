from typing import Generic, TypeVar

from sage.categories.homset import Homset
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.categories.category import Category
from sage.structure.sage_object import SageCoercionAtom

type MapCallInput = Element | SageCoercionAtom

_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)

class Map(Element, Generic[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        parent: Homset[
            Map[_DomainElement, _CodomainElement],
            _DomainElement,
            _CodomainElement,
        ],
        codomain: Parent[_CodomainElement] | None = ...,
    ) -> None: ...
    def domain(self) -> Parent[_DomainElement]: ...
    def codomain(self) -> Parent[_CodomainElement]: ...
    def category(self) -> Category: ...
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def __call__(self, x: _DomainElement) -> _CodomainElement: ...

class Section(Map[_CodomainElement, _DomainElement]):
    def __init__(self, map: Map[_DomainElement, _CodomainElement]) -> None: ...
    def codomain(self) -> Parent[_DomainElement]: ...
    def inverse(self) -> Map[_DomainElement, _CodomainElement]: ...
