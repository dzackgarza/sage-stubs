from typing import TYPE_CHECKING
from sage.structure.element import Element

if TYPE_CHECKING: # noqa: PYI002
    pass 

class LaurentSeries(Element):
    def degree(self) -> int: ...
    def valuation(self) -> int: ...
    def derivative(self, *args: object) -> LaurentSeries: ...
