import builtins

from sage.rings.integer import Integer
from sage.stats.distributions.discrete_gaussian_integer import (
    DiscreteGaussianDistributionIntegerSampler,
)

class _SageObject: ...

class DiscreteGaussianDistributionPolynomialSampler:
    D: DiscreteGaussianDistributionIntegerSampler
    P: builtins.int
    n: Integer

    def __init__(
        self, P: builtins.int, n: builtins.int, sigma: builtins.object
    ) -> None: ...
    def __call__(self) -> _SageObject: ...
