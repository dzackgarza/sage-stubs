from sage.groups.abelian_gps.abelian_group_gap import (
    AbelianGroupElement_gap,
    AbelianGroupGap,
)
from sage.rings.integer import Integer
from sage.rings.rational import Rational

# spinor_genus.py:35.
class SpinorOperator(AbelianGroupElement_gap):
    def _repr_(self) -> str: ...

# spinor_genus.py:78: the group of spinor operators, a product of p-adic unit
# square classes at the given primes.
class SpinorOperators(AbelianGroupGap):
    # spinor_genus.py:95: a tuple of primes (p_1 = 2, ..., p_n).
    def __init__(self, primes: tuple[int | Integer, ...]) -> None: ...
    # spinor_genus.py:113: returns SpinorOperators, (self._primes,).
    def __reduce__(
        self,
    ) -> tuple[type[SpinorOperators], tuple[tuple[int | Integer, ...]]]: ...
    # spinor_genus.py:130.
    Element: type[SpinorOperator]
    def _repr_(self) -> str: ...
    # spinor_genus.py:144: x is a nonzero rational number and p a prime; the
    # result is self.one() times generators of self.
    def to_square_class(
        self, x: int | Integer | Rational, p: int | Integer
    ) -> SpinorOperator: ...
    # spinor_genus.py:191: r is a nonzero integer and prime a prime or -1; the
    # result is a product of square classes in self.
    def delta(
        self, r: int | Integer, prime: int | Integer | None = None
    ) -> SpinorOperator: ...
