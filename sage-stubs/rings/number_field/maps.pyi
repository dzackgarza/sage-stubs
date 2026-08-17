from sage.categories.map import Map
from sage.modules.free_module import FreeModule_ambient_field
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.function_field.function_field import FunctionField
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.ring import Field, Ring
from sage.structure.parent import ElementConstructorInput

class MapRelativeVectorSpaceToRelativeNumberField(NumberFieldIsomorphism, Map):
    def __init__(self, V: FreeModule_ambient_field, K: NumberField_generic) -> None: ...
    def _call_(self, v: FreeModuleElement) -> NumberFieldElement: ...

class MapRelativeNumberFieldToRelativeVectorSpace(NumberFieldIsomorphism, Map):
    def __init__(self, K: NumberField_generic, V: FreeModule_ambient_field) -> None: ...
    def _call_(self, alpha: NumberFieldElement) -> FreeModuleElement: ...

class MapVectorSpaceToRelativeNumberField(NumberFieldIsomorphism, Map):
    def __init__(
        self,
        V: FreeModule_ambient_field,
        L: NumberField_generic,
        from_V: Map,
        from_K: Map,
    ) -> None: ...
    def _call_(self, x: FreeModuleElement) -> NumberFieldElement: ...

class MapRelativeNumberFieldToVectorSpace(NumberFieldIsomorphism, Map):
    def __init__(
        self, L: NumberField_generic, V: FreeModule_ambient_field, to_K: Map, to_V: Map
    ) -> None: ...
    def _call_(self, x: NumberFieldElement) -> FreeModuleElement: ...

class NumberFieldIsomorphism(Map):
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...

class MapVectorSpaceToNumberField(NumberFieldIsomorphism):
    def __init__(
        self, V: ElementConstructorInput, K: NumberField_generic | FunctionField | Field
    ) -> None: ...
    def _call_(self, v: ElementConstructorInput) -> NumberFieldElement: ...

class MapNumberFieldToVectorSpace(Map):
    def __init__(
        self, K: NumberField_generic | FunctionField | Field, V: ElementConstructorInput
    ) -> None: ...
    def _call_(
        self, x: NumberFieldElement | ElementConstructorInput
    ) -> NumberFieldElement: ...

class NameChangeMap(NumberFieldIsomorphism):
    def __init__(
        self,
        K: NumberField_generic | FunctionField | Field,
        L: NumberField_generic | FunctionField | Field,
    ) -> None: ...
    def _call_(
        self, x: NumberFieldElement | ElementConstructorInput
    ) -> NumberFieldElement: ...

class MapRelativeToAbsoluteNumberField(NumberFieldIsomorphism):
    def __init__(
        self, R: Ring, A: NumberFieldElement | ElementConstructorInput
    ) -> None: ...
    def _call_(
        self, x: NumberFieldElement | ElementConstructorInput
    ) -> NumberFieldElement: ...

class MapAbsoluteToRelativeNumberField(NumberFieldIsomorphism):
    def __init__(
        self, A: NumberFieldElement | ElementConstructorInput, R: Ring
    ) -> None: ...
    def _call_(
        self, x: NumberFieldElement | ElementConstructorInput
    ) -> NumberFieldElement: ...
