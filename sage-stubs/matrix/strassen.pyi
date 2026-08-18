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

def strassen_window_multiply(
    C: builtins.object, A: builtins.object, B: builtins.object, cutoff: builtins.object
) -> ElementConstructorInput: ...
def subtract_strassen_product(
    result: builtins.object,
    A: builtins.object,
    B: builtins.object,
    cutoff: builtins.object,
) -> ElementConstructorInput: ...
def strassen_echelon(
    A: builtins.object, cutoff: builtins.object
) -> ElementConstructorInput: ...
def strassen_echelon_c(
    A: builtins.object, cutoff: builtins.object, mul_cutoff: builtins.object
) -> ElementConstructorInput: ...

class int_range:
    def __init__(
        self, indices: builtins.object = ..., range: builtins.object = ...
    ) -> None: ...
    def intervals(self) -> ElementConstructorInput: ...
    def to_list(self) -> ElementConstructorInput: ...
    def __iter__(self) -> Iterator[FreeModuleElement[_Scalar]]: ...
    def __len__(self) -> builtins.int: ...
    def __add__(self, right: builtins.object) -> Self: ...
    def __sub__(self, right: builtins.object) -> Self: ...
    def __mul__(self, right: builtins.object) -> Self: ...

def test(
    n: builtins.object, m: builtins.object, R: builtins.object, c: builtins.object = ...
) -> ElementConstructorInput: ...
