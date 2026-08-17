from sage.rings.finite_rings.element_givaro import FiniteField_givaroElement
from sage.rings.finite_rings.finite_field_givaro import FiniteField_givaro
from sage.rings.finite_rings.maps_finite_field import FiniteFieldVectorSpaceIsomorphism
from sage.rings.finite_rings.residue_field import ResidueField_generic
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element

class ResidueFiniteField_givaro(ResidueField_generic, FiniteField_givaro):
    def __init__(
        self,
        p: Ideal_generic,
        q: int | Integer,
        name: str,
        modulus: Polynomial,
        to_vs: FiniteFieldVectorSpaceIsomorphism,
        to_order: FiniteFieldVectorSpaceIsomorphism,
        PB: list[Element],
    ) -> None: ...
    def _element_constructor_(
        self,
        e: FiniteField_givaroElement
        | Element
        | int
        | Integer
        | str
        | Polynomial
        | None,
    ) -> FiniteField_givaroElement: ...
