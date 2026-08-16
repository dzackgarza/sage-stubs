from sage.rings.finite_rings.element_pari_ffelt import FiniteFieldElement_pari_ffelt
from sage.rings.finite_rings.finite_field_pari_ffelt import FiniteField_pari_ffelt
from sage.rings.finite_rings.maps_finite_field import FiniteFieldVectorSpaceIsomorphism
from sage.rings.finite_rings.residue_field import ResidueField_generic
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element

class ResidueFiniteField_pari_ffelt(ResidueField_generic, FiniteField_pari_ffelt):
    def __init__(self, p: Ideal_generic, characteristic: Integer, name: str, modulus: Polynomial, to_vs: FiniteFieldVectorSpaceIsomorphism, to_order: FiniteFieldVectorSpaceIsomorphism, PB: list[Element]) -> None: ...
    def _element_constructor_(self, x: Element) -> FiniteFieldElement_pari_ffelt: ...
