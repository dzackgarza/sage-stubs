from typing import TYPE_CHECKING
from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.integer import Integer

from sage.rings.finite_rings.element_givaro import FiniteField_givaroElement
class FiniteField_givaro(FiniteField):
    

    _cache: object
    _modulus: object

    def __init__(
        self,
        q,
        name: str = "a",
        modulus=None,
        repr: str = "poly",
        cache: bool = False,
    ) -> None: ...

    def characteristic(self) -> Integer:
        
        ...

    def order(self) -> Integer:
        
        ...

    def degree(self) -> Integer:
        
        ...

    def _repr_option(self, key: str) -> bool:
        
        ...

    def random_element(self, *args, **kwds) -> FiniteField_givaroElement:
        
        ...

    def _element_constructor_(self, e) -> FiniteField_givaroElement:
        
        ...

    def gen(self, n: int = 0) -> FiniteField_givaroElement:
        
        ...

    def prime_subfield(self) -> FiniteField:
        
        ...

    def log_to_int(self, n: int) -> int:
        
        ...

    def int_to_log(self, n: int) -> int:
        
        ...

    def from_integer(self, n: int) -> FiniteField_givaroElement:
        
        ...

    def _pari_modulus(self):
        
        ...

    def __iter__(self):
        
        ...

    def a_times_b_plus_c(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        
        ...

    def a_times_b_minus_c(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        
        ...

    def c_minus_a_times_b(
        self,
        a: FiniteField_givaroElement,
        b: FiniteField_givaroElement,
        c: FiniteField_givaroElement,
    ) -> FiniteField_givaroElement:
        
        ...

    def frobenius_endomorphism(self, n: int = 1):
        
        ...
