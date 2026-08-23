from collections.abc import Iterable
from typing import Generic, TypeVar

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import (
    FreeModule_ambient,
    FreeModuleInput,
    Module_free_ambient,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.quotient_module import QuotientModule_free_ambient
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type AmbientFreeModule[_Scalar: RingElement] = (
    FreeModule_ambient[_Scalar] | QuotientModule_free_ambient[_Scalar]
)

class Submodule_free_ambient(
    Module_free_ambient[_Scalar],
    Generic[_Scalar],
):
    def __init__(
        self,
        ambient: AmbientFreeModule[_Scalar],
        gens: Iterable[FreeModuleInput[_Scalar]],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> None: ...
    def _groebner_basis_contains(
        self,
        v: FreeModuleInput[_Scalar],
    ) -> bool: ...
    def _check_element_membership(
        self,
        x: FreeModuleInput[_Scalar],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    generators_matrix = matrix
    def relations(self) -> Submodule_free_ambient[_Scalar]: ...
    def gens(self) -> list[FreeModuleElement[_Scalar]]: ...
    def gen(self, i: int = ...) -> FreeModuleElement[_Scalar]: ...
    def ambient_module(self) -> AmbientFreeModule[_Scalar]: ...

Submodule = Submodule_free_ambient
