from typing import Generic, TypeVar

from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_pseudomorphism import FreeModulePseudoMorphism
from sage.structure.element import RingElement

_DomainScalar = TypeVar("_DomainScalar", bound=RingElement)
_CodomainScalar = TypeVar("_CodomainScalar", bound=RingElement)


class FreeModulePseudoHomspace(
    Homset[
        FreeModulePseudoMorphism[_DomainScalar, _CodomainScalar],
        FreeModuleElement[_DomainScalar],
        FreeModuleElement[_CodomainScalar],
    ],
    Generic[_DomainScalar, _CodomainScalar],
):
    def __init__(
        self,
        domain: FreeModule_generic[_DomainScalar],
        codomain: FreeModule_generic[_CodomainScalar],
        twisting_morphism: Map[_DomainScalar, _CodomainScalar],
    ) -> None: ...
    def domain(self) -> FreeModule_generic[_DomainScalar]: ...
    def codomain(self) -> FreeModule_generic[_CodomainScalar]: ...
    def twisting_morphism(self) -> Map[_DomainScalar, _CodomainScalar]: ...
    def matrix_space(self) -> MatrixSpace[_CodomainScalar]: ...
    def _element_constructor_(
        self,
        matrix: Matrix[_CodomainScalar],
        side: str = ...,
    ) -> FreeModulePseudoMorphism[_DomainScalar, _CodomainScalar]: ...
