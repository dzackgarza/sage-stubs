from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion
from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.sage_object import SageObject

class AsymptoticExpansionGenerators(SageObject):
    @staticmethod
    def Stirling(
        var: int | Integer,
        precision: int | Integer = ...,
        skip_constant_factor: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def log_Stirling(
        var: int | Integer,
        precision: int | Integer = ...,
        skip_constant_summand: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def HarmonicNumber(
        var: int | Integer,
        precision: int | Integer = ...,
        skip_constant_summand: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def Binomial_kn_over_n(
        var: int | Integer,
        k: int | Integer,
        precision: int | Integer = ...,
        skip_constant_factor: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def SingularityAnalysis(
        var: int | Integer,
        zeta: int | Integer = ...,
        alpha: RingElement | int | Integer | Rational = ...,
        beta: RingElement | int | Integer | Rational = ...,
        delta: int | Integer = ...,
        precision: int | Integer = ...,
        normalized: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def ImplicitExpansion(
        var: int | Integer,
        phi: Map | Morphism,
        tau: int | Integer = ...,
        precision: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def ImplicitExpansionPeriodicPart(
        var: int | Integer,
        phi: Map | Morphism,
        period: int | Integer,
        tau: int | Integer = ...,
        precision: int | Integer = ...,
    ) -> AsymptoticExpansion: ...
    @staticmethod
    def InverseFunctionAnalysis(
        var: int | Integer,
        phi: Map | Morphism,
        tau: int | Integer = ...,
        period: int | Integer = ...,
        precision: int | Integer = ...,
    ) -> AsymptoticExpansion: ...

asymptotic_expansions: AsymptoticExpansion
