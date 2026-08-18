from collections.abc import Sequence
from typing import Generic, TypeVar

from sage.categories.functor import ConstructionFunctor, Functor
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.quotient_module import FreeModule_quotient
from sage.structure.element import RingElement
from sage.structure.parent import Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_TargetScalar = TypeVar("_TargetScalar", bound=RingElement)


class ModuleFunctor(ConstructionFunctor, Generic[_Scalar]):
    def rank(self) -> int: ...
    def __call__(
        self,
        ring: Parent[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...


class FreeModuleFunctor(ModuleFunctor[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        rank: int,
        sparse: bool = ...,
        inner_product_matrix: object | None = ...,
    ) -> None: ...
    def rank(self) -> int: ...
    def is_sparse(self) -> bool: ...
    def __call__(
        self,
        ring: Parent[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...


class VectorFunctor(FreeModuleFunctor[_Scalar], Generic[_Scalar]):
    pass


class SubspaceFunctor(ConstructionFunctor, Generic[_Scalar]):
    def __init__(
        self,
        generators: Sequence[FreeModuleElement[_Scalar]],
        ambient_dimension: int,
    ) -> None: ...
    def __call__(
        self,
        ring: Parent[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...


class QuotientModuleFunctor(ConstructionFunctor, Generic[_Scalar]):
    def __init__(
        self,
        relations: Sequence[FreeModuleElement[_Scalar]],
        ambient_dimension: int,
    ) -> None: ...
    def __call__(
        self,
        ring: Parent[_Scalar],
    ) -> FreeModule_quotient[_Scalar]: ...


class BaseChangeFunctor(Functor, Generic[_Scalar, _TargetScalar]):
    def __init__(
        self,
        target_ring: Parent[_TargetScalar],
    ) -> None: ...
    def __call__(
        self,
        module: FreeModule_generic[_Scalar],
    ) -> FreeModule_generic[_TargetScalar]: ...
