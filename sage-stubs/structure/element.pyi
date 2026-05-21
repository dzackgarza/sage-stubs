from typing import Protocol

from sage.structure.parent import Parent

class Element(Protocol):
    ...

def parent(x: object) -> Parent: ...
