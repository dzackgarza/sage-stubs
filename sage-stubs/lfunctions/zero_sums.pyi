

from sage.rings.real_double import RealDoubleElement
from sage.rings.integer import Integer
from sage.schemes.elliptic_curves.ell_rational_field import EllipticCurve_rational_field
from sage.schemes.elliptic_curves.lseries_ell import Lseries_ell
class LFunctionZeroSum_abstract:
    def ncpus(self, n: int | None = ...) -> int: ...
    def level(self) -> Integer: ...
    def weight(self) -> Integer: ...
    def C0(self, include_euler_gamma: bool = ...) -> RealDoubleElement: ...
    def cnlist(
        self,
        n: int,
        python_floats: bool = ...,
    ) -> list[RealDoubleElement]: ...
    def digamma(
        self,
        s: complex,
        include_constant_term: bool = ...,
    ) -> RealDoubleElement | complex: ...
    def logarithmic_derivative(
        self,
        s: complex,
        num_terms: int = ...,
        as_interval: bool = ...,
    ) -> tuple[RealDoubleElement | complex, RealDoubleElement]: ...
    def completed_logarithmic_derivative(
        self,
        s: complex,
        num_terms: int = ...,
    ) -> tuple[RealDoubleElement | complex, RealDoubleElement]: ...
    def zerosum(
        self,
        Delta: float = ...,
        tau: float = ...,
        function: str = ...,
        ncpus: int | None = ...,
    ) -> RealDoubleElement: ...

class LFunctionZeroSum_EllipticCurve(LFunctionZeroSum_abstract):
    def __init__(
        self,
        E: EllipticCurve_rational_field,
        N: int | None = ...,
        ncpus: int = ...,
    ) -> None: ...
    def elliptic_curve(self) -> EllipticCurve_rational_field: ...
    def lseries(self) -> Lseries_ell: ...
    def cn(self, n: int) -> RealDoubleElement: ...
    def analytic_rank_upper_bound(
        self,
        max_Delta: float | None = ...,
        adaptive: bool = ...,
        root_number: str | int = ...,
        bad_primes: list[int] | None = ...,
        ncpus: int | None = ...,
    ) -> Integer: ...

def LFunctionZeroSum(
    X: EllipticCurve_rational_field,
    *args: object,
    **kwds: object,
) -> LFunctionZeroSum_EllipticCurve: ...
