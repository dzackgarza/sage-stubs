from sage.rings.commutative_ring_element import CommutativeRingElement
from sage.structure.sage_object import SageObject


class FiniteRingElement(CommutativeRingElement):
    ...


class FinitePolyExtElement(FiniteRingElement):
    ...


class Cache_base(SageObject):
    def fetch_int(self, number: int) -> FinitePolyExtElement: ...
