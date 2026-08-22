from typing import overload

from sage.rings.function_field.drinfeld_modules.drinfeld_module import DrinfeldModule
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.lazy_series import LazyPowerSeries
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring_element import PowerSeries
from sage.structure.element import RingElement

class DrinfeldModule_charzero(DrinfeldModule):
    def _compute_coefficient_exp(self, k: int | Integer) -> RingElement: ...
    @overload
    def exponential(
        self,
        prec: PlusInfinity = ...,
        name: str = ...,
    ) -> LazyPowerSeries: ...
    @overload
    def exponential(
        self,
        prec: int | Integer,
        name: str = ...,
    ) -> PowerSeries: ...
    def _compute_coefficient_log(self, k: int | Integer) -> RingElement: ...
    @overload
    def logarithm(
        self,
        prec: PlusInfinity = ...,
        name: str = ...,
    ) -> LazyPowerSeries: ...
    @overload
    def logarithm(
        self,
        prec: int | Integer,
        name: str = ...,
    ) -> PowerSeries: ...
    def _compute_goss_polynomial(
        self,
        n: int | Integer,
        q: int | Integer,
        poly_ring: PolynomialRing_generic,
        X: Polynomial,
    ) -> Polynomial: ...
    def goss_polynomial(self, n: int | Integer, var: str = ...) -> Polynomial: ...

class DrinfeldModule_rational(DrinfeldModule_charzero):
    def coefficient_in_function_ring(self, n: int | Integer) -> Polynomial: ...
    def coefficients_in_function_ring(self, sparse: bool = ...) -> list[Polynomial]: ...
    def class_polynomial(self) -> Polynomial: ...
