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

def p_saturation(
    A: builtins.object, p: builtins.int, proof: builtins.bool = ...
) -> ElementConstructorInput: ...
def random_sublist_of_size(
    k: builtins.int, n: builtins.int
) -> ElementConstructorInput: ...
def solve_system_with_difficult_last_row(
    B: builtins.object, A: builtins.object
) -> ElementConstructorInput: ...
def saturation(
    A: builtins.object,
    proof: builtins.bool = ...,
    p: builtins.int = ...,
    max_dets: builtins.int = ...,
) -> ElementConstructorInput: ...
def index_in_saturation(
    A: builtins.object, proof: builtins.bool = ...
) -> ElementConstructorInput: ...
