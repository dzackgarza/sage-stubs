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

class CellModule:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        A: builtins.object,
        mu: builtins.object,
        **kwds: builtins.object,
    ) -> CellModule: ...
    def __init__(
        self, A: builtins.object, mu: builtins.object, **kwds: builtins.object
    ) -> None: ...
    def cellular_algebra(self) -> CellModule: ...
    def bilinear_form(
        self, x: builtins.object, y: builtins.object
    ) -> Matrix[_Scalar]: ...
    def bilinear_form_matrix(
        self, ordering: builtins.object = ...
    ) -> Matrix[_Scalar]: ...
    def nonzero_bilinear_form(self) -> CellModule: ...
    def radical_basis(self) -> CellModule: ...
    def radical(self) -> CellModule: ...
    def simple_module(self) -> CellModule: ...

    class Element: ...

class SimpleModule:
    def __init__(self, submodule: builtins.object) -> None: ...

    class Element: ...
