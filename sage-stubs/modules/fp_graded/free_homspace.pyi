from typing import Generic, TypeVar

from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.homspace import FPModuleHomspace
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
