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

def find_primitive_p_divisible_vector__random(
    self: builtins.object, p: builtins.int
) -> ElementConstructorInput: ...
def find_primitive_p_divisible_vector__next(
    self: builtins.object, p: builtins.int, v: builtins.object = ...
) -> ElementConstructorInput: ...
def find_p_neighbor_from_vec(
    self: builtins.object,
    p: builtins.int,
    y: builtins.object,
    return_matrix: builtins.bool = ...,
) -> ElementConstructorInput: ...
def neighbor_iteration(
    seeds: builtins.object,
    p: builtins.int,
    mass: builtins.object = ...,
    max_classes: builtins.object = ...,
    algorithm: builtins.str = ...,
    max_neighbors: builtins.int = ...,
    verbose: builtins.bool = ...,
) -> ElementConstructorInput: ...
def orbits_lines_mod_p(
    self: builtins.object, p: builtins.int
) -> ElementConstructorInput: ...
