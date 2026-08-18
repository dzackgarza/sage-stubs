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

class Matrix_gap:
    def __init__(
        self,
        parent: builtins.object,
        entries: builtins.object = ...,
        copy: builtins.object = ...,
        coerce: builtins.object = ...,
    ) -> None: ...
    def __copy__(self) -> Self: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...
    def gap(self) -> Matrix_gap: ...
    def get_unsafe(self, i: builtins.object, j: builtins.object) -> Matrix_gap: ...
    def set_unsafe(
        self, i: builtins.object, j: builtins.object, x: builtins.object
    ) -> Matrix_gap: ...
    def copy_from_unsafe(
        self,
        iDst: builtins.object,
        jDst: builtins.object,
        src: builtins.object,
        iSrc: builtins.object,
        jSrc: builtins.object,
    ) -> Matrix_gap: ...
    def __neg__(self) -> Self: ...
    def __invert__(self) -> Self: ...
    def transpose(self) -> Self: ...
    def determinant(self) -> _Scalar: ...
    def trace(self) -> _Scalar: ...
    def rank(self) -> Integer: ...
    def minpoly(
        self, var: builtins.object = ..., **kwds: builtins.object
    ) -> Polynomial: ...
    def elementary_divisors(self) -> Matrix_gap: ...
