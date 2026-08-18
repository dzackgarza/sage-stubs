from typing import Generic, TypeVar

from sage.categories.pushout import ConstructionFunctor
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule_generic
from sage.modules.quotient_module import FreeModule_quotient
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type QuotientModule[_Scalar: RingElement] = (
    FGP_Module_class[_Scalar]
    | FreeModule_quotient[_Scalar]
)

class QuotientModuleFunctor(ConstructionFunctor, Generic[_Scalar]):
    rank: int

    def __init__(self, relations: FreeModule_generic[_Scalar]) -> None: ...
    def relations(self) -> FreeModule_generic[_Scalar]: ...
    def _apply_functor(
        self,
        ambient: FreeModule_generic[_Scalar],
    ) -> QuotientModule[_Scalar]: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def merge(
        self,
        other: ConstructionFunctor,
    ) -> QuotientModuleFunctor[_Scalar] | None: ...
