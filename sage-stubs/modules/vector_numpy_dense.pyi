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

class Vector_numpy_dense:
    def __cinit__(
        self,
        parent: builtins.object,
        entries: builtins.object,
        coerce: builtins.object = ...,
        copy: builtins.object = ...,
    ) -> Vector_numpy_dense: ...
    def __create_vector__(self) -> Vector_numpy_dense: ...
    def is_dense_c(self) -> builtins.bool: ...
    def is_sparse_c(self) -> builtins.bool: ...
    def __copy__(self, copy: builtins.object = ...) -> Self: ...
    def __init__(
        self,
        parent: builtins.object,
        entries: builtins.object,
        coerce: builtins.object = ...,
        copy: builtins.object = ...,
    ) -> None: ...
    def __len__(self) -> builtins.int: ...
    def set_unsafe(
        self, i: builtins.object, value: builtins.object
    ) -> Vector_numpy_dense: ...
    def get_unsafe(self, i: builtins.object) -> Vector_numpy_dense: ...
    def numpy(self, dtype: builtins.object = ...) -> Vector_numpy_dense: ...
