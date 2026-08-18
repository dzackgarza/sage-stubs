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

def count_modp_solutions__by_Gauss_sum(
    self: builtins.object, p: builtins.int, m: builtins.int
) -> ElementConstructorInput: ...
def local_good_density_congruence_odd(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object,
    NZvec: builtins.object,
) -> ElementConstructorInput: ...
def local_good_density_congruence_even(
    self: builtins.object,
    m: builtins.int,
    Zvec: builtins.object,
    NZvec: builtins.object,
) -> ElementConstructorInput: ...
def local_good_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
def local_zero_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
def local_badI_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
def local_badII_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
def local_bad_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
def local_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
def local_primitive_density_congruence(
    self: builtins.object,
    p: builtins.int,
    m: builtins.int,
    Zvec: builtins.object = ...,
    NZvec: builtins.object = ...,
) -> ElementConstructorInput: ...
