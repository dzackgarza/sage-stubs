from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.modules.fp_graded.homspace import (
    FPModuleHomspace,
    GradedModule,
    GradedModuleElement,
)
from sage.structure.element import RingElement

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

class FreeGradedModuleHomspace(
    FPModuleHomspace[_AlgebraElement],
    Generic[_AlgebraElement],
):
    Element: type[FreeGradedModuleMorphism[_AlgebraElement]]
    element_class: type[FreeGradedModuleMorphism[_AlgebraElement]]

    def domain(self) -> FreeGradedModule[_AlgebraElement]: ...
    def codomain(self) -> GradedModule[_AlgebraElement]: ...
    def _element_constructor_(
        self,
        values: FreeGradedModuleMorphism[_AlgebraElement]
        | Sequence[GradedModuleElement[_AlgebraElement]]
        | int,
    ) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def an_element(
        self,
        n: GeneratorDegree = ...,
    ) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
    ) -> list[FreeGradedModuleMorphism[_AlgebraElement]]: ...
    def zero(self) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def identity(self) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    one = identity

from sage.modules.fp_graded.free_module import FreeGradedModule, GeneratorDegree
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
