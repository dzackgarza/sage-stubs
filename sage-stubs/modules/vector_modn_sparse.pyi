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

import builtins

class _SageObject: ...

def allocate_c_vector_modint(
    v: builtins.object, num_nonzero: builtins.object
) -> ElementConstructorInput: ...
def clear_c_vector_modint(v: builtins.object) -> ElementConstructorInput: ...
def binary_search0_modn(
    v: builtins.object, n: builtins.object, x: builtins.object
) -> ElementConstructorInput: ...
def binary_search_modn(
    v: builtins.object, n: builtins.object, x: builtins.object, ins: builtins.object
) -> ElementConstructorInput: ...
def get_entry(v: builtins.object, n: builtins.object) -> ElementConstructorInput: ...
def is_entry_zero_unsafe(v: builtins.object, n: builtins.object) -> builtins.bool: ...
def to_list(v: builtins.object) -> ElementConstructorInput: ...
def set_entry(
    v: builtins.object, n: builtins.object, x: builtins.object
) -> ElementConstructorInput: ...
def scale_c_vector_modint(
    v: builtins.object, scalar: builtins.object
) -> ElementConstructorInput: ...
