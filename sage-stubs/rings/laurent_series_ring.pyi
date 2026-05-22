from typing import TYPE_CHECKING

if TYPE_CHECKING: # noqa: PYI002
    from sage.rings.ring import Ring
    from sage.rings.laurent_series_ring_element import LaurentSeries

class LaurentSeriesRing_generic:
    def gen(self, n: int = ...) -> LaurentSeries: ...
    def default_prec(self) -> int: ...
    def base_ring(self) -> Ring: ...
