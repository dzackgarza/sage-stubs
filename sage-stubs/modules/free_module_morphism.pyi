from typing import Generic, Literal, TypeVar

from sage.modules.free_module import FreeModule_generic
from sage.structure.element import Matrix, RingElement

from .matrix_morphism import MatrixMorphism

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class FreeModuleMorphism(MatrixMorphism, Generic[_Scalar]):
    def kernel(self) -> FreeModule_generic[RingElement]: ...
    def image(self) -> FreeModule_generic[RingElement]: ...
    def matrix(
        self, side: Literal["left", "right"] | None = ...
    ) -> Matrix[RingElement]: ...
