from collections.abc import Callable, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.morphism import Morphism
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
_NewAlgebraElement = TypeVar("_NewAlgebraElement", bound=RingElement)

type GradedModuleElement[_AlgebraElement: RingElement] = (
    FPElement[_AlgebraElement]
    | FreeGradedModuleElement[_AlgebraElement]
)
type GradedModule[_AlgebraElement: RingElement] = (
    FPModule[_AlgebraElement]
    | FreeGradedModule[_AlgebraElement]
)
type FPModuleMorphismValues[_AlgebraElement: RingElement] = (
    Sequence[GradedModuleElement[_AlgebraElement]]
    | Callable[
        [GradedModuleElement[_AlgebraElement]],
        GradedModuleElement[_AlgebraElement],
    ]
    | int
)
type GradedPieceMorphism = (
    FreeModuleMorphism[RingElement, RingElement]
    | FGP_Morphism[RingElement]
)

class FPModuleMorphism(
    Morphism[
        GradedModuleElement[_AlgebraElement],
        GradedModuleElement[_AlgebraElement],
    ],
    Generic[_AlgebraElement],
):
    def __init__(
        self,
        parent: FPModuleHomspace[_AlgebraElement],
        values: FPModuleMorphismValues[_AlgebraElement],
        check: bool = ...,
    ) -> None: ...
    def parent(self) -> FPModuleHomspace[_AlgebraElement]: ...
    def domain(self) -> GradedModule[_AlgebraElement]: ...
    def codomain(self) -> GradedModule[_AlgebraElement]: ...
    @property
    def _free_morphism(
        self,
    ) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def change_ring(
        self,
        algebra: Parent[_NewAlgebraElement],
    ) -> FPModuleMorphism[_NewAlgebraElement]: ...
    def degree(self) -> int | Integer: ...
    def values(self) -> tuple[GradedModuleElement[_AlgebraElement], ...]: ...
    def _richcmp_(
        self,
        other: FPModuleMorphism[_AlgebraElement],
        op: int,
    ) -> bool: ...
    def __add__(self, g: FPModuleMorphism[_AlgebraElement]) -> Self: ...
    def __neg__(self) -> Self: ...
    def __sub__(self, g: FPModuleMorphism[_AlgebraElement]) -> Self: ...
    def __mul__(
        self,
        g: FPModuleMorphism[_AlgebraElement],
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def is_zero(self) -> bool: ...
    def __bool__(self) -> bool: ...
    def is_identity(self) -> bool: ...
    def __call__(
        self,
        x: GradedModuleElement[_AlgebraElement],
    ) -> GradedModuleElement[_AlgebraElement]: ...
    def _repr_type(self) -> str: ...
    def _repr_defn(self) -> str: ...
    def vector_presentation(
        self,
        n: int | Integer,
    ) -> GradedPieceMorphism: ...
    def solve(
        self,
        x: GradedModuleElement[_AlgebraElement],
    ) -> GradedModuleElement[_AlgebraElement] | None: ...
    def lift(
        self,
        f: FPModuleMorphism[_AlgebraElement],
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement] | None: ...
    def split(
        self,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement] | None: ...
    def homology(
        self,
        f: FPModuleMorphism[_AlgebraElement],
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def suspension(
        self,
        t: int | Integer,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def cokernel_projection(self) -> FPModuleMorphism[_AlgebraElement]: ...
    def kernel_inclusion(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def image(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
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
    ) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def _resolve_image(
        self,
        top_dim: int | Integer | None = ...,
        verbose: bool = ...,
    ) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def fp_module(
        self,
    ) -> FPModule[_AlgebraElement] | FreeGradedModule[_AlgebraElement]: ...

from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import FreeGradedModule
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.homspace import FPModuleHomspace
from sage.modules.fp_graded.module import FPModule
