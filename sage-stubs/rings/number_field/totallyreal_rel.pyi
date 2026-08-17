from sage.rings.integer import Integer
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject

def integral_elements_in_box(
    K: NumberField_generic, C: RingElement | int | Integer | Rational
) -> NumberFieldElement: ...

eps_global: NumberFieldElement

class tr_data_rel(SageObject):
    def __init__(
        self,
        F: ElementConstructorInput,
        m: int | Integer,
        B: NumberFieldElement | ElementConstructorInput,
        a: NumberFieldElement | ElementConstructorInput = ...,
    ) -> None: ...
    def incr(
        self,
        f_out: int | Integer,
        verbose: int | Integer = ...,
        haltk: int | Integer = ...,
    ) -> NumberFieldElement: ...

def enumerate_totallyreal_fields_rel(
    F: Polynomial | MPolynomial,
    m: int | Integer,
    B: NumberFieldElement | ElementConstructorInput,
    a: NumberFieldElement | ElementConstructorInput = ...,
    verbose: int | Integer = ...,
    return_seqs: int | Integer = ...,
    return_pari_objects: int | Integer = ...,
) -> NumberFieldElement: ...
def enumerate_totallyreal_fields_all(
    n: int | Integer,
    B: NumberFieldElement | ElementConstructorInput,
    verbose: int | Integer = ...,
    return_seqs: int | Integer = ...,
    return_pari_objects: int | Integer = ...,
) -> NumberFieldElement: ...
