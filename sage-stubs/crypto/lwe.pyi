from collections.abc import Callable
from typing import Literal, Protocol, overload

from sage.modules.free_module import FreeModule_ambient
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_quotient_ring import (
    PolynomialQuotientRing_generic,
)
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.stats.distributions.discrete_gaussian_integer import (
    DiscreteGaussianDistributionIntegerSampler,
)
from sage.stats.distributions.discrete_gaussian_polynomial import (
    DiscreteGaussianDistributionPolynomialSampler,
)
from sage.structure.sage_object import SageObject


type SecretDistribution = (
    Literal["uniform", "noise"]
    | tuple[int | Integer, int | Integer]
)
type LWESample = tuple[
    FreeModuleElement[IntegerMod_abstract],
    IntegerMod_abstract,
]
type RingLWESample = tuple[
    FreeModuleElement[IntegerMod_abstract],
    FreeModuleElement[IntegerMod_abstract],
]
type ModularLWESample = LWESample | RingLWESample
type BalancedLWESample = tuple[
    FreeModuleElement[Integer],
    Integer,
]
type BalancedRingLWESample = tuple[
    FreeModuleElement[Integer],
    FreeModuleElement[Integer],
]
type BalancedSample = BalancedLWESample | BalancedRingLWESample


class IntegerNoiseSampler(Protocol):
    def __call__(self) -> int | Integer: ...


class PolynomialNoiseSampler(Protocol):
    n: Integer
    def __call__(self) -> Polynomial: ...


class UniformSampler(SageObject):
    lower_bound: Integer
    upper_bound: Integer

    def __init__(
        self,
        lower_bound: int | Integer,
        upper_bound: int | Integer,
    ) -> None: ...
    def __call__(self) -> int: ...
    def _repr_(self) -> str: ...


class UniformPolynomialSampler(SageObject):
    n: Integer
    P: PolynomialRing_generic
    lower_bound: Integer
    upper_bound: Integer
    D: UniformSampler

    def __init__(
        self,
        P: PolynomialRing_generic,
        n: int | Integer,
        lower_bound: int | Integer,
        upper_bound: int | Integer,
    ) -> None: ...
    def __call__(self) -> Polynomial: ...
    def _repr_(self) -> str: ...


class LWE(SageObject):
    n: Integer
    m: int | Integer | None
    K: IntegerModRing_generic
    FM: FreeModule_ambient[IntegerMod_abstract]
    D: IntegerNoiseSampler
    secret_dist: SecretDistribution

    def __init__(
        self,
        n: int | Integer,
        q: int | Integer,
        D: IntegerNoiseSampler,
        secret_dist: SecretDistribution = ...,
        m: int | Integer | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __call__(self) -> LWESample: ...


class Regev(LWE):
    def __init__(
        self,
        n: int | Integer,
        secret_dist: SecretDistribution = ...,
        m: int | Integer | None = ...,
    ) -> None: ...


class LindnerPeikert(LWE):
    def __init__(
        self,
        n: int | Integer,
        delta: float = ...,
        m: int | Integer | None = ...,
    ) -> None: ...


class UniformNoiseLWE(LWE):
    def __init__(
        self,
        n: int | Integer,
        instance: Literal["key", "encrypt"] = ...,
        m: int | Integer | None = ...,
    ) -> None: ...


class RingLWE(SageObject):
    N: Integer
    n: Integer
    m: int | Integer | None
    K: IntegerModRing_generic
    D: PolynomialNoiseSampler
    q: int | Integer
    poly: Polynomial
    R_q: PolynomialQuotientRing_generic
    secret_dist: Literal["uniform", "noise"]

    def __init__(
        self,
        N: int | Integer,
        q: int | Integer,
        D: PolynomialNoiseSampler,
        poly: Polynomial | None = ...,
        secret_dist: Literal["uniform", "noise"] = ...,
        m: int | Integer | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __call__(self) -> RingLWESample: ...


class RingLindnerPeikert(RingLWE):
    def __init__(
        self,
        N: int | Integer,
        delta: float = ...,
        m: int | Integer | None = ...,
    ) -> None: ...


class RingLWEConverter(SageObject):
    ringlwe: RingLWE
    n: Integer

    def __init__(self, ringlwe: RingLWE) -> None: ...
    def __call__(self) -> LWESample: ...
    def _repr_(self) -> str: ...


type LWEOracle = LWE | RingLWE | RingLWEConverter
type LWEOracleClass = type[LWE] | type[RingLWE]
type LWEOracleInput = str | LWEOracleClass | LWEOracle


@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: LWE | type[LWE],
    seed: int | Integer | None = ...,
    balanced: Literal[False] = ...,
    **kwds: object,
) -> list[LWESample]: ...
@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: RingLWE | type[RingLWE],
    seed: int | Integer | None = ...,
    balanced: Literal[False] = ...,
    **kwds: object,
) -> list[RingLWESample]: ...
@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: RingLWEConverter,
    seed: int | Integer | None = ...,
    balanced: Literal[False] = ...,
    **kwds: object,
) -> list[LWESample]: ...
@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: LWE | type[LWE],
    seed: int | Integer | None,
    balanced: Literal[True],
    **kwds: object,
) -> list[BalancedLWESample]: ...
@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: RingLWE | type[RingLWE],
    seed: int | Integer | None,
    balanced: Literal[True],
    **kwds: object,
) -> list[BalancedRingLWESample]: ...
@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: RingLWEConverter,
    seed: int | Integer | None,
    balanced: Literal[True],
    **kwds: object,
) -> list[BalancedLWESample]: ...
@overload
def samples(
    m: int | Integer,
    n: int | Integer,
    lwe: LWEOracleInput,
    seed: int | Integer | None = ...,
    balanced: bool = ...,
    **kwds: object,
) -> list[ModularLWESample | BalancedSample]: ...


@overload
def balance_sample(
    s: LWESample,
    q: int | Integer | None = ...,
) -> BalancedLWESample: ...
@overload
def balance_sample(
    s: RingLWESample,
    q: int | Integer | None = ...,
) -> BalancedRingLWESample: ...
