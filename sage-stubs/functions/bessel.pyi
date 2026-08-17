from collections.abc import Callable
from typing import Literal

from sage.symbolic.function import BuiltinFunction, FunctionArgument, FunctionResult


type BesselType = Literal["I", "J", "K", "Y"]
type BesselFunction = Function_Bessel_I | Function_Bessel_J | Function_Bessel_K | Function_Bessel_Y


class Function_Bessel_J(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_Bessel_Y(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_Bessel_I(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_Bessel_K(BuiltinFunction):
    def __init__(self) -> None: ...


bessel_J: Function_Bessel_J
bessel_Y: Function_Bessel_Y
bessel_I: Function_Bessel_I
bessel_K: Function_Bessel_K
bessel_type_dict: dict[BesselType, BesselFunction]


def Bessel(
    order: FunctionArgument | None = None,
    typ: BesselType = "J",
) -> BesselFunction | Callable[[FunctionArgument], FunctionResult]: ...


class Function_Struve_H(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_Struve_L(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_Hankel1(BuiltinFunction):
    def __init__(self) -> None: ...
class Function_Hankel2(BuiltinFunction):
    def __init__(self) -> None: ...
class SphericalBesselJ(BuiltinFunction):
    def __init__(self) -> None: ...
class SphericalBesselY(BuiltinFunction):
    def __init__(self) -> None: ...
class SphericalHankel1(BuiltinFunction):
    def __init__(self) -> None: ...
class SphericalHankel2(BuiltinFunction):
    def __init__(self) -> None: ...


struve_H: Function_Struve_H
struve_L: Function_Struve_L
hankel1: Function_Hankel1
hankel2: Function_Hankel2
spherical_bessel_J: SphericalBesselJ
spherical_bessel_Y: SphericalBesselY
spherical_hankel1: SphericalHankel1
spherical_hankel2: SphericalHankel2


def spherical_bessel_f(
    F: BuiltinFunction,
    n: int,
    z: FunctionArgument,
) -> FunctionResult: ...
