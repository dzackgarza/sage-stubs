from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.categories.homset import Homset
from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.structure.element import RingElement

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)

type GradedModuleElement[_AlgebraElement: RingElement] = (
    FPElement[int, _AlgebraElement]
    | FreeGradedModuleElement[int, _AlgebraElement]
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

    def _element_constructor_(
        self,
        values: FPModuleMorphism[_AlgebraElement]
        | Sequence[GradedModuleElement[_AlgebraElement]]
        | int,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def an_element(self, n: int = ...) -> FPModuleMorphism[_AlgebraElement]: ...
    def basis_elements(
        self,
        n: int,
    ) -> list[FPModuleMorphism[_AlgebraElement]]: ...
    def zero(self) -> FPModuleMorphism[_AlgebraElement]: ...
    def identity(self) -> FPModuleMorphism[_AlgebraElement]: ...

from sage.modules.fp_graded.morphism import FPModuleMorphism
