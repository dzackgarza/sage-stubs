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

class OperationTable:
    def __init__(
        self,
        S: builtins.object,
        operation: builtins.object,
        names: builtins.str = ...,
        elements: builtins.object = ...,
        closed: builtins.bool = ...,
    ) -> None: ...
    def __getitem__(
        self, pair: builtins.object
    ) -> FreeModuleElement[_Scalar] | _Scalar: ...
    def __eq__(self, other: builtins.object) -> builtins.bool: ...
    def __ne__(self, other: builtins.object) -> builtins.bool: ...
    def set_print_symbols(
        self, ascii: builtins.object, latex: builtins.object
    ) -> ElementConstructorInput: ...
    def column_keys(self) -> ElementConstructorInput: ...
    row_keys: _SageObject

    def translation(self) -> ElementConstructorInput: ...
    def table(self) -> ElementConstructorInput: ...
    def change_names(self, names: builtins.object) -> ElementConstructorInput: ...
    def matrix_of_variables(self) -> Matrix[_Scalar]: ...
    def color_table(
        self,
        element_names: builtins.bool = ...,
        cmap: builtins.object = ...,
        **options: builtins.object,
    ) -> ElementConstructorInput: ...
    def gray_table(self, **options: builtins.object) -> ElementConstructorInput: ...
