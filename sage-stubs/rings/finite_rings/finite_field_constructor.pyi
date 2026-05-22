from sage.rings.integer import Integer
from sage.rings.finite_rings.finite_field_base import FiniteField

def GF(q: Integer, name: str = 'a', modulus: object = None, proof: bool = True, **kwds: object) -> FiniteField: ...
