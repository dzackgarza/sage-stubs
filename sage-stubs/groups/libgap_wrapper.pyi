from sage.libs.gap.element import GapElement
from sage.structure.element import MultiplicativeGroupElement
from sage.structure.sage_object import SageObject

class ParentLibGAP(SageObject):
    def gap(self) -> GapElement: ...

class ElementLibGAP(MultiplicativeGroupElement):
    def gap(self) -> GapElement: ...
