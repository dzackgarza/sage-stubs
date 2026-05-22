from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.rings.number_field.number_field import NumberField_generic
    from sage.rings.number_field.number_field_element import NumberFieldElement
    from sage.structure.sequence import Sequence

class NumberFieldHomomorphism_im_gens:
    """Morphism from one number field to another defined by images of generators."""

    def __invert__(self) -> NumberFieldHomomorphism_im_gens:
        """Return the inverse of an isomorphism of absolute number fields."""
        ...

    def preimage(self, y: NumberFieldElement) -> NumberFieldElement:
        """Compute a preimage of y in the domain, provided one exists."""
        ...

class RelativeNumberFieldHomomorphism_from_abs:
    """Homomorphism from a relative number field, stored as a homomorphism from the absolute field."""

    def __init__(self, parent, abs_hom) -> None: ...

    def abs_hom(self) -> NumberFieldHomomorphism_im_gens:
        """Return the corresponding homomorphism from the absolute number field."""
        ...

    def _repr_type(self) -> str:
        """Return a short string to identify the type of this homomorphism."""
        ...

    def im_gens(self) -> Sequence:
        """Return the images of the generators under this map."""
        ...

    def _richcmp_(self, other, op) -> bool:
        """Compare."""
        ...

    def _repr_defn(self) -> str:
        """Return a string describing the images of the generators under this map."""
        ...

    def _call_(self, x: NumberFieldElement) -> NumberFieldElement:
        """Evaluate this map at the element x."""
        ...

class CyclotomicFieldHomomorphism_im_gens(NumberFieldHomomorphism_im_gens):
    """Morphism from one cyclotomic field to another defined by images of generators."""
    ...
