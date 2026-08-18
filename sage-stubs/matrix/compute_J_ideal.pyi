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

def lifting(
    p: builtins.int, t: builtins.object, A: builtins.object, G: builtins.object
) -> ElementConstructorInput: ...
def p_part(f: builtins.object, p: builtins.int) -> ElementConstructorInput: ...

class ComputeMinimalPolynomials:
    def __init__(self, B: builtins.object) -> None: ...
    def find_monic_replacements(
        self,
        p: builtins.int,
        t: builtins.object,
        pt_generators: builtins.object,
        prev_nu: builtins.object,
    ) -> ElementConstructorInput: ...
    def current_nu(
        self,
        p: builtins.int,
        t: builtins.object,
        pt_generators: builtins.object,
        prev_nu: builtins.object,
    ) -> ElementConstructorInput: ...
    def mccoy_column(
        self, p: builtins.int, t: builtins.object, nu: builtins.object
    ) -> ElementConstructorInput: ...
    def p_minimal_polynomials(
        self, p: builtins.int, s_max: builtins.object = ...
    ) -> ElementConstructorInput: ...
    def null_ideal(self, b: builtins.int = ...) -> ElementConstructorInput: ...
    def prime_candidates(self) -> ElementConstructorInput: ...
    def integer_valued_polynomials_generators(self) -> ElementConstructorInput: ...
