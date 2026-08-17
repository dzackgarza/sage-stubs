from collections.abc import Iterator

from sage.rings.integer import Integer
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.structure.sage_object import SageObject

class Small_primes_of_degree_one_iter(SageObject):
    def __init__(
        self,
        field: NumberField_generic,
        num_integer_primes: int | Integer = ...,
        max_iterations: int | Integer = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[NumberFieldElement]: ...
    def __next__(self) -> NumberFieldElement: ...
    next: NumberFieldElement
