from typing import TYPE_CHECKING

from sage.categories.morphism import Morphism
from sage.rings.integer import Integer
from sage.structure.parent import Parent
from sage.structure.element import Element
from sage.categories.map import Map

if TYPE_CHECKING:
    from sage.categories.homset import Homset

class RingMap(Morphism):
    """Set-theoretic map between rings."""

    def _repr_type(self) -> str: ...

class RingMap_lift(RingMap):
    """Lifting map from a quotient ring to its parent."""

    S: Parent
    to_S: Map

    def __init__(self, R: Parent, S: Parent) -> None: ...

class RingHomomorphism(RingMap):
    """Homomorphism of rings."""

    _lift: Morphism
    _cached_methods: dict

class RingHomomorphism_im_gens(RingHomomorphism):
    """Ring homomorphism defined by images of generators."""

    _im_gens: object
    _base_map: object

class RingHomomorphism_from_base(RingHomomorphism):
    """Ring homomorphism induced from a base ring homomorphism."""

    _underlying: object

class RingHomomorphism_from_fraction_field(RingHomomorphism):
    """Ring homomorphism from a fraction field."""

    _morphism: object

class RingHomomorphism_cover(RingHomomorphism):
    """Natural quotient map from a ring to its quotient."""

    pass

class RingHomomorphism_from_quotient(RingHomomorphism):
    """Ring homomorphism from a quotient ring."""

    phi: object

class FrobeniusEndomorphism_generic(RingHomomorphism):
    """Frobenius endomorphism on a ring of characteristic p."""

    _p: Integer
    _q: Integer
    _power: int
