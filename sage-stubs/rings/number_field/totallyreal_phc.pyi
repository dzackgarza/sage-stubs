from sage.rings.integer import Integer
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.structure.parent import ElementConstructorInput

def coefficients_to_power_sums(
    n: int | Integer, m: int | Integer, a: NumberFieldElement | ElementConstructorInput
) -> NumberFieldElement: ...
