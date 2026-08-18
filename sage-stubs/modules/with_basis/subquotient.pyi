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

from sage.categories.morphism import Morphism
from sage.combinat.free_module import CombinatorialFreeModule

class QuotientModuleWithBasis(CombinatorialFreeModule):
    def ambient(self) -> QuotientModuleWithBasis: ...
    def lift(
        self, x: FreeModuleElement[_Scalar] | Sequence[_Scalar]
    ) -> QuotientModuleWithBasis: ...
    def retract(
        self, x: FreeModuleElement[_Scalar] | Sequence[_Scalar]
    ) -> QuotientModuleWithBasis: ...

class SubmoduleWithBasis(CombinatorialFreeModule):
    def ambient(self) -> ElementConstructorInput: ...
    lift: Morphism
    reduce: Morphism
    retract: Morphism

    def is_submodule(self, other: ElementConstructorInput) -> bool: ...
    def cokernel_basis_indices(self) -> list[Hashable]: ...
