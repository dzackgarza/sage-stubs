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

class M4RIE_finite_field:
    def __dealloc__(self) -> ElementConstructorInput: ...

def poly_to_word(f: builtins.object) -> ElementConstructorInput: ...

class Matrix_gf2e_dense:
    def __cinit__(
        self,
        *args: builtins.object,
        alloc: builtins.object = ...,
        **kwds: builtins.object,
    ) -> Matrix_gf2e_dense: ...
    def __dealloc__(self) -> Matrix_gf2e_dense: ...
    def __init__(
        self,
        parent: builtins.object,
        entries: builtins.object = ...,
        copy: builtins.object = ...,
        coerce: builtins.object = ...,
    ) -> None: ...
    def set_unsafe(
        self, i: builtins.object, j: builtins.object, value: builtins.object
    ) -> Matrix_gf2e_dense: ...
    def get_unsafe(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_gf2e_dense: ...
    def copy_from_unsafe(
        self,
        iDst: builtins.object,
        jDst: builtins.object,
        src: builtins.object,
        iSrc: builtins.object,
        jSrc: builtins.object,
    ) -> Matrix_gf2e_dense: ...
    def get_is_zero_unsafe(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_gf2e_dense: ...
    def __neg__(self) -> Self: ...
    def __copy__(self) -> Self: ...
    def __bool__(self) -> builtins.bool: ...
    def randomize(
        self,
        density: builtins.object = ...,
        nonzero: builtins.object = ...,
        *args: builtins.object,
        **kwds: builtins.object,
    ) -> Matrix_gf2e_dense: ...
    def echelonize(
        self,
        algorithm: builtins.object = ...,
        reduced: builtins.object = ...,
        **kwds: builtins.object,
    ) -> Matrix_gf2e_dense: ...
    def is_invertible(self) -> builtins.bool: ...
    def __invert__(self) -> Self: ...
    def rescale_row_c(
        self,
        row: builtins.object,
        multiple: builtins.object,
        start_col: builtins.object,
    ) -> Matrix_gf2e_dense: ...
    def add_multiple_of_row_c(
        self,
        row_to: builtins.object,
        row_from: builtins.object,
        multiple: builtins.object,
        start_col: builtins.object,
    ) -> Matrix_gf2e_dense: ...
    def swap_rows_c(
        self, row1: builtins.object, row2: builtins.object
    ) -> Matrix_gf2e_dense: ...
    def swap_columns_c(
        self, col1: builtins.object, col2: builtins.object
    ) -> Matrix_gf2e_dense: ...
    def augment(self, right: builtins.object) -> Matrix_gf2e_dense: ...
    def rank(self) -> Integer: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...
    def slice(self) -> Matrix_gf2e_dense: ...
    def cling(self, *C: builtins.object) -> Matrix_gf2e_dense: ...
    def determinant(self) -> _Scalar: ...

def unpickle_matrix_gf2e_dense_v0(
    a: builtins.object,
    base_ring: builtins.object,
    nrows: builtins.object,
    ncols: builtins.object,
) -> Matrix[_Scalar]: ...
