from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.modules.free_module import FreeModule_ambient_field
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.structure.parent import Parent

class MapRelativeVectorSpaceToRelativeNumberField(Map):
    def __init__(
        self,
        V: FreeModule_ambient_field
        | Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ],
        K: NumberField_generic | Parent[_CodomainElement] | None,
    ) -> None: ...
    def _call_(self, v: FreeModuleElement) -> NumberFieldElement: ...

class MapRelativeNumberFieldToRelativeVectorSpace(Map):
    def __init__(
        self,
        K: NumberField_generic
        | Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ],
        V: FreeModule_ambient_field | Parent[_CodomainElement] | None,
    ) -> None: ...
    def _call_(self, alpha: NumberFieldElement) -> FreeModuleElement: ...

class MapVectorSpaceToRelativeNumberField(Map):
    def __init__(
        self,
        V: FreeModule_ambient_field
        | Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ],
        L: NumberField_generic | Parent[_CodomainElement] | None,
        from_V: Map,
        from_K: Map,
    ) -> None: ...
    def _call_(self, x: FreeModuleElement) -> NumberFieldElement: ...

class MapRelativeNumberFieldToVectorSpace(Map):
    def __init__(
        self,
        L: NumberField_generic
        | Homset[
            Map[_DomainElement, _CodomainElement], _DomainElement, _CodomainElement
        ],
        V: FreeModule_ambient_field | Parent[_CodomainElement] | None,
        to_K: Map,
        to_V: Map,
    ) -> None: ...
    def _call_(self, x: NumberFieldElement) -> FreeModuleElement: ...
