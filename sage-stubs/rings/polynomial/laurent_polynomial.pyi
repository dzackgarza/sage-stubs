from typing import TYPE_CHECKING

from sage.rings.polynomial.laurent_polynomial_ring import LaurentPolynomialRing
class LaurentPolynomial:
    

    def __init__(self) -> None: ...

    def derivative(self, var: str | None = None) -> LaurentPolynomial:
        
        ...

    def is_monomial(self) -> bool:
        
        ...

    def is_constant(self) -> bool:
        
        ...

    def degree(self, var: str | None = None) -> int:
        
        ...

    def content(self) -> object:
        
        ...

    def gcd(self, other) -> LaurentPolynomial:
        
        ...
