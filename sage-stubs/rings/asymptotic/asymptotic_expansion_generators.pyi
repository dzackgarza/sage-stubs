from collections.abc import Callable

from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

type AsymptoticScalar = RingElement | int | Integer | Rational
type ImplicitFunction = Callable[[Expression], Expression]

class AsymptoticExpansionGenerators(SageObject):
    @staticmethod
    def Stirling(
        var: str,
        precision: int | Integer | None = ...,
        skip_constant_factor: bool = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def log_Stirling(
        var: str,
        precision: int | Integer | None = ...,
        skip_constant_summand: bool = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def HarmonicNumber(
        var: str,
        precision: int | Integer | None = ...,
        skip_constant_summand: bool = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def Binomial_kn_over_n(
        var: str,
        k: AsymptoticScalar,
        precision: int | Integer | None = ...,
        skip_constant_factor: bool = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def SingularityAnalysis(
        var: str,
        zeta: AsymptoticScalar = ...,
        alpha: AsymptoticScalar = ...,
        beta: AsymptoticScalar = ...,
        delta: int | Integer = ...,
        precision: int | Integer | None = ...,
        normalized: bool = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def ImplicitExpansion(
        var: str,
        phi: ImplicitFunction,
        tau: AsymptoticScalar | None = ...,
        precision: int | Integer | None = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def ImplicitExpansionPeriodicPart(
        var: str,
        phi: ImplicitFunction,
        period: int | Integer,
        tau: AsymptoticScalar | None = ...,
        precision: int | Integer | None = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def InverseFunctionAnalysis(
        var: str,
        phi: ImplicitFunction,
        tau: AsymptoticScalar | None = ...,
        period: int | Integer = ...,
        precision: int | Integer | None = ...,
    ) -> AsymptoticExpansion: ...

asymptotic_expansions: AsymptoticExpansionGenerators
