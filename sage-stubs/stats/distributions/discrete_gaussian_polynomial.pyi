from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.stats.distributions.discrete_gaussian_integer import (
    DiscreteGaussianDistributionIntegerSampler,
    RealInput,
)
from sage.structure.sage_object import SageObject


class DiscreteGaussianDistributionPolynomialSampler(SageObject):
    D: DiscreteGaussianDistributionIntegerSampler
    n: Integer
    P: PolynomialRing_generic

    def __init__(
        self,
        P: PolynomialRing_generic,
        n: int | Integer,
        sigma: RealInput | DiscreteGaussianDistributionIntegerSampler,
    ) -> None: ...
    def __call__(self) -> Polynomial: ...
    def _repr_(self) -> str: ...
