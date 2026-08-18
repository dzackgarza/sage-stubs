from sage.categories.category import Category
from sage.modules.fp_graded.free_module import FreeGradedModule
from sage.modules.fp_graded.module import FPModule
from sage.modules.fp_graded.steenrod.profile import SteenrodProfile
from sage.rings.integer import Integer
from sage.structure.element import RingElement

class SteenrodModuleMixin:
    def profile(self) -> SteenrodProfile: ...
    def export_module_definition(
        self,
        powers_of_two_only: bool = ...,
    ) -> str: ...

class SteenrodFPModule(FPModule[RingElement], SteenrodModuleMixin):
    def _Hom_(
        self,
        other: SteenrodFPModule | SteenrodFreeModule,
        category: Category | None = ...,
    ) -> SteenrodFPModuleHomspace: ...
    def resolution(
        self,
        k: int,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> list[SteenrodFPModuleMorphism]: ...

class SteenrodFreeModule(
    FreeGradedModule[RingElement],
    SteenrodModuleMixin,
):
    def _Hom_(
        self,
        Y: SteenrodFPModule | SteenrodFreeModule,
        category: Category | None,
    ) -> SteenrodFreeModuleHomspace: ...

from sage.modules.fp_graded.steenrod.homspace import (
    SteenrodFPModuleHomspace,
    SteenrodFreeModuleHomspace,
)
from sage.modules.fp_graded.steenrod.morphism import SteenrodFPModuleMorphism
