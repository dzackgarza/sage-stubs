from sage.structure.element import Element
from sage.structure.parent import Parent

class RealSet(Parent):
    def _an_element_(self) -> Element: ...
