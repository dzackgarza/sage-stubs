from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.categories.homset import Homset
from sage.structure.element import RingElement

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

type GradedModuleElement[_AlgebraElement: RingElement] = (
    FPElement[_AlgebraElement]
    | FreeGradedModuleElement[_AlgebraElement]
)
type GradedModule[_AlgebraElement: RingElement] = (
    FPModule[_AlgebraElement]
    | FreeGradedModule[_AlgebraElement]
)

class FPModuleHomspace(
    Homset[
        FPModuleMorphism[_AlgebraElement],
        GradedModuleElement[_AlgebraElement],
        GradedModuleElement[_AlgebraElement],
    ],
    Generic[_AlgebraElement],
):
    Element: type[FPModuleMorphism[_AlgebraElement]]
    element_class: type[FPModuleMorphism[_AlgebraElement]]

    def domain(self) -> GradedModule[_AlgebraElement]: ...
    def codomain(self) -> GradedModule[_AlgebraElement]: ...
    def _element_constructor_(
        self,
        values: FPModuleMorphism[_AlgebraElement]
        | Sequence[GradedModuleElement[_AlgebraElement]]
        | int,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def an_element(
        self,
        n: GeneratorDegree = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
    ) -> list[FPModuleMorphism[_AlgebraElement]]: ...
    def zero(self) -> FPModuleMorphism[_AlgebraElement]: ...
    def identity(self) -> FPModuleMorphism[_AlgebraElement]: ...
    one = identity

from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import FreeGradedModule, GeneratorDegree
from sage.modules.fp_graded.module import FPModule
from sage.modules.fp_graded.morphism import FPModuleMorphism
