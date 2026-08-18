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

def mass__by_Siegel_densities(
    self: builtins.object,
    odd_algorithm: builtins.str = ...,
    even_algorithm: builtins.str = ...,
) -> ElementConstructorInput: ...
def Pall_mass_density_at_odd_prime(
    self: builtins.object, p: builtins.int
) -> ElementConstructorInput: ...
def Watson_mass_at_2(self: builtins.object) -> ElementConstructorInput: ...
def Kitaoka_mass_at_2(self: builtins.object) -> ElementConstructorInput: ...
def mass_at_two_by_counting_mod_power(
    self: builtins.object, k: builtins.int
) -> ElementConstructorInput: ...
