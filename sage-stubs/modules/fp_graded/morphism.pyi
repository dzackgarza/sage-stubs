from collections.abc import Callable, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.morphism import Morphism
from sage.matrix.matrix0 import Matrix
from sage.modules.fg_pid.fgp_morphism import FGP_Morphism
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.parent import Parent

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
_NewAlgebraElement = TypeVar("_NewAlgebraElement", bound=RingElement)

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
type FPModuleMorphismValues[
    _AlgebraElement: RingElement,
    _GroundElement: RingElement,
] = (
    Sequence[
        GradedModuleElement[
            _AlgebraElement,
            _GroundElement,
        ]
    ]
    | Callable[
        [
            GradedModuleElement[
                _AlgebraElement,
                _GroundElement,
            ]
        ],
        GradedModuleElement[
            _AlgebraElement,
            _GroundElement,
        ],
    ]
    | int
)
type GradedPieceMorphism[_GroundElement: RingElement] = (
    FreeModuleMorphism[_GroundElement, _GroundElement]
    | FGP_Morphism[_GroundElement]
)

def _create_relations_matrix(
    module: GradedModule[_AlgebraElement, _GroundElement],
    relations: Sequence[Sequence[_AlgebraElement]],
    source_degs: Sequence[int | Integer],
    target_degs: Sequence[int | Integer],
) -> tuple[
    list[list[GradedPieceMorphism[_GroundElement]]],
    Matrix[_GroundElement],
]: ...

class FPModuleMorphism(
    Morphism[
        GradedModuleElement[_AlgebraElement, _GroundElement],
        GradedModuleElement[_AlgebraElement, _GroundElement],
    ],
    Generic[_AlgebraElement, _GroundElement],
):
    def __init__(
        self,
        parent: FPModuleHomspace[
            _AlgebraElement,
            _GroundElement,
        ],
        values: FPModuleMorphismValues[
            _AlgebraElement,
            _GroundElement,
        ],
        check: bool = ...,
    ) -> None: ...
    def parent(
        self,
    ) -> FPModuleHomspace[_AlgebraElement, _GroundElement]: ...
    def domain(
        self,
    ) -> GradedModule[_AlgebraElement, _GroundElement]: ...
    def codomain(
        self,
    ) -> GradedModule[_AlgebraElement, _GroundElement]: ...
    def base_ring(self) -> Parent[_AlgebraElement]: ...
    @property
    def _free_morphism(
        self,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def change_ring(
        self,
        algebra: Parent[_NewAlgebraElement],
    ) -> FPModuleMorphism[_NewAlgebraElement, RingElement]: ...
    def degree(self) -> int | Integer: ...
    def values(
        self,
    ) -> tuple[
        GradedModuleElement[_AlgebraElement, _GroundElement],
        ...,
    ]: ...
    def _richcmp_(
        self,
        other: FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
        op: int,
    ) -> bool: ...
    def __add__(
        self,
        g: FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
    ) -> Self: ...
    def __neg__(self) -> Self: ...
    def __sub__(
        self,
        g: FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
    ) -> Self: ...
    def __mul__(
        self,
        g: FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def is_zero(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def is_identity(self) -> bool: ...
    def __call__(
        self,
        x: GradedModuleElement[
            _AlgebraElement,
            _GroundElement,
        ],
    ) -> GradedModuleElement[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def _repr_type(self) -> str: ...
    def _repr_defn(self) -> str: ...
    def vector_presentation(
        self,
        n: int | Integer,
    ) -> GradedPieceMorphism[_GroundElement]: ...
    def solve(
        self,
        x: GradedModuleElement[
            _AlgebraElement,
            _GroundElement,
        ],
    ) -> GradedModuleElement[
        _AlgebraElement,
        _GroundElement,
    ] | None: ...
    def lift(
        self,
        f: FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
        verbose: bool = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ] | None: ...
    def split(
        self,
        verbose: bool = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ] | None: ...
    def homology(
        self,
        f: FPModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def suspension(
        self,
        t: int | Integer,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def cokernel_projection(
        self,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def kernel_inclusion(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def image(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def is_injective(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> bool: ...
    def is_surjective(self) -> bool: ...
    def _resolve_kernel(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def _resolve_image(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def fp_module(
        self,
    ) -> (
        FPModule[_AlgebraElement, _GroundElement]
        | FreeGradedModule[_AlgebraElement, _GroundElement]
    ): ...

from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import FreeGradedModule
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.homspace import FPModuleHomspace
from sage.modules.fp_graded.module import FPModule
