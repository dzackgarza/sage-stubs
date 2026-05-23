from collections.abc import Hashable
from typing import TypeAlias

from sage.structure.element import Element
from sage.structure.parent import Parent

_ImageElement: TypeAlias = Element | Hashable | list[Hashable]

class ImageSubobject(Parent):
    def _an_element_(self) -> _ImageElement: ...
