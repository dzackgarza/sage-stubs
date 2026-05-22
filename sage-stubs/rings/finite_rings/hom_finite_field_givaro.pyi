from sage.rings.finite_rings.finite_field_givaro import FiniteField_givaro
from sage.rings.finite_rings.hom_finite_field import FrobeniusEndomorphism_finite_field


class FrobeniusEndomorphism_givaro(FrobeniusEndomorphism_finite_field):
    def __init__(self, domain: FiniteField_givaro, power: int = 1) -> None: ...
