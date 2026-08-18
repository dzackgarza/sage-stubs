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
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class

class FGP_Morphism(Morphism[FGP_Element, FGP_Element], Generic[_Scalar]):
    def __init__(
        self,
        parent: ElementConstructorInput,
        phi: ElementConstructorInput,
        check: bool = ...,
    ) -> None: ...
    def im_gens(self) -> tuple[FGP_Element, ...]: ...
    def image(self) -> FGP_Module_class[_Scalar]: ...
    def kernel(self) -> FGP_Module_class[_Scalar]: ...
    def inverse_image(
        self, submodule: FGP_Module_class[_Scalar]
    ) -> FGP_Module_class[_Scalar]: ...
    def lift(self, x: FGP_Element) -> FGP_Element: ...
    def __call__(self, x: FGP_Element) -> FGP_Element: ...
    def __richcmp__(self, other: FGP_Morphism, op: int) -> bool: ...
    def _repr_(self) -> str: ...

class FGP_Homset_class:
    def __init__(
        self,
        X: FGP_Module_class,
        Y: FGP_Module_class,
        category: ElementConstructorInput = ...,
    ) -> None: ...
    def __call__(
        self, x: FreeModuleElement[_Scalar] | Sequence[_Scalar], check: bool = ...
    ) -> FGP_Morphism: ...
