from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.sage_object import SageObject

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class TensorOperation(SageObject, Generic[_Scalar]):
    def domain(self) -> tuple[FreeModule_generic[_Scalar], ...]: ...
    def codomain(self) -> FreeModule_generic[_Scalar]: ...
    def __call__(
        self,
        *vectors: FreeModuleElement[_Scalar],
    ) -> FreeModuleElement[_Scalar]: ...


class TensorProductOperation(TensorOperation[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        modules: Sequence[FreeModule_generic[_Scalar]],
    ) -> None: ...


class SymmetricPowerOperation(TensorOperation[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        module: FreeModule_generic[_Scalar],
        degree: int,
    ) -> None: ...
    def degree(self) -> int: ...


class ExteriorPowerOperation(TensorOperation[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        module: FreeModule_generic[_Scalar],
        degree: int,
    ) -> None: ...
    def degree(self) -> int: ...


def tensor_product(
    *modules: FreeModule_generic[_Scalar],
) -> FreeModule_generic[_Scalar]: ...


def symmetric_power(
    module: FreeModule_generic[_Scalar],
    degree: int,
) -> FreeModule_generic[_Scalar]: ...


def exterior_power(
    module: FreeModule_generic[_Scalar],
    degree: int,
) -> FreeModule_generic[_Scalar]: ...


def dual(
    module: FreeModule_generic[_Scalar],
) -> FreeModule_generic[_Scalar]: ...
