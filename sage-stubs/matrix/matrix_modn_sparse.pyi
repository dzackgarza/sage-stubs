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

ai: _SageObject
MAX_MODULUS: _SageObject

class Matrix_modn_sparse:
    def __cinit__(self) -> Matrix_modn_sparse: ...
    def __dealloc__(self) -> Matrix_modn_sparse: ...
    def __init__(
        self,
        parent: builtins.object,
        entries: builtins.object = ...,
        copy: builtins.object = ...,
        coerce: builtins.object = ...,
    ) -> None: ...
    def set_unsafe(
        self, i: builtins.object, j: builtins.object, value: builtins.object
    ) -> Matrix_modn_sparse: ...
    def get_unsafe(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_modn_sparse: ...
    def copy_from_unsafe(
        self,
        iDst: builtins.object,
        jDst: builtins.object,
        src: builtins.object,
        iSrc: builtins.object,
        jSrc: builtins.object,
    ) -> Matrix_modn_sparse: ...
    def get_is_zero_unsafe(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_modn_sparse: ...
    def swap_rows(
        self, r1: builtins.object, r2: builtins.object
    ) -> Matrix_modn_sparse: ...
    def swap_rows_c(
        self, n1: builtins.object, n2: builtins.object
    ) -> Matrix_modn_sparse: ...
    def density(self) -> Matrix_modn_sparse: ...
    def transpose(self) -> Self: ...
    def matrix_from_rows(
        self, rows: builtins.object
    ) -> Matrix[IntegerMod_abstract]: ...
    def matrix_from_columns(
        self, cols: builtins.object
    ) -> Matrix[IntegerMod_abstract]: ...
    def rank(self, algorithm: builtins.object = ...) -> Integer: ...
    def determinant(self, algorithm: builtins.object = ...) -> IntegerMod_abstract: ...
