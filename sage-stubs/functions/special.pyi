from sage.rings.complex_mpfr import ComplexNumber
from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionResult


class SphericalHarmonic(BuiltinFunction):
    def __init__(self) -> None: ...


spherical_harmonic: SphericalHarmonic

def elliptic_j(z: FunctionArgument, prec: int = 53) -> ComplexNumber: ...


class EllipticE(BuiltinFunction):
    def __init__(self) -> None: ...
class EllipticEC(BuiltinFunction):
    def __init__(self) -> None: ...
class EllipticEU(BuiltinFunction):
    def __init__(self) -> None: ...
class EllipticF(BuiltinFunction):
    def __init__(self) -> None: ...
class EllipticKC(BuiltinFunction):
    def __init__(self) -> None: ...
class EllipticPi(BuiltinFunction):
    def __init__(self) -> None: ...


elliptic_e: EllipticE
elliptic_ec: EllipticEC
elliptic_eu: EllipticEU
elliptic_f: EllipticF
elliptic_kc: EllipticKC
elliptic_pi: EllipticPi

def elliptic_eu_f(u: FunctionArgument, m: FunctionArgument) -> FunctionResult: ...
