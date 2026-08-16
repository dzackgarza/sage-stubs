from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.rings.number_field.number_field import NumberField_generic
from sage.structure.parent import Parent

class RelativeNumberFieldHomset(Homset[NumberField_generic, NumberField_generic]):
    def __init__(
        self,
        R: NumberField_generic | Parent[_DomainElement],
        S: NumberField_generic | Parent[_CodomainElement],
        category: Category | None = ...,
    ) -> None: ...
