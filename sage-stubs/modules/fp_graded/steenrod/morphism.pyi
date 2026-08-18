from typing import Generic

from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.morphism import FPModuleMorphism
from sage.modules.fp_graded.steenrod.profile import SteenrodProfile
from sage.rings.integer import Integer
from sage.structure.element import RingElement

class SteenrodFPModuleMorphism(FPModuleMorphism[RingElement]):
    def profile(self) -> SteenrodProfile: ...
    def is_injective(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> bool: ...
    def kernel_inclusion(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism: ...
    def cokernel_projection(
        self,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism: ...
    def image(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism: ...

class SteenrodFreeModuleMorphism(
    SteenrodFPModuleMorphism,
    FreeGradedModuleMorphism[RingElement],
): ...
