from collections.abc import Iterable

from sage.algebras.steenrod.steenrod_algebra import SteenrodAlgebra_generic
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import (
    FreeGradedModule,
    GeneratorDegree,
    GeneratorNames,
)
from sage.modules.fp_graded.module import FPModule, FPRelations
from sage.modules.fp_graded.steenrod.profile import SteenrodProfile
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

type SteenrodModuleElement = (
    FPElement[RingElement, FiniteRingElement]
    | FreeGradedModuleElement[RingElement, FiniteRingElement]
)

class SteenrodModuleMixin:
    def profile(self) -> SteenrodProfile: ...
    def export_module_definition(
        self,
        powers_of_two_only: bool = ...,
    ) -> str: ...

class SteenrodFPModule(
    FPModule[RingElement, FiniteRingElement],
    SteenrodModuleMixin,
):
    @staticmethod
    def __classcall__(
        class_: type[SteenrodFPModule],
        arg0: SteenrodAlgebra_generic
        | SteenrodFreeModule
        | Morphism,
        generator_degrees: Iterable[GeneratorDegree] | None = ...,
        relations: FPRelations = ...,
        names: GeneratorNames = ...,
    ) -> SteenrodFPModule | SteenrodFreeModule: ...
    def base_ring(self) -> SteenrodAlgebra_generic: ...
    def change_ring(
        self,
        algebra: SteenrodAlgebra_generic,
    ) -> SteenrodFPModule: ...
    def _Hom_(
        self,
        other: SteenrodFPModule | SteenrodFreeModule,
        category: Category | None = ...,
    ) -> SteenrodFPModuleHomspace: ...
    def minimal_presentation(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism: ...
    def suspension(
        self,
        t: int | Integer,
    ) -> SteenrodFPModule: ...
    def submodule_inclusion(
        self,
        spanning_elements: Iterable[SteenrodModuleElement],
    ) -> SteenrodFPModuleMorphism: ...
    def resolution(
        self,
        k: int,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> list[SteenrodFreeModuleMorphism]: ...

class SteenrodFreeModule(
    FreeGradedModule[RingElement, FiniteRingElement],
    SteenrodModuleMixin,
):
    def base_ring(self) -> SteenrodAlgebra_generic: ...
    def change_ring(
        self,
        algebra: SteenrodAlgebra_generic,
    ) -> SteenrodFreeModule: ...
    def _Hom_(
        self,
        Y: SteenrodFPModule | SteenrodFreeModule,
        category: Category | None,
    ) -> SteenrodFreeModuleHomspace: ...
    def suspension(
        self,
        t: int | Integer,
    ) -> SteenrodFreeModule: ...
    def resolution(
        self,
        k: int,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> list[SteenrodFreeModuleMorphism]: ...
    def minimal_presentation(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFreeModuleMorphism: ...

from sage.modules.fp_graded.steenrod.homspace import (
    SteenrodFPModuleHomspace,
    SteenrodFreeModuleHomspace,
)
from sage.modules.fp_graded.steenrod.morphism import (
    SteenrodFPModuleMorphism,
    SteenrodFreeModuleMorphism,
)
