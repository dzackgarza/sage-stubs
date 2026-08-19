from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.homspace import (
    GradedModule,
    GradedModuleElement,
)
from sage.modules.fp_graded.morphism import FPModuleMorphism
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

class FreeGradedModuleMorphism(
    FPModuleMorphism[_AlgebraElement],
    Generic[_AlgebraElement],
):
    def __init__(
        self,
        parent: FreeGradedModuleHomspace[_AlgebraElement],
        values: Sequence[GradedModuleElement[_AlgebraElement]],
    ) -> None: ...
    def parent(self) -> FreeGradedModuleHomspace[_AlgebraElement]: ...
    def domain(self) -> FreeGradedModule[_AlgebraElement]: ...
    def codomain(self) -> GradedModule[_AlgebraElement]: ...
    def degree(self) -> int | Integer: ...
    def __call__(
        self,
        x: FreeGradedModuleElement[_AlgebraElement],
    ) -> GradedModuleElement[_AlgebraElement]: ...
    def fp_module(
        self,
    ) -> FPModule[_AlgebraElement] | FreeGradedModule[_AlgebraElement]: ...

from sage.modules.fp_graded.free_homspace import FreeGradedModuleHomspace
from sage.modules.fp_graded.free_module import FreeGradedModule
from sage.modules.fp_graded.module import FPModule
