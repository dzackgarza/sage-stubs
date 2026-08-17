from sage.categories.homset import hom
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.unique_representation import UniqueRepresentation

class MapAbsoluteToRelativeNumberField: ...
class MapRelativeToAbsoluteNumberField: ...
class NameChangeMap: ...

class NumberFieldStructure(UniqueRepresentation):
    def __init__(self, other: NumberField_generic) -> None: ...
    def create_structure(self, field: NumberField_generic) -> NumberFieldElement: ...

class NameChange(NumberFieldStructure):
    def create_structure(
        self, field: NumberField_generic
    ) -> tuple[NameChangeMap, NameChangeMap]: ...

class AbsoluteFromRelative(NumberFieldStructure):
    def create_structure(
        self, field: NumberField_generic
    ) -> tuple[MapAbsoluteToRelativeNumberField, MapRelativeToAbsoluteNumberField]: ...

class RelativeFromAbsolute(NumberFieldStructure):
    def __init__(
        self,
        other: NumberFieldElement | ElementConstructorInput,
        gen: ElementConstructorInput,
    ) -> None: ...
    def create_structure(
        self, field: NumberField_generic
    ) -> tuple[NumberFieldElement, hom]: ...

class RelativeFromRelative(NumberFieldStructure):
    def create_structure(
        self, field: NumberField_generic
    ) -> tuple[NumberFieldElement, NumberFieldElement]: ...
