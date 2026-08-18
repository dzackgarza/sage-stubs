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

class FieldConverter_class:
    def __init__(self, field: builtins.object) -> None: ...
    def fel_to_field(self, x: builtins.object) -> ElementConstructorInput: ...
    def field_to_fel(self, x: builtins.object) -> ElementConstructorInput: ...

class PrimeFieldConverter_class:
    def __init__(self, field: builtins.object) -> None: ...
    def fel_to_field(self, x: builtins.object) -> ElementConstructorInput: ...
    def field_to_fel(self, x: builtins.object) -> ElementConstructorInput: ...

def FieldConverter(field: builtins.object) -> ElementConstructorInput: ...
def new_mtx(
    mat: builtins.object, template: builtins.object
) -> ElementConstructorInput: ...

class Matrix_gfpn_dense:
    def __dealloc__(self) -> Matrix_gfpn_dense: ...
    def __init__(
        self,
        parent: builtins.object,
        entries: builtins.object = ...,
        copy: builtins.object = ...,
        coerce: builtins.object = ...,
        mutable: builtins.object = ...,
    ) -> None: ...
    @staticmethod
    def from_filename(filename: builtins.object) -> Matrix_gfpn_dense: ...
    def __copy__(self) -> Self: ...
    def __reduce__(self) -> builtins.str | builtins.tuple[builtins.object, ...]: ...
    def get_unsafe(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def get_unsafe_int(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def get_is_zero_unsafe(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def get_slice(
        self, i: builtins.object, j: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def set_unsafe(
        self, i: builtins.object, j: builtins.object, value: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def set_unsafe_int(
        self, i: builtins.object, j: builtins.object, value: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def set_slice_unsafe(
        self, i: builtins.object, S: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def copy_from_unsafe(
        self,
        iDst: builtins.object,
        jDst: builtins.object,
        src: builtins.object,
        iSrc: builtins.object,
        jSrc: builtins.object,
    ) -> Matrix_gfpn_dense: ...
    def randomize(
        self,
        density: builtins.object = ...,
        nonzero: builtins.object = ...,
        *args: builtins.object,
        **kwds: builtins.object,
    ) -> Matrix_gfpn_dense: ...
    def rescale_row_c(
        self, i: builtins.object, s: builtins.object, start_col: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def add_multiple_of_row_c(
        self,
        row_to: builtins.object,
        row_from: builtins.object,
        multiple: builtins.object,
        start_col: builtins.object,
    ) -> Matrix_gfpn_dense: ...
    def swap_rows_c(
        self, row1: builtins.object, row2: builtins.object
    ) -> Matrix_gfpn_dense: ...
    def trace(self) -> _Scalar: ...
    def __neg__(self) -> Self: ...
    def __truediv__(self, p: builtins.object) -> Self: ...
    def __invert__(self) -> Self: ...
    def transpose(self) -> Self: ...
    def order(self) -> Matrix_gfpn_dense: ...
    def left_kernel_matrix(self) -> Matrix[_Scalar]: ...

def mtx_unpickle(
    f: builtins.object,
    nr: builtins.object,
    nc: builtins.object,
    data: builtins.object,
    m: builtins.object,
) -> ElementConstructorInput: ...
