from collections.abc import Iterator

from sage.rings.finite_rings.element_givaro import FiniteField_givaroElement
from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.finite_rings.hom_finite_field_givaro import FrobeniusEndomorphism_givaro
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial


class FiniteField_givaro(FiniteField):
    _cache: object
    _modulus: object

    def __init__(
        self,
        q: int | Integer,
        name: str = "a",
        modulus: Polynomial | None = None,
        repr: str = "poly",
        cache: bool = False,
    ) -> None: ...

    def characteristic(self) -> int:
        ...

    def order(self) -> Integer:
        ...

    def degree(self) -> int:
        ...

    def _repr_option(self, key: str) -> bool:
        ...

    def random_element(self, *args: object, **kwds: object) -> FiniteField_givaroElement:
        ...

    def _element_constructor_(self, e: FiniteField_givaroElement | int | Integer | str | Polynomial | None) -> FiniteField_givaroElement:
        ...

    def gen(self, n: int = 0) -> FiniteField_givaroElement:
        ...

    def prime_subfield(self) -> FiniteField:
        ...

    def log_to_int(self, n: int) -> int:
        ...

    def int_to_log(self, n: int) -> int:
        ...

    def from_integer(self, n: int, reverse: bool = False) -> FiniteField_givaroElement:
        ...

    def _pari_modulus(self) -> Polynomial:
        ...

    def __iter__(self) -> Iterator[FiniteField_givaroElement]:
        ...

    def a_times_b_plus_c(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        ...

    def a_times_b_minus_c(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        ...

    def c_minus_a_times_b(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        ...

    def frobenius_endomorphism(self, n: int = 1) -> FrobeniusEndomorphism_givaro:
        ...
