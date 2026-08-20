from typing import Literal

from sage.rings.integer import Integer
from sage.rings.rational import Rational
from sage.rings.real_mpfr import RealNumber
from sage.structure.sage_object import SageObject


type DiscreteGaussianAlgorithm = Literal[
    "uniform+table",
    "uniform+online",
    "uniform+logtable",
    "sigma2+logtable",
]
type DiscreteGaussianPrecision = Literal["mp", "dp"]
type RealInput = int | Integer | Rational | float | RealNumber


class DiscreteGaussianDistributionIntegerSampler(SageObject):
    table_cutoff: int
    sigma: RealNumber
    c: RealNumber
    tau: Integer
    algorithm: DiscreteGaussianAlgorithm

    def __init__(
        self,
        sigma: RealInput,
        c: RealInput = ...,
        tau: int | Integer = ...,
        algorithm: DiscreteGaussianAlgorithm | None = ...,
        precision: DiscreteGaussianPrecision = ...,
    ) -> None: ...
    def _flush_cache(self) -> None: ...
    def __call__(self) -> Integer: ...
    def _repr_(self) -> str: ...
