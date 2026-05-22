from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing

class LaurentPolynomial:
    """Base class for Laurent polynomials."""

    def __init__(self) -> None: ...

    def derivative(self, var: str | None = None) -> LaurentPolynomial:
        """Return the derivative of this Laurent polynomial."""
        ...

    def is_monomial(self) -> bool:
        """Return True if this is a monomial."""
        ...

    def is_constant(self) -> bool:
        """Return True if this is a constant."""
        ...

    def degree(self, var: str | None = None) -> int:
        """Return the degree in the variable var."""
        ...

    def content(self) -> object:
        """Return the content of this Laurent polynomial."""
        ...

    def gcd(self, other) -> LaurentPolynomial:
        """Return the gcd of this and other."""
        ...
