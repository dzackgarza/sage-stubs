from sage.rings.finite_rings.finite_field_givaro import FiniteField_givaro
from sage.rings.finite_rings.hom_finite_field import (
    FiniteFieldHomomorphism_generic,
    FrobeniusEndomorphism_finite_field,
    SectionFiniteFieldHomomorphism_generic,
)
from sage.rings.finite_rings.homset import FiniteFieldHomset
from sage.structure.element import Element

class SectionFiniteFieldHomomorphism_givaro(SectionFiniteFieldHomomorphism_generic):
    def __init__(self, inverse: FiniteFieldHomomorphism_givaro) -> None: ...
    def _call_(self, x: Element) -> Element: ...

class FiniteFieldHomomorphism_givaro(FiniteFieldHomomorphism_generic):
    def __init__(
        self,
        parent: FiniteFieldHomset,
        im_gens: tuple[Element, ...] | None = None,
        check: bool = False,
    ) -> None: ...
    def _call_(self, x: Element) -> Element: ...

class FrobeniusEndomorphism_givaro(FrobeniusEndomorphism_finite_field):
    def __init__(self, domain: FiniteField_givaro, power: int = 1) -> None: ...
    def fixed_field(
        self,
    ) -> tuple[FiniteField_givaro, FiniteFieldHomomorphism_givaro]: ...
