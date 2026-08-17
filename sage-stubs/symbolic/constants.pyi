from collections.abc import Callable, Mapping
from types import NotImplementedType
from typing import Literal

from sage.rings.infinity import MinusInfinity, PlusInfinity, UnsignedInfinity
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.symbolic.expression import Expression


type ConstantDomain = Literal["positive", "real", "complex"]
type ConstantConversions = Mapping[str, str]
type NamedConstant = Constant | PlusInfinity | MinusInfinity | UnsignedInfinity


constants_table: dict[int, Constant]
constants_name_table: dict[str, NamedConstant]


def unpickle_Constant(
    class_name: str,
    name: str,
    conversions: ConstantConversions | None,
    latex: str | None,
    mathml: str,
    domain: ConstantDomain,
) -> Constant: ...


class Constant:
    def __init__(
        self,
        name: str,
        conversions: ConstantConversions | None = None,
        latex: str | None = None,
        mathml: str = "",
        domain: ConstantDomain = "complex",
    ) -> None: ...
    def __richcmp__(self, other: object, op: int) -> bool | NotImplementedType: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[
            [
                str,
                str,
                ConstantConversions | None,
                str | None,
                str,
                ConstantDomain,
            ],
            Constant,
        ],
        tuple[
            str,
            str,
            ConstantConversions,
            str,
            str,
            ConstantDomain,
        ],
    ]: ...
    def domain(self) -> ConstantDomain: ...
    def expression(self) -> Expression: ...
    def name(self) -> str: ...
    def __repr__(self) -> str: ...


class Pi(Constant):
    def __init__(self, name: str = "pi") -> None: ...
    def __float__(self) -> float: ...


class NotANumber(Constant):
    def __init__(self, name: str = "NaN") -> None: ...
    def __float__(self) -> float: ...


class GoldenRatio(Constant):
    def __init__(self, name: str = "golden_ratio") -> None: ...
    def minpoly(
        self,
        bits: int | None = None,
        degree: int | None = None,
        epsilon: float = 0,
    ) -> Polynomial: ...
    def __float__(self) -> float: ...


class Log2(Constant):
    def __init__(self, name: str = "log2") -> None: ...
    def __float__(self) -> float: ...


class EulerGamma(Constant):
    def __init__(self, name: str = "euler_gamma") -> None: ...
    def __float__(self) -> float: ...


class Catalan(Constant):
    def __init__(self, name: str = "catalan") -> None: ...
    def __float__(self) -> float: ...


class Khinchin(Constant):
    def __init__(self, name: str = "khinchin") -> None: ...
    def __float__(self) -> float: ...


class TwinPrime(Constant):
    def __init__(self, name: str = "twinprime") -> None: ...
    def __float__(self) -> float: ...


class Mertens(Constant):
    def __init__(self, name: str = "mertens") -> None: ...
    def __float__(self) -> float: ...


class Glaisher(Constant):
    def __init__(self, name: str = "glaisher") -> None: ...
    def __float__(self) -> float: ...


pi: Pi
e: Expression
I: Expression
NaN: NotANumber
golden_ratio: GoldenRatio
log2: Log2
euler_gamma: EulerGamma
catalan: Catalan
khinchin: Khinchin
twinprime: TwinPrime
mertens: Mertens
glaisher: Glaisher
