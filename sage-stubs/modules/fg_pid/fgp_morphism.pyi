from typing import Generic, Self, TypeVar, overload

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type FGPUnderlyingMorphism[_Scalar: RingElement] = (
    Morphism[FreeModuleElement[_Scalar], FreeModuleElement[_Scalar]]
    | _Scalar
)

def FGP_Homset(
    X: FGP_Module_class[_Scalar],
    Y: FGP_Module_class[_Scalar],
) -> FGP_Homset_class[_Scalar]: ...

class FGP_Morphism(
    Morphism[FGP_Element[_Scalar], FGP_Element[_Scalar]],
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: FGP_Homset_class[_Scalar],
        phi: FGP_Morphism[_Scalar] | FGPUnderlyingMorphism[_Scalar],
        check: bool = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def im_gens(self) -> tuple[FGP_Element[_Scalar], ...]: ...
    def _richcmp_(self, other: FGP_Morphism[_Scalar], op: int) -> bool: ...
    def __add__(self, right: FGP_Morphism[_Scalar] | _Scalar) -> Self: ...
    def __sub__(self, right: FGP_Morphism[_Scalar] | _Scalar) -> Self: ...
    def __neg__(self) -> Self: ...
    @overload
    def __call__(
        self,
        x: FGP_Module_class[_Scalar],
    ) -> FGP_Module_class[_Scalar]: ...
    @overload
    def __call__(
        self,
        x: FGP_Element[_Scalar] | FreeModuleElement[_Scalar],
    ) -> FGP_Element[_Scalar]: ...
    def kernel(self) -> FGP_Module_class[_Scalar]: ...
    def inverse_image(
        self,
        A: FGP_Module_class[_Scalar],
    ) -> FGP_Module_class[_Scalar]: ...
    def image(self) -> FGP_Module_class[_Scalar]: ...
    def lift(
        self,
        x: FGP_Element[_Scalar] | FreeModuleElement[_Scalar],
    ) -> FGP_Element[_Scalar]: ...

class FGP_Homset_class(
    Homset[
        FGP_Morphism[_Scalar],
        FGP_Element[_Scalar],
        FGP_Element[_Scalar],
    ],
    Generic[_Scalar],
):
    Element: type[FGP_Morphism[_Scalar]]

    def __init__(
        self,
        X: FGP_Module_class[_Scalar],
        Y: FGP_Module_class[_Scalar],
        category: Category | None = ...,
    ) -> None: ...
    def _coerce_map_from_(self, S: object) -> bool: ...
    def __call__(
        self,
        x: FGP_Morphism[_Scalar] | FGPUnderlyingMorphism[_Scalar],
    ) -> FGP_Morphism[_Scalar]: ...
