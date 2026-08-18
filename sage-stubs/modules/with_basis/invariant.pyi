from collections.abc import Callable, Hashable, Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.pushout import ConstructionFunctor
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.subquotient import SubmoduleWithBasis
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent

_Actor = TypeVar("_Actor", bound=Element, default=Element)
_Index = TypeVar("_Index", bound=Hashable, default=Hashable)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type InvariantSide = Literal["left", "right"]
type AmbientElement[_Index: Hashable, _Scalar: RingElement] = IndexedFreeModuleElement[_Index, _Scalar]
type InvariantAction[_Actor: Element, _Index: Hashable, _Scalar: RingElement] = Callable[
    [_Actor | AmbientElement[_Index, _Scalar], _Actor | AmbientElement[_Index, _Scalar]],
    AmbientElement[_Index, _Scalar],
]
type CharacterInput[_Scalar: RingElement] = Sequence[_Scalar] | Callable[[Element], RingElement]

class FiniteDimensionalInvariantModule(
    SubmoduleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    def __init__(
        self,
        M: CombinatorialFreeModule,
        S: Parent[_Actor],
        action: InvariantAction[_Actor, _Index, _Scalar] | None = ...,
        side: InvariantSide = ...,
        *args: object,
        **kwargs: object,
    ) -> None: ...
    def construction(
        self,
    ) -> tuple[ConstructionFunctor, CombinatorialFreeModule]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def semigroup(self) -> Parent[_Actor]: ...
    def semigroup_representation(self) -> CombinatorialFreeModule: ...

class FiniteDimensionalTwistedInvariantModule(
    SubmoduleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
    @staticmethod
    def __classcall_private__(
        class_: type[FiniteDimensionalTwistedInvariantModule[_Actor, _Index, _Scalar]],
        M: CombinatorialFreeModule,
        G: Parent[_Actor],
        chi: CharacterInput[_Scalar],
        action: InvariantAction[_Actor, _Index, _Scalar] | None = ...,
        side: InvariantSide = ...,
        **kwargs: object,
    ) -> FiniteDimensionalInvariantModule[_Actor, _Index, _Scalar] | FiniteDimensionalTwistedInvariantModule[_Actor, _Index, _Scalar]: ...
    def __init__(
        self,
        M: CombinatorialFreeModule,
        G: Parent[_Actor],
        chi: CharacterInput[_Scalar],
        action: InvariantAction[_Actor, _Index, _Scalar] | None = ...,
        side: InvariantSide = ...,
        **kwargs: object,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def project(
        self,
        x: AmbientElement[_Index, _Scalar],
    ) -> IndexedFreeModuleElement[Hashable, _Scalar]: ...
    def project_ambient(
        self,
        x: AmbientElement[_Index, _Scalar],
    ) -> AmbientElement[_Index, _Scalar]: ...
    def projection_matrix(self) -> Matrix[_Scalar]: ...
