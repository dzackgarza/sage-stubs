from collections.abc import Sequence

from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_homspace import FreeGradedModuleHomspace
from sage.modules.fp_graded.homspace import FPModuleHomspace
from sage.modules.fp_graded.steenrod.module import (
    SteenrodFPModule,
    SteenrodFreeModule,
)
from sage.modules.fp_graded.steenrod.morphism import (
    SteenrodFPModuleMorphism,
    SteenrodFreeModuleMorphism,
)
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

type SteenrodModule = SteenrodFPModule | SteenrodFreeModule
type SteenrodModuleElement = (
    FPElement[RingElement, FiniteRingElement]
    | FreeGradedModuleElement[RingElement, FiniteRingElement]
)

class SteenrodFPModuleHomspace(
    FPModuleHomspace[RingElement, FiniteRingElement],
):
    Element: type[SteenrodFPModuleMorphism]
    element_class: type[SteenrodFPModuleMorphism]

    def domain(self) -> SteenrodModule: ...
    def codomain(self) -> SteenrodModule: ...
    def _element_constructor_(
        self,
        values: SteenrodFPModuleMorphism
        | Sequence[SteenrodModuleElement]
        | int,
    ) -> SteenrodFPModuleMorphism: ...
    def an_element(
        self,
        n: int | Integer = ...,
    ) -> SteenrodFPModuleMorphism: ...
    def basis_elements(
        self,
        n: int | Integer,
    ) -> list[SteenrodFPModuleMorphism]: ...
    def zero(self) -> SteenrodFPModuleMorphism: ...
    def identity(self) -> SteenrodFPModuleMorphism: ...
    one = identity

class SteenrodFreeModuleHomspace(
    SteenrodFPModuleHomspace,
    FreeGradedModuleHomspace[RingElement, FiniteRingElement],
):
    Element: type[SteenrodFreeModuleMorphism]
    element_class: type[SteenrodFreeModuleMorphism]

    def domain(self) -> SteenrodFreeModule: ...
    def codomain(self) -> SteenrodModule: ...
    def _element_constructor_(
        self,
        values: SteenrodFreeModuleMorphism
        | Sequence[SteenrodModuleElement]
        | int,
    ) -> SteenrodFreeModuleMorphism: ...
    def an_element(
        self,
        n: int | Integer = ...,
    ) -> SteenrodFreeModuleMorphism: ...
    def basis_elements(
        self,
        n: int | Integer,
    ) -> list[SteenrodFreeModuleMorphism]: ...
    def zero(self) -> SteenrodFreeModuleMorphism: ...
    def identity(self) -> SteenrodFreeModuleMorphism: ...
    one = identity
