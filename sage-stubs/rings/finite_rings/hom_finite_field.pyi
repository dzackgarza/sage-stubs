from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.morphism import FrobeniusEndomorphism_generic
from sage.structure.element import Element


class FrobeniusEndomorphism_finite_field(FrobeniusEndomorphism_generic):
    def __init__(self, domain: FiniteField, n: int = 1) -> None: ...
    def _call_(self, x: Element) -> Element: ...
