from sage.rings.function_field.element import FunctionFieldElement
from sage.rings.function_field.function_field import FunctionField
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput

class FunctionFieldFactory(UniqueFactory):
    def create_key(
        self, F: FunctionField, names: str | tuple[str, ...]
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        key: tuple[ElementConstructorInput, ...],
        **extra_args: ElementConstructorInput,
    ) -> FunctionFieldFactory: ...

FunctionField: FunctionFieldElement

class FunctionFieldExtensionFactory(UniqueFactory):
    def create_key(
        self, polynomial: Polynomial | MPolynomial, names: str | tuple[str, ...]
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        key: tuple[ElementConstructorInput, ...],
        **extra_args: ElementConstructorInput,
    ) -> FunctionFieldExtensionFactory: ...

FunctionFieldExtension: FunctionFieldElement
