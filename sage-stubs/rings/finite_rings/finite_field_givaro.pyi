from typing import TYPE_CHECKING
from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.integer import Integer

if TYPE_CHECKING:
    from sage.rings.finite_rings.element_givaro import FiniteField_givaroElement

class FiniteField_givaro(FiniteField):
    """Finite field implemented using Zech logs (cardinality < 2^16)."""

    _cache: object
    _modulus: object

    def __init__(
        self,
        q,
        name: str = "a",
        modulus=None,
        repr: str = "poly",
        cache: bool = False,
    ) -> None: ...

    def characteristic(self) -> Integer:
        """Return the characteristic of this field."""
        ...

    def order(self) -> Integer:
        """Return the cardinality of this field."""
        ...

    def degree(self) -> Integer:
        """Return n if the cardinality of self is p^n."""
        ...

    def _repr_option(self, key: str) -> bool:
        """Metadata about the _repr_ output."""
        ...

    def random_element(self, *args, **kwds) -> FiniteField_givaroElement:
        """Return a random element of self."""
        ...

    def _element_constructor_(self, e) -> FiniteField_givaroElement:
        """Coerce several data types to self."""
        ...

    def gen(self, n: int = 0) -> FiniteField_givaroElement:
        """Return a generator of self over its prime field."""
        ...

    def prime_subfield(self) -> FiniteField:
        """Return the prime subfield GF(p) of self if self is GF(p^n)."""
        ...

    def log_to_int(self, n: int) -> int:
        """Convert log representation to integer representation."""
        ...

    def int_to_log(self, n: int) -> int:
        """Convert integer representation to log representation."""
        ...

    def from_integer(self, n: int) -> FiniteField_givaroElement:
        """Given integer n return a finite field element equal to n."""
        ...

    def _pari_modulus(self):
        """Return the modulus of self in a format for PARI."""
        ...

    def __iter__(self):
        """Finite fields may be iterated over."""
        ...

    def a_times_b_plus_c(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        """Return a*b + c."""
        ...

    def a_times_b_minus_c(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        """Return a*b - c."""
        ...

    def c_minus_a_times_b(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        """Return c - a*b."""
        ...

    def frobenius_endomorphism(self, n: int = 1):
        """Return the n-th power of the absolute arithmetic Frobenius endomorphism."""
        ...
