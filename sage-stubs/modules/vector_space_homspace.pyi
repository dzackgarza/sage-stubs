from typing import Generic, TypeVar

from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.vector_space_morphism import (
    LinearTransformationRule,
    VectorSpaceMorphism,
)
from sage.structure.element import FieldElement

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)


class VectorSpaceHomspace(
    FreeModuleHomspace[_Scalar, _Scalar],
    Generic[_Scalar],
):
    def __call__(
        self,
        A: VectorSpaceMorphism[_Scalar]
        | LinearTransformationRule[_Scalar],
        check: bool = ...,
        **kwds: object,
    ) -> VectorSpaceMorphism[_Scalar]: ...
    def _repr_(self) -> str: ...
