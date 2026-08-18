from sage.modules.fp_graded.free_homspace import FreeGradedModuleHomspace
from sage.modules.fp_graded.homspace import FPModuleHomspace
from sage.modules.fp_graded.steenrod.morphism import (
    SteenrodFPModuleMorphism,
    SteenrodFreeModuleMorphism,
)
from sage.structure.element import RingElement

class SteenrodFPModuleHomspace(FPModuleHomspace[RingElement]):
    Element: type[SteenrodFPModuleMorphism]

class SteenrodFreeModuleHomspace(
    SteenrodFPModuleHomspace,
    FreeGradedModuleHomspace[RingElement],
):
    Element: type[SteenrodFreeModuleMorphism]
