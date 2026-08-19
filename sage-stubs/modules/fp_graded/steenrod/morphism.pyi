from collections.abc import Callable

from sage.algebras.steenrod.steenrod_algebra import SteenrodAlgebra_generic
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.morphism import FPModuleMorphism
from sage.modules.fp_graded.steenrod.profile import SteenrodProfile
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.integer import Integer
from sage.structure.element import RingElement

type SteenrodActionMethod = Callable[
    ...,
    FPModuleMorphism[RingElement, FiniteRingElement],
]

class SteenrodFPModuleMorphism(
    FPModuleMorphism[RingElement, FiniteRingElement],
):
    def parent(self) -> SteenrodFPModuleHomspace: ...
    def domain(self) -> SteenrodFPModule | SteenrodFreeModule: ...
    def codomain(self) -> SteenrodFPModule | SteenrodFreeModule: ...
    def base_ring(self) -> SteenrodAlgebra_generic: ...
    def profile(self) -> SteenrodProfile: ...
    def change_ring(
        self,
        algebra: SteenrodAlgebra_generic,
    ) -> SteenrodFPModuleMorphism: ...
    def suspension(
        self,
        t: int | Integer,
    ) -> SteenrodFPModuleMorphism: ...
    def lift(
        self,
        f: SteenrodFPModuleMorphism,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism | None: ...
    def split(
        self,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism | None: ...
    def homology(
        self,
        f: SteenrodFPModuleMorphism,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFPModuleMorphism: ...
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
    def _resolve_kernel(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFreeModuleMorphism: ...
    def _resolve_image(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> SteenrodFreeModuleMorphism: ...
    def _action(
        self,
        method: SteenrodActionMethod,
        *args: object,
        **kwds: object,
    ) -> SteenrodFPModuleMorphism: ...
    def fp_module(self) -> SteenrodFPModule | SteenrodFreeModule: ...

class SteenrodFreeModuleMorphism(
    FreeGradedModuleMorphism[RingElement, FiniteRingElement],
    SteenrodFPModuleMorphism,
):
    def parent(self) -> SteenrodFreeModuleHomspace: ...
    def domain(self) -> SteenrodFreeModule: ...
    def codomain(self) -> SteenrodFPModule | SteenrodFreeModule: ...
    def change_ring(
        self,
        algebra: SteenrodAlgebra_generic,
    ) -> SteenrodFreeModuleMorphism: ...
    def suspension(
        self,
        t: int | Integer,
    ) -> SteenrodFreeModuleMorphism: ...
    def fp_module(self) -> SteenrodFPModule | SteenrodFreeModule: ...

from sage.modules.fp_graded.steenrod.homspace import (
    SteenrodFPModuleHomspace,
    SteenrodFreeModuleHomspace,
)
from sage.modules.fp_graded.steenrod.module import (
    SteenrodFPModule,
    SteenrodFreeModule,
)
