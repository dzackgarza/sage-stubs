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
_GroundElement = TypeVar(
    "_GroundElement",
    bound=RingElement,
    default=RingElement,
)

class FreeGradedModuleMorphism(
    FPModuleMorphism[_AlgebraElement, _GroundElement],
    Generic[_AlgebraElement, _GroundElement],
):
    def __init__(
        self,
        parent: FreeGradedModuleHomspace[
            _AlgebraElement,
            _GroundElement,
        ],
        values: Sequence[
            GradedModuleElement[
                _AlgebraElement,
                _GroundElement,
            ]
        ],
    ) -> None: ...
    def parent(
        self,
    ) -> FreeGradedModuleHomspace[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def domain(
        self,
    ) -> FreeGradedModule[_AlgebraElement, _GroundElement]: ...
    def codomain(
        self,
    ) -> GradedModule[_AlgebraElement, _GroundElement]: ...
    def degree(self) -> int | Integer: ...
    def __call__(
        self,
        x: FreeGradedModuleElement[
            _AlgebraElement,
            _GroundElement,
        ],
    ) -> GradedModuleElement[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def fp_module(
        self,
    ) -> (
        FPModule[_AlgebraElement, _GroundElement]
        | FreeGradedModule[_AlgebraElement, _GroundElement]
    ): ...

from sage.modules.fp_graded.free_homspace import FreeGradedModuleHomspace
from sage.modules.fp_graded.free_module import FreeGradedModule
from sage.modules.fp_graded.module import FPModule
