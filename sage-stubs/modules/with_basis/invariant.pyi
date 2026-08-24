from collections.abc import Callable, Hashable, Sequence
from typing import Generic, Literal, Self, TypeVar

from sage.categories.pushout import ConstructionFunctor
from sage.combinat.free_module import CombinatorialFreeModule
from sage.matrix.matrix0 import Matrix
from sage.modules.with_basis.indexed_element import IndexedFreeModuleElement
from sage.modules.with_basis.subquotient import SubmoduleWithBasis
from sage.structure.element import Element, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

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
    def _test_invariant(self, **options: object) -> None: ...
    def semigroup(self) -> Parent[_Actor]: ...
    def semigroup_representation(self) -> CombinatorialFreeModule: ...

    class Element(SubmoduleWithBasis.Element):
        def _mul_(self, other: Self) -> Self: ...
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...


class FiniteDimensionalTwistedInvariantModule(
    SubmoduleWithBasis[_Index, _Scalar],
    Generic[_Actor, _Index, _Scalar],
):
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

    class Element(SubmoduleWithBasis.Element):
        def _acted_upon_(
            self,
            scalar: ElementConstructorInput,
            self_on_left: bool = ...,
        ) -> Self | None: ...
