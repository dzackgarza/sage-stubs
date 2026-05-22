from typing import TypeAlias

from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.combinat.root_system.cartan_type import CartanType_abstract

_ElementList: TypeAlias = list[Element]

class ClassicalCrystalOfLetters(UniqueRepresentation, Parent):
    def cartan_type(self) -> CartanType_abstract: ...
    def module_generators(self) -> tuple[Element, ...]: ...
    def list(self) -> _ElementList: ...
    def lt_elements(self, x: Element, y: Element) -> bool: ...
