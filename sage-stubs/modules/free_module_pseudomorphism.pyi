from typing import Generic, TypeVar

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement

_DomainScalar = TypeVar("_DomainScalar", bound=RingElement)
_CodomainScalar = TypeVar("_CodomainScalar", bound=RingElement)


class FreeModulePseudoMorphism(
    Morphism[
        FreeModuleElement[_DomainScalar],
        FreeModuleElement[_CodomainScalar],
    ],
    Generic[_DomainScalar, _CodomainScalar],
):
    def __init__(
        self,
        parent: FreeModulePseudoHomspace[_DomainScalar, _CodomainScalar],
        matrix: Matrix[_CodomainScalar],
        side: str = ...,
    ) -> None: ...
    def domain(self) -> FreeModule_generic[_DomainScalar]: ...
    def codomain(self) -> FreeModule_generic[_CodomainScalar]: ...
    def matrix(self, side: str | None = ...) -> Matrix[_CodomainScalar]: ...
    def twisting_morphism(self) -> Map[_DomainScalar, _CodomainScalar]: ...
    def _call_(
        self,
        x: FreeModuleElement[_DomainScalar],
    ) -> FreeModuleElement[_CodomainScalar]: ...
    def rank(self) -> int: ...
    def kernel(self) -> FreeModule_submodule[_DomainScalar]: ...
    def image(self) -> FreeModule_submodule[_CodomainScalar]: ...
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...


from sage.modules.free_module_pseudohomspace import FreeModulePseudoHomspace
