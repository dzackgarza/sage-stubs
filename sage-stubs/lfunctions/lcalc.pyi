from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.rings.integer import Integer
    from sage.rings.real_mpfr import RealNumber
    from sage.rings.complex_mpfr import ComplexNumber

class LCalc:
    def __call__(self, args: str) -> str: ...
    def help(self) -> None: ...
    def zeros(
        self,
        n: int,
        L: str = ...,
    ) -> list[RealNumber]: ...
    def zeros_in_interval(
        self,
        x: float,
        y: float,
        stepsize: float,
        L: str = ...,
    ) -> list[tuple[RealNumber, RealNumber]]: ...
    def value(
        self,
        s: complex,
        L: str = ...,
    ) -> ComplexNumber: ...
    def values_along_line(
        self,
        s0: complex,
        s1: complex,
        number_samples: int,
        L: str = ...,
    ) -> list[tuple[ComplexNumber, ComplexNumber]]: ...
    def twist_values(
        self,
        s: complex,
        dmin: int,
        dmax: int,
        L: str = ...,
    ) -> list[tuple[Integer, ComplexNumber]]: ...
    def twist_zeros(
        self,
        n: int,
        dmin: int,
        dmax: int,
        L: str = ...,
    ) -> dict[Integer, list[RealNumber]]: ...
    def analytic_rank(self, L: str = ...) -> Integer: ...

lcalc: LCalc
