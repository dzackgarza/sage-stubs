from sage.structure.element import Element

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

    def content(self) -> Element:
        
        ...

    def gcd(self, other: LaurentPolynomial | int) -> LaurentPolynomial:
        
        ...
