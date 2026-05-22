
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.categories.homset import Homset
from sage.structure.sequence import Sequence_generic
class NumberFieldHomomorphism_im_gens:
    

    def __invert__(self) -> NumberFieldHomomorphism_im_gens:
        
        ...

    def preimage(self, y: NumberFieldElement) -> NumberFieldElement:
        
        ...

class RelativeNumberFieldHomomorphism_from_abs:
    

    def __init__(
        self,
        parent: Homset[NumberField_generic, NumberField_generic],
        abs_hom: NumberFieldHomomorphism_im_gens,
    ) -> None: ...

    def abs_hom(self) -> NumberFieldHomomorphism_im_gens:
        
        ...

    def _repr_type(self) -> str:
        
        ...

    def im_gens(self) -> Sequence_generic:
        
        ...

    def _richcmp_(self, other: RelativeNumberFieldHomomorphism_from_abs, op: int) -> bool:
        
        ...

    def _repr_defn(self) -> str:
        
        ...

    def _call_(self, x: NumberFieldElement) -> NumberFieldElement:
        
        ...

class CyclotomicFieldHomomorphism_im_gens(NumberFieldHomomorphism_im_gens):
    ...
