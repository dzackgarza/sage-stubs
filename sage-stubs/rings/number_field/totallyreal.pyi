from collections.abc import Iterator

from sage.rings.integer import Integer
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import ElementConstructorInput

def odlyzko_bound_totallyreal(n: int | Integer) -> NumberFieldElement: ...
def weed_fields(
    S: NumberFieldElement | ElementConstructorInput, lenS: ElementConstructorInput = ...
) -> NumberFieldElement: ...
def enumerate_totallyreal_fields_prim(
    n: int | Integer,
    B: NumberFieldElement | ElementConstructorInput,
    a: NumberFieldElement | ElementConstructorInput = ...,
    verbose: ElementConstructorInput = ...,
    return_seqs: ElementConstructorInput = ...,
    phc: ElementConstructorInput = ...,
    keep_fields: ElementConstructorInput = ...,
    t_2: ElementConstructorInput = ...,
    just_print: ElementConstructorInput = ...,
    return_pari_objects: ElementConstructorInput = ...,
) -> Iterator[tuple[Polynomial, NumberField_generic]]: ...
