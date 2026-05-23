from sage.categories.map import Map
from sage.modules.free_module import FreeModule_ambient_field
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement

class MapRelativeVectorSpaceToRelativeNumberField(Map):
    def __init__(self, V: FreeModule_ambient_field, K: NumberField_generic) -> None: ...
    def _call_(self, v: FreeModuleElement) -> NumberFieldElement: ...

class MapRelativeNumberFieldToRelativeVectorSpace(Map):
    def __init__(self, K: NumberField_generic, V: FreeModule_ambient_field) -> None: ...
    def _call_(self, alpha: NumberFieldElement) -> FreeModuleElement: ...

class MapVectorSpaceToRelativeNumberField(Map):
    def __init__(
        self,
        V: FreeModule_ambient_field,
        L: NumberField_generic,
        from_V: Map,
        from_K: Map,
    ) -> None: ...
    def _call_(self, x: FreeModuleElement) -> NumberFieldElement: ...

class MapRelativeNumberFieldToVectorSpace(Map):
    def __init__(
        self,
        L: NumberField_generic,
        V: FreeModule_ambient_field,
        to_K: Map,
        to_V: Map,
    ) -> None: ...
    def _call_(self, x: NumberFieldElement) -> FreeModuleElement: ...
