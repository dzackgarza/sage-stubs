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

class FiniteDimensionalInvariantModule:
    def __init__(
        self,
        M: builtins.int,
        S: builtins.object,
        action: builtins.object = ...,
        side: builtins.str = ...,
        *args: builtins.object,
        **kwargs: builtins.object,
    ) -> None: ...
    def construction(self) -> FiniteDimensionalInvariantModule: ...
    def semigroup(self) -> FiniteDimensionalInvariantModule: ...
    semigroup_representation: _SageObject

    class Element: ...

class FiniteDimensionalTwistedInvariantModule:
    @staticmethod
    def __classcall_private__(
        cls: builtins.object,
        M: builtins.int,
        G: builtins.object,
        chi: builtins.object,
        action: builtins.object = ...,
        side: builtins.str = ...,
        **kwargs: builtins.object,
    ) -> FiniteDimensionalInvariantModule: ...
    def __init__(
        self,
        M: builtins.int,
        G: builtins.object,
        chi: builtins.object,
        action: builtins.object = ...,
        side: builtins.str = ...,
        **kwargs: builtins.object,
    ) -> None: ...
    def project(self, x: builtins.object) -> FiniteDimensionalInvariantModule: ...
    def project_ambient(
        self, x: builtins.object
    ) -> FiniteDimensionalInvariantModule: ...
    def projection_matrix(self) -> Matrix[_Scalar]: ...

    class Element: ...
