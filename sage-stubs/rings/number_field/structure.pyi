from sage.rings.number_field.number_field import NumberField_generic

class NumberFieldStructure:
    other: NumberField_generic

    def __init__(self, other: NumberField_generic) -> None: ...
