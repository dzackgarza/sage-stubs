from collections.abc import Callable, Hashable, Iterable
from typing import Generic, TypeVar

from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.with_basis.representation import Representation_abstract
from sage.modules.with_basis.subquotient import SubmoduleWithBasis
from sage.structure.element import Element, RingElement

_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_Actor = TypeVar("_Actor", bound=Element, default=Element)


class FiniteDimensionalInvariantModule(
    SubmoduleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        representation: Representation_abstract[_Actor, _Index, _Scalar],
        S: Iterable[_Actor] | None = ...,
        action: Callable | None = ...,
        side: str = ...,
    ) -> None: ...
    def representation(self) -> Representation_abstract[_Actor, _Index, _Scalar]: ...
    def acting_set(self) -> tuple[_Actor, ...]: ...


class InvariantModule(
    FiniteDimensionalInvariantModule[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    pass


class TwistedInvariantModule(
    FiniteDimensionalInvariantModule[_Actor, _Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def character(self) -> Callable[[_Actor], _Scalar]: ...


def invariant_module(
    representation: Representation_abstract[_Actor, _Index, _Scalar],
    S: Iterable[_Actor] | None = ...,
) -> InvariantModule[_Actor, _Index, _Scalar]: ...


def twisted_invariant_module(
    representation: Representation_abstract[_Actor, _Index, _Scalar],
    character: Callable[[_Actor], _Scalar],
    S: Iterable[_Actor] | None = ...,
) -> TwistedInvariantModule[_Actor, _Index, _Scalar]: ...
