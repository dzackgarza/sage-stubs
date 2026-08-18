from collections.abc import Iterable
from typing import Generic, TypeVar

from sage.matrix.matrix import Matrix
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class FGP_CongruenceModule(FGP_Module_class[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        ambient: FreeModule_generic[_Scalar],
        relations: FreeModule_submodule[_Scalar],
        modulus: _Scalar,
        check: bool = ...,
    ) -> None: ...
    def modulus(self) -> _Scalar: ...
    def congruence_matrix(self) -> Matrix[_Scalar]: ...
    def lift_generators(self) -> tuple[FreeModuleElement[_Scalar], ...]: ...
    def submodule(
        self,
        generators: Iterable[object],
    ) -> FGP_CongruenceModule[_Scalar]: ...
