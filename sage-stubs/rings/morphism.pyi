
from sage.categories.morphism import Morphism
from sage.rings.integer import Integer
from sage.structure.parent import Parent
from sage.structure.element import Element
from sage.categories.map import Map

from sage.categories.homset import Homset
class RingMap(Morphism):
    

    def _repr_type(self) -> str: ...

class RingMap_lift(RingMap):
    

    S: Parent
    to_S: Map

    def __init__(self, R: Parent, S: Parent) -> None: ...

class RingHomomorphism(RingMap):
    

    _lift: Morphism
    _cached_methods: dict[str, object]

class RingHomomorphism_im_gens(RingHomomorphism):
    

    _im_gens: object
    _base_map: object

class RingHomomorphism_from_base(RingHomomorphism):
    

    _underlying: object

class RingHomomorphism_from_fraction_field(RingHomomorphism):
    

    _morphism: object

class RingHomomorphism_cover(RingHomomorphism):
    ...


class RingHomomorphism_from_quotient(RingHomomorphism):
    

    phi: object

class FrobeniusEndomorphism_generic(RingHomomorphism):
    

    _p: Integer
    _q: Integer
    _power: int
