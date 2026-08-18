from typing import Generic, TypeVar

from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import VectorSpace
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.vector_space_morphism import VectorSpaceMorphism
from sage.sets.family import AbstractFamily
from sage.structure.element import FieldElement

_Scalar = TypeVar("_Scalar", bound=FieldElement, default=FieldElement)


class VectorSpaceHomspace(
    FreeModuleHomspace[_Scalar],
    Generic[_Scalar],
):
    element_class: type[VectorSpaceMorphism[_Scalar]]
    def domain(self) -> VectorSpace[_Scalar]: ...
    def codomain(self) -> VectorSpace[_Scalar]: ...
    def matrix_space(self) -> MatrixSpace[_Scalar]: ...
    def dimension(self) -> int: ...
    def basis(self) -> AbstractFamily: ...
    def zero(self) -> VectorSpaceMorphism[_Scalar]: ...
    def identity(self) -> VectorSpaceMorphism[_Scalar]: ...
    one = identity
    def _element_constructor_(
        self,
        matrix: object,
        side: str = ...,
    ) -> VectorSpaceMorphism[_Scalar]: ...
    def natural_map(self) -> VectorSpaceMorphism[_Scalar]: ...
