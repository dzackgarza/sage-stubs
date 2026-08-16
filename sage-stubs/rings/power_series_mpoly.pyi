from sage.rings.infinity import PlusInfinity
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.power_series_ring import PowerSeriesRing_generic
from sage.rings.power_series_ring_element import PowerSeries
from sage.structure.element import Element

type ElementList[E] = list[E]

class PowerSeries_mpoly(PowerSeries):
    def __init__(
        self,
        parent: PowerSeriesRing_generic | PowerSeriesRing,
        f: MPolynomial | Element | int = 0,
        prec: int | PlusInfinity | bool = ...,
        check: bool = True,
        is_gen: bool = False,
    ) -> None: ...
    def __call__(self, *args: object, **kwds: object) -> Element: ...
    def do_truncation(self) -> None: ...
    def list(self) -> ElementList[Element]: ...
    def polynomial(self) -> MPolynomial: ...
