from typing import Literal

from sage.rings.rational import Rational
from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionKeyword, FunctionResult


type JacobiKind = Literal["nd", "ns", "nc", "dn", "ds", "dc", "sn", "sd", "sc", "cn", "cd", "cs"]

HALF: Rational


class Jacobi(BuiltinFunction):
    def __init__(self, kind: JacobiKind) -> None: ...


jacobi_nd: Jacobi
jacobi_ns: Jacobi
jacobi_nc: Jacobi
jacobi_dn: Jacobi
jacobi_ds: Jacobi
jacobi_dc: Jacobi
jacobi_sn: Jacobi
jacobi_sd: Jacobi
jacobi_sc: Jacobi
jacobi_cn: Jacobi
jacobi_cd: Jacobi
jacobi_cs: Jacobi


class InverseJacobi(BuiltinFunction):
    def __init__(self, kind: JacobiKind) -> None: ...


inverse_jacobi_nd: InverseJacobi
inverse_jacobi_ns: InverseJacobi
inverse_jacobi_nc: InverseJacobi
inverse_jacobi_dn: InverseJacobi
inverse_jacobi_ds: InverseJacobi
inverse_jacobi_dc: InverseJacobi
inverse_jacobi_sn: InverseJacobi
inverse_jacobi_sd: InverseJacobi
inverse_jacobi_sc: InverseJacobi
inverse_jacobi_cn: InverseJacobi
inverse_jacobi_cd: InverseJacobi
inverse_jacobi_cs: InverseJacobi


def jacobi(
    kind: JacobiKind,
    z: FunctionArgument,
    m: FunctionArgument,
    **kwargs: FunctionKeyword,
) -> FunctionResult: ...
def inverse_jacobi(
    kind: JacobiKind,
    x: FunctionArgument,
    m: FunctionArgument,
    **kwargs: FunctionKeyword,
) -> FunctionResult: ...


class JacobiAmplitude(BuiltinFunction):
    def __init__(self) -> None: ...


jacobi_am: JacobiAmplitude

def inverse_jacobi_f(kind: JacobiKind, x: float, m: float) -> float | complex: ...
def jacobi_am_f(x: float, m: float) -> float | complex: ...
