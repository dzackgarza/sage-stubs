from typing import TypeAlias

from sage.structure.parent import Parent
from sage.rings.polynomial.polynomial_element import Polynomial

_ExtensionKwarg: TypeAlias = str | bool | int | Parent | None

class CommutativeRings:
    class ElementMethods:
        ...
    class ParentMethods:
        def extension(
            self,
            poly: Polynomial,
            name: str | tuple[str, ...] | None = None,
            names: str | tuple[str, ...] | None = None,
            **kwds: _ExtensionKwarg,
        ) -> Parent: ...
    class Finite:
        class ParentMethods:
            ...
