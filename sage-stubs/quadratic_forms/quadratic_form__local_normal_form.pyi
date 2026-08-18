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

from sage.quadratic_forms.quadratic_form import QuadraticForm

def find_entry_with_minimal_scale_at_prime(
    self: object, prime: int
) -> tuple[int, int]: ...
def local_normal_form(
    self: object,
    prime: int,
    *args: ElementConstructorInput,
    **kwargs: ElementConstructorInput,
) -> QuadraticForm: ...
def jordan_blocks_by_scale_and_unimodular(
    self: object, prime: int
) -> ElementConstructorInput: ...
def jordan_blocks_in_unimodular_list_by_scale_power(
    self: object, prime: int, *args: ElementConstructorInput
) -> ElementConstructorInput: ...
