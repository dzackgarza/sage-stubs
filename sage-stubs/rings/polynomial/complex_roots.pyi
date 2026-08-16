from sage.rings.real_mpfi import RealIntervalFieldElement
from sage.structure.element import Element

def interval_roots(
    self, rts: list[object], prec: int
) -> list[RealIntervalFieldElement]: ...
def intervals_disjoint(self) -> bool: ...
def complex_roots(
    self, skip_squarefree: bool = False, retval: str = "interval", min_prec: int = 0
) -> list[Element]: ...
