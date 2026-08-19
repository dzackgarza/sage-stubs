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
_GroundElement = TypeVar(
    "_GroundElement",
    bound=RingElement,
    default=RingElement,
)

class FreeGradedModuleHomspace(
    FPModuleHomspace[_AlgebraElement, _GroundElement],
    Generic[_AlgebraElement, _GroundElement],
):
    Element: type[
        FreeGradedModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ]
    ]
    element_class: type[
        FreeGradedModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ]
    ]

    def domain(
        self,
    ) -> FreeGradedModule[_AlgebraElement, _GroundElement]: ...
    def codomain(
        self,
    ) -> GradedModule[_AlgebraElement, _GroundElement]: ...
    def _element_constructor_(
        self,
        values: FreeGradedModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ]
        | Sequence[
            GradedModuleElement[
                _AlgebraElement,
                _GroundElement,
            ]
        ]
        | int,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def an_element(
        self,
        n: GeneratorDegree = ...,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
    ) -> list[
        FreeGradedModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ]
    ]: ...
    def zero(
        self,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def identity(
        self,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    one = identity

from sage.modules.fp_graded.free_module import FreeGradedModule, GeneratorDegree
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
