from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.rings.number_field.number_field import NumberField_generic

class RelativeNumberFieldHomset(Homset[NumberField_generic, NumberField_generic]):
    def __init__(
        self,
        R: NumberField_generic,
        S: NumberField_generic,
        category: Category | None = ...,
    ) -> None: ...
