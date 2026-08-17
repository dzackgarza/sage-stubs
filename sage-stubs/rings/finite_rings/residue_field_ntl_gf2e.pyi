from sage.rings.finite_rings.element_ntl_gf2e import FiniteField_ntl_gf2eElement
from sage.rings.finite_rings.finite_field_ntl_gf2e import FiniteField_ntl_gf2e
from sage.rings.finite_rings.maps_finite_field import FiniteFieldVectorSpaceIsomorphism
from sage.rings.finite_rings.residue_field import ResidueField_generic
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element

class ResidueFiniteField_ntl_gf2e(ResidueField_generic, FiniteField_ntl_gf2e):
    def __init__(
        self,
        q: int | Integer,
        name: str,
        modulus: Polynomial,
        repr: str,
        p: Ideal_generic,
        to_vs: FiniteFieldVectorSpaceIsomorphism,
        to_order: FiniteFieldVectorSpaceIsomorphism,
        PB: list[Element],
    ) -> None: ...
    def _element_constructor_(
        self,
        e: FiniteField_ntl_gf2eElement
        | Element
        | int
        | Integer
        | str
        | Polynomial
        | None,
    ) -> FiniteField_ntl_gf2eElement: ...
