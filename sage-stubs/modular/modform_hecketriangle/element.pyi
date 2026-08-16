from sage.lfunctions.dokchitser import Dokchitser
from sage.modular.modform_hecketriangle.abstract_space import FormsSpace_abstract
from sage.modular.modform_hecketriangle.graded_ring_element import FormsRingElement
from sage.structure.element import Element, Vector

class FormsElement(FormsRingElement):
    def __init__(self, parent: FormsSpace_abstract, rat: Element) -> None: ...
    def coordinate_vector(self) -> Vector: ...
    def ambient_coordinate_vector(self) -> Vector: ...
    def lseries(
        self,
        num_prec: int | None = ...,
        max_imaginary_part: float = ...,
        max_asymp_coeffs: int = ...,
    ) -> Dokchitser: ...
