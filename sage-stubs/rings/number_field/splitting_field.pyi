from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject

class SplittingFieldAbort(Exception):
    def __init__(
        self, div: ElementConstructorInput, mult: ElementConstructorInput
    ) -> None: ...

class SplittingData(SageObject):
    def __init__(
        self, _pol: ElementConstructorInput, _dm: ElementConstructorInput
    ) -> None: ...
    def key(self) -> NumberFieldElement: ...
    def poldegree(self) -> NumberFieldElement: ...

def splitting_field(
    poly: Polynomial | MPolynomial,
    name: str,
    map: bool = ...,
    degree_multiple: Polynomial | MPolynomial = ...,
    abort_degree: Polynomial | MPolynomial = ...,
    simplify: Polynomial | MPolynomial = ...,
    simplify_all: Polynomial | MPolynomial = ...,
) -> NumberFieldElement: ...
