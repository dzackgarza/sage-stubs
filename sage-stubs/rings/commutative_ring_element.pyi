from typing import Protocol

from sage.structure.element import RingElement

class CommutativeRingElement(RingElement, Protocol):
    ...


__all__ = ("CommutativeRingElement",)
