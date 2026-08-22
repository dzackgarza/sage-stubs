from typing import overload

from sage.rings.function_field.drinfeld_modules.drinfeld_module import DrinfeldModule
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.lazy_series import LazyPowerSeries
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring_element import PowerSeries
from sage.structure.element import RingElement
from sage.structure.parent import Parent

type _CarlitzBase = Parent[RingElement] | RingElement | str | None

def CarlitzModule(A: PolynomialRing_generic, base: _CarlitzBase = ...) -> DrinfeldModule: ...

@overload
def carlitz_exponential(
    A: PolynomialRing_generic,
    prec: PlusInfinity = ...,
    name: str = ...,
) -> LazyPowerSeries: ...
@overload
def carlitz_exponential(
    A: PolynomialRing_generic,
    prec: int | Integer,
    name: str = ...,
) -> PowerSeries: ...

@overload
def carlitz_logarithm(
    A: PolynomialRing_generic,
    prec: PlusInfinity = ...,
    name: str = ...,
) -> LazyPowerSeries: ...
@overload
def carlitz_logarithm(
    A: PolynomialRing_generic,
    prec: int | Integer,
    name: str = ...,
) -> PowerSeries: ...

def carlitz_factorial(A: PolynomialRing_generic, n: Integer) -> Polynomial: ...

carlitz_series: dict[Integer, LazyPowerSeries]

def carlitz_bernoulli(A: PolynomialRing_generic, n: Integer) -> Polynomial: ...
