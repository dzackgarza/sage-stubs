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

def reallocate_mpq_vector(
    v: builtins.object, num_nonzero: builtins.object
) -> ElementConstructorInput: ...
def allocate_mpq_vector(
    v: builtins.object, num_nonzero: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_init(
    v: builtins.object, degree: builtins.object, num_nonzero: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_clear(v: builtins.object) -> ElementConstructorInput: ...
def mpq_binary_search0(
    v: builtins.object, n: builtins.object, x: builtins.object
) -> ElementConstructorInput: ...
def mpq_binary_search(
    v: builtins.object, n: builtins.object, x: builtins.object, ins: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_get_entry(
    ans: builtins.object, v: builtins.object, n: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_is_entry_zero_unsafe(
    v: builtins.object, n: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_to_list(v: builtins.object) -> ElementConstructorInput: ...
def mpq_vector_set_entry(
    v: builtins.object, n: builtins.object, x: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_set_entry_str(
    v: builtins.object, n: builtins.object, x_str: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_scale(
    v: builtins.object, scalar: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_scalar_multiply(
    v: builtins.object, w: builtins.object, scalar: builtins.object
) -> ElementConstructorInput: ...
def mpq_vector_cmp(
    v: builtins.object, w: builtins.object
) -> ElementConstructorInput: ...
