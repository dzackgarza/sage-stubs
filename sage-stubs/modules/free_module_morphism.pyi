from typing import Generic, Literal, TypeVar

from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from .matrix_morphism import MatrixMorphism
from sage.structure.element import Matrix, RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class FreeModuleMorphism(MatrixMorphism, Generic[_Scalar]):
    def kernel(self) -> FreeModule_generic[_Scalar]: ...
    def image(self) -> FreeModule_generic[_Scalar]: ...
    def matrix(self, side: Literal["left", "right"] | None = ...) -> Matrix[_Scalar]: ...
