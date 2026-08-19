from typing import Generic, TypeVar

from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic_field
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.vector_space_morphism import (
    LinearTransformationRule,
    MatrixSide,
    VectorSpaceMorphism,
)
from sage.structure.element import FieldElement

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)

class VectorSpaceHomspace(
    FreeModuleHomspace[_Scalar, _Scalar],
    Generic[_Scalar],
):
    element_class: type[VectorSpaceMorphism[_Scalar]]

    def domain(self) -> FreeModule_generic_field[_Scalar]: ...
    def codomain(self) -> FreeModule_generic_field[_Scalar]: ...
    def matrix_space(self) -> MatrixSpace[_Scalar]: ...
    def __call__(
        self,
        A: VectorSpaceMorphism[_Scalar]
        | LinearTransformationRule[_Scalar],
        check: bool = ...,
        **kwds: object,
    ) -> VectorSpaceMorphism[_Scalar]: ...
    def zero(self) -> VectorSpaceMorphism[_Scalar]: ...
    def identity(self) -> VectorSpaceMorphism[_Scalar]: ...
    one = identity
    def _repr_(self) -> str: ...
