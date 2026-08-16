from typing import Generic, Self, TypeVar

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageCoercionAtom

type MapCallInput = Element | SageCoercionAtom
_DomainElement = TypeVar("_DomainElement", default=Element)
_CodomainElement = TypeVar("_CodomainElement", default=Element)

class Map(Element, Generic[_DomainElement, _CodomainElement]):
    def __init__(
        self,
        parent: Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ]
        | Parent[Self],
        codomain: Parent[_CodomainElement] | None = ...,
    ) -> None: ...
    def domain(self) -> Parent[Map]: ...
    def codomain(self) -> Parent[Map]: ...
    def category(self) -> Category: ...
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def __call__(self, x: _DomainElement) -> Map: ...

class Section(Map[_CodomainElement, _DomainElement]):
    def __init__(
        self,
        map: Map[_DomainElement, _CodomainElement]
        | Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ],
    ) -> None: ...
    def codomain(self) -> Parent[Section]: ...
    def inverse(self) -> Map[Section, Section]: ...
