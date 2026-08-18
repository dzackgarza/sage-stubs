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

class FreeGradedModule:
    def __classcall__(
        cls: builtins.object,
        algebra: builtins.object,
        generator_degrees: builtins.object,
        category: builtins.object = ...,
        names: builtins.object = ...,
        prefix: builtins.str = ...,
        **kwds: builtins.object,
    ) -> FreeGradedModule: ...
    def __init__(
        self,
        algebra: builtins.object,
        generator_degrees: builtins.object,
        category: builtins.object,
        names: builtins.object = ...,
        **kwds: builtins.object,
    ) -> None: ...
    Element: _SageObject

    def change_ring(self, algebra: builtins.object) -> FreeGradedModule: ...
    def generator_degrees(self) -> FreeGradedModule: ...
    def is_trivial(self) -> builtins.bool: ...
    def connectivity(self) -> FreeGradedModule: ...
    def an_element(self, n: builtins.int = ...) -> FreeModuleElement[_Scalar]: ...
    def basis_elements(self, n: builtins.int) -> FreeGradedModule: ...
    def element_from_coordinates(
        self, coordinates: builtins.object, n: builtins.int
    ) -> FreeGradedModule: ...
    def vector_presentation(self, n: builtins.int) -> FreeGradedModule: ...
    def generator(self, index: builtins.object) -> FreeGradedModule: ...
    gen: _SageObject

    def generators(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def suspension(self, t: builtins.object) -> FreeGradedModule: ...
    def has_relations(self) -> builtins.bool: ...
    def relations(self) -> FreeGradedModule: ...
    def resolution(
        self,
        k: builtins.int,
        top_dim: builtins.object = ...,
        verbose: builtins.bool = ...,
    ) -> FreeGradedModule: ...
    def minimal_presentation(
        self, top_dim: builtins.object = ..., verbose: builtins.bool = ...
    ) -> FreeGradedModule: ...
