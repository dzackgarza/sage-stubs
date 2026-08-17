from sage.rings.integer import Integer
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

def coords_in_U_mod_p(
    u: Polynomial | MPolynomial, U: ElementConstructorInput, p: int | Integer
) -> NumberFieldElement: ...
def basis_for_p_cokernel(
    S: NumberFieldElement | ElementConstructorInput,
    C: RingElement | int | Integer | Rational,
    p: int | Integer,
) -> NumberFieldElement: ...
def pSelmerGroup(
    K: NumberField_generic,
    S: NumberFieldElement | ElementConstructorInput,
    p: int | Integer,
    proof: bool = ...,
    debug: NumberField_generic = ...,
) -> NumberFieldElement: ...
