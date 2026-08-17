from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.rings.number_field.number_field import NumberField_generic
from sage.rings.number_field.number_field_element import NumberFieldElement
from sage.rings.ring import Ring
from sage.structure.element import Element
from sage.structure.parent import ElementConstructorInput

class NumberFieldEmbedding(Morphism):
    def __init__(
        self, K: NumberField_generic, R: Ring, gen_embedding: ElementConstructorInput
    ) -> None: ...
    def gen_image(self) -> NumberFieldElement: ...
    def _call_(self, x: NumberFieldElement | ElementConstructorInput) -> Element: ...
    def _repr_defn(self) -> str: ...

class EmbeddedNumberFieldMorphism(NumberFieldEmbedding):
    def __init__(
        self,
        K: NumberField_generic,
        L: NumberField_generic,
        ambient_field: ElementConstructorInput = ...,
    ) -> None: ...
    def section(self) -> Morphism: ...

class EmbeddedNumberFieldConversion(Map):
    def __init__(
        self,
        K: NumberField_generic,
        L: NumberField_generic,
        ambient_field: ElementConstructorInput = ...,
    ) -> None: ...
    def _call_(self, x: NumberFieldElement | ElementConstructorInput) -> Element: ...

def matching_root(
    poly: ElementConstructorInput,
    target: ElementConstructorInput,
    ambient_field: ElementConstructorInput = ...,
    margin: ElementConstructorInput = ...,
    max_prec: ElementConstructorInput = ...,
) -> NumberFieldElement: ...
def closest(
    target: ElementConstructorInput,
    values: ElementConstructorInput,
    margin: ElementConstructorInput = ...,
) -> NumberFieldElement: ...
def root_from_approx(
    f: ElementConstructorInput, a: NumberFieldElement | ElementConstructorInput
) -> NumberFieldElement: ...
def create_embedding_from_approx(
    K: NumberField_generic, gen_image: ElementConstructorInput
) -> NumberFieldElement: ...

class CyclotomicFieldEmbedding(NumberFieldEmbedding):
    def __init__(self, K: NumberField_generic, L: NumberField_generic) -> None: ...
    def section(self) -> Morphism: ...
    def _call_(self, x: NumberFieldElement | ElementConstructorInput) -> Element: ...

class CyclotomicFieldConversion(Map):
    def __init__(self, K: NumberField_generic, L: NumberField_generic) -> None: ...
    def _call_(self, x: NumberFieldElement | ElementConstructorInput) -> Element: ...
