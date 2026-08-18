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

from sage.matrix.matrix import Matrix

class PermutationGroup: ...

def basis_of_short_vectors(
    self: object, show_lengths: bool = False
) -> ElementConstructorInput: ...
def short_vector_list_up_to_length(
    self: object, len_bound: int, up_to_sign_flag: bool = False
) -> ElementConstructorInput: ...
def short_primitive_vector_list_up_to_length(
    self: object, len_bound: int, up_to_sign_flag: bool = False
) -> ElementConstructorInput: ...
def _compute_automorphisms(self: object) -> ElementConstructorInput: ...
def automorphism_group(self: object) -> PermutationGroup: ...
def automorphisms(self: object) -> ElementConstructorInput: ...
def number_of_automorphisms(self: object) -> int: ...
def set_number_of_automorphisms(self: object, n: int) -> None: ...
