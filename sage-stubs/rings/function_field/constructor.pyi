from sage.rings.function_field.function_field import (
    FunctionField as FunctionFieldParent,
)
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.ring import Field
from sage.structure.factory import UniqueFactory
from sage.structure.parent import ElementConstructorInput

class FunctionFieldFactory(UniqueFactory):
    def create_key(
        self, F: Field, names: str | tuple[str, ...]
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        key: tuple[ElementConstructorInput, ...],
        **extra_args: ElementConstructorInput,
    ) -> FunctionFieldParent: ...

FunctionField: FunctionFieldFactory

class FunctionFieldExtensionFactory(UniqueFactory):
    def create_key(
        self, polynomial: Polynomial | MPolynomial, names: str | tuple[str, ...]
    ) -> tuple[ElementConstructorInput, ...]: ...
    def create_object(
        self,
        version: int | tuple[int, ...],
        key: tuple[ElementConstructorInput, ...],
        **extra_args: ElementConstructorInput,
    ) -> FunctionFieldParent: ...

FunctionFieldExtension: FunctionFieldExtensionFactory
