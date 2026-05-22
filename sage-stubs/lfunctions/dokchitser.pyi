from typing import TYPE_CHECKING
from sage.structure.sage_object import SageObject
from sage.rings.complex_mpfr import ComplexField
from sage.rings.integer import Integer
from sage.rings.power_series_ring_element import PowerSeriesRingElement

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

class Dokchitser(SageObject):
    """Dokchitser's L-functions calculator."""

    conductor: int
    gammaV: list
    weight: int | float
    eps: int | float | complex
    poles: list
    residues: list | str
    prec: int

    def __new__(cls, *args, **kwargs) -> Dokchitser: ...
    def __init__(
        self,
        conductor: int,
        gammaV: Sequence,
        weight: int | float,
        eps: int | float | complex,
        poles: Sequence | None = None,
        residues: Sequence | str = ...,
        prec: int = ...,
        init: str | None = None,
    ) -> None: ...
    def __reduce__(self) -> tuple: ...
    def _repr_(self) -> str: ...
    def __del__(self) -> None: ...
    def gp(self): ...
    def cost(self, T: int | float = ...) -> Integer: ...
    def num_coeffs(self, T: int | float = ...) -> Integer: ...
    def init_coeffs(
        self,
        v: str | list | tuple,
        cutoff: int | float = ...,
        w: str | list | tuple | None = None,
        pari_precode: str = ...,
        max_imaginary_part: int | float = ...,
        max_asymp_coeffs: int = ...,
    ) -> None: ...
    def _clear_value_cache(self) -> None: ...
    def __call__(self, s: int | float | complex, c: int | float | None = None): ...
    def derivative(self, s: int | float | complex, k: int = ...) -> complex: ...
    def taylor_series(
        self, a: int | float | complex = ..., k: int = ..., var: str = ...
    ) -> PowerSeriesRingElement: ...
    def check_functional_equation(self, T: int | float = ...) -> complex: ...
    def set_coeff_growth(self, coefgrow: str) -> None: ...
