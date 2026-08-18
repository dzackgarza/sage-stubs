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

from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement

class ModuleMorphism:
    def __init__(
        self,
        domain: FreeModule_generic,
        codomain: FreeModule_generic = ...,
        category: ElementConstructorInput = ...,
        affine: bool = ...,
    ) -> None: ...
    def __call__(self, x: IndexedFreeModuleElement) -> IndexedFreeModuleElement: ...

class ModuleMorphismFromFunction(ModuleMorphism):
    def __init__(
        self,
        domain: FreeModule_generic,
        codomain: FreeModule_generic,
        function: ElementConstructorInput,
        category: ElementConstructorInput = ...,
    ) -> None: ...

class ModuleMorphismByLinearity(ModuleMorphism):
    def __init__(
        self,
        domain: FreeModule_generic,
        codomain: FreeModule_generic = ...,
        on_basis: ElementConstructorInput = ...,
        category: ElementConstructorInput = ...,
    ) -> None: ...

class TriangularModuleMorphism(ModuleMorphism):
    def __init__(
        self,
        domain: FreeModule_generic,
        codomain: FreeModule_generic = ...,
        on_basis: ElementConstructorInput = ...,
        category: ElementConstructorInput = ...,
        unitriangular: str = ...,
    ) -> None: ...

class TriangularModuleMorphismByLinearity(
    ModuleMorphismByLinearity, TriangularModuleMorphism
): ...
