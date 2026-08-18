from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class FreeModuleHomspace(
    Homset[
        FreeModuleMorphism[_Scalar],
        FreeModuleElement[_Scalar],
        FreeModuleElement[_Scalar],
    ],
    Generic[_Scalar],
):
    element_class: type[FreeModuleMorphism[_Scalar]]
    def __init__(
        self,
        domain: FreeModule_generic[_Scalar],
        codomain: FreeModule_generic[_Scalar],
        category: Category | None = ...,
    ) -> None: ...
    def domain(self) -> FreeModule_generic[_Scalar]: ...
    def codomain(self) -> FreeModule_generic[_Scalar]: ...
    def matrix_space(self) -> MatrixSpace[_Scalar]: ...
    def dimension(self) -> int: ...
    def rank(self) -> int: ...
    def basis(self) -> AbstractFamily: ...
    def zero(self) -> FreeModuleMorphism[_Scalar]: ...
    def identity(self) -> FreeModuleMorphism[_Scalar]: ...
    one = identity
    def random_element(self, *args: object, **kwds: object) -> FreeModuleMorphism[_Scalar]: ...
    def _element_constructor_(
        self,
        matrix: Matrix[_Scalar]
        | list[FreeModuleElement[_Scalar]]
        | FreeModuleMorphism[_Scalar],
        side: str = ...,
    ) -> FreeModuleMorphism[_Scalar]: ...
