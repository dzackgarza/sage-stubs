from collections.abc import Callable

from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.interfaces.r import R
from sage.misc.weak_dict import _K, _V
from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.function_field import FunctionField
from sage.rings.function_field.place import FunctionFieldPlace
from sage.rings.integer import Integer
from sage.rings.morphism import RingHomomorphism
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

class FunctionFieldVectorSpaceIsomorphism(Morphism):
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def __hash__(self) -> int: ...
    def _repr_(self) -> str: ...
    def _richcmp_(
        self,
        other: FunctionFieldElement | ElementConstructorInput,
        op: ElementConstructorInput,
    ) -> bool: ...

class MapVectorSpaceToFunctionField(FunctionFieldVectorSpaceIsomorphism):
    def __init__(self, V: ElementConstructorInput, K: FunctionField) -> None: ...
    def domain(self) -> Parent: ...
    def codomain(self) -> Parent: ...
    def _call_(self, v: FunctionField) -> _K: ...

class MapFunctionFieldToVectorSpace(FunctionFieldVectorSpaceIsomorphism):
    def __init__(self, K: FunctionField, V: ElementConstructorInput) -> None: ...
    def _call_(self, x: FunctionFieldElement | ElementConstructorInput) -> _V: ...

class FunctionFieldMorphism(RingHomomorphism):
    def __init__(
        self,
        parent: FunctionField,
        im_gen: ElementConstructorInput,
        base_morphism: Map | Morphism,
    ) -> None: ...

class FunctionFieldMorphism_polymod(FunctionFieldMorphism):
    def __init__(
        self,
        parent: FunctionField,
        im_gen: ElementConstructorInput,
        base_morphism: Map | Morphism,
    ) -> None: ...
    def _call_(self, x: FunctionFieldElement | ElementConstructorInput) -> Element: ...

class FunctionFieldMorphism_rational(FunctionFieldMorphism):
    def __init__(
        self,
        parent: FunctionField,
        im_gen: ElementConstructorInput,
        base_morphism: Map | Morphism,
    ) -> None: ...
    def _call_(
        self, x: FunctionFieldElement | ElementConstructorInput
    ) -> R | RingElement | FunctionFieldElement: ...

class FunctionFieldConversionToConstantBaseField(Map):
    def __init__(self, parent: FunctionField) -> None: ...
    def _call_(
        self, x: FunctionFieldElement | ElementConstructorInput
    ) -> FunctionFieldElement: ...

class FunctionFieldToFractionField(FunctionFieldVectorSpaceIsomorphism):
    def section(self) -> Morphism: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> FunctionFieldElement: ...

class FractionFieldToFunctionField(FunctionFieldVectorSpaceIsomorphism):
    def section(self) -> Morphism: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> FunctionFieldElement: ...

class FunctionFieldCompletion(Map):
    def __init__(
        self,
        field: FunctionField,
        place: FunctionFieldPlace,
        name: str = ...,
        prec: int | Integer = ...,
        gen_name: str = ...,
    ) -> None: ...
    def default_precision(self) -> int | Integer: ...
    def _call_(
        self, f: Polynomial | MPolynomial | Map | Callable[..., Element]
    ) -> FunctionFieldElement: ...

class FunctionFieldRingMorphism(SetMorphism):
    def _repr_(self) -> str: ...

class FunctionFieldLinearMap(SetMorphism):
    def _repr_(self) -> str: ...

class FunctionFieldLinearMapSection(SetMorphism):
    def _repr_(self) -> str: ...
