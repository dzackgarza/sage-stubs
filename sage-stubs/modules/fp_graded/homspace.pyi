from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.categories.homset import Homset
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

type GradedModuleElement[
    _AlgebraElement: RingElement,
    _GroundElement: RingElement,
] = (
    FPElement[_AlgebraElement, _GroundElement]
    | FreeGradedModuleElement[_AlgebraElement, _GroundElement]
)
type GradedModule[
    _AlgebraElement: RingElement,
    _GroundElement: RingElement,
] = (
    FPModule[_AlgebraElement, _GroundElement]
    | FreeGradedModule[_AlgebraElement, _GroundElement]
)

class FPModuleHomspace(
    Homset[
        FPModuleMorphism[_AlgebraElement, _GroundElement],
        GradedModuleElement[_AlgebraElement, _GroundElement],
        GradedModuleElement[_AlgebraElement, _GroundElement],
    ],
    Generic[_AlgebraElement, _GroundElement],
):
    Element: type[
        FPModuleMorphism[_AlgebraElement, _GroundElement]
    ]
    element_class: type[
        FPModuleMorphism[_AlgebraElement, _GroundElement]
    ]

    def domain(
        self,
    ) -> GradedModule[_AlgebraElement, _GroundElement]: ...
    def codomain(
        self,
    ) -> GradedModule[_AlgebraElement, _GroundElement]: ...
    def _element_constructor_(
        self,
        values: FPModuleMorphism[
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
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def an_element(
        self,
        n: GeneratorDegree = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
    ) -> list[
        FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ]
    ]: ...
    def zero(
        self,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def identity(
        self,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    one = identity

from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import FreeGradedModule, GeneratorDegree
from sage.modules.fp_graded.module import FPModule
from sage.modules.fp_graded.morphism import FPModuleMorphism
