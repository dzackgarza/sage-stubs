from collections.abc import Iterator, Sequence
from typing import Self, TypeVar
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.rational import Rational
from sage.rings.real_double import RealDoubleElement
from sage.rings.complex_double import ComplexDoubleElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.ring import Ring
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput
from sage.structure.sage_object import SageObject
from sage.symbolic.expression import Expression

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class FilteredVectorSpace_class(FreeModule_ambient_field):
    def __init__(
        self,
        base_ring: Field,
        dim: int,
        generators: ElementConstructorInput,
        filtration: ElementConstructorInput,
        check: bool = ...,
    ) -> None: ...
    def change_ring(self, base_ring: Field) -> FilteredVectorSpace_class: ...
    def ambient_vector_space(self) -> FreeModule_ambient_field: ...
    def is_constant(self) -> bool: ...
    def is_exhaustive(self) -> bool: ...
    def is_separated(self) -> bool: ...
    def graded(self, degree: int) -> FreeModule_ambient_field: ...
    def grading_type(self) -> str: ...
    def presentation(self) -> FreeModule_generic: ...
    def support(self) -> FreeModule_generic: ...
    def num_graded_parts(self) -> int: ...
    def graded_dimension(self, degree: int) -> int: ...

def FilteredVectorSpace(
    generators: ElementConstructorInput = ...,
    filtration: ElementConstructorInput = ...,
    base_ring: Field | None = ...,
) -> FilteredVectorSpace_class: ...
