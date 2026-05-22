from typing import Protocol

from sage.structure.parent import Parent

class Element(Protocol):
    ...

class RingElement(Element, Protocol):
    ...

class InfinityElement(RingElement, Protocol):
    ...

def parent(x: object) -> Parent: ...
