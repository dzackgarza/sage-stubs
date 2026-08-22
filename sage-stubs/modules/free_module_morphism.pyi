from collections.abc import Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import (
    FreeModule_generic,
    FreeModule_generic_field,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.matrix_morphism import MatrixMorphism
from sage.structure.element import FieldElement, RingElement
from sage.structure.parent import Parent

_DomainScalar = TypeVar(
    "_DomainScalar",
    bound=RingElement,
    default=RingElement,
)
_CodomainScalar = TypeVar(
    "_CodomainScalar",
    bound=RingElement,
    default=RingElement,
)
_NewScalar = TypeVar("_NewScalar", bound=RingElement)

type MatrixSide = Literal["left", "right"]


class FreeModuleMorphism(
    MatrixMorphism[
        FreeModuleElement[_DomainScalar],
        FreeModuleElement[_CodomainScalar],
        _CodomainScalar,
    ],
    Generic[_DomainScalar, _CodomainScalar],
):
    def __init__(
        self,
        parent: FreeModuleHomspace[_DomainScalar, _CodomainScalar],
        A: Matrix[_CodomainScalar] | MatrixMorphism,
        side: MatrixSide = ...,
    ) -> None: ...
    def pushforward(
        self,
        x: FreeModule_generic[_DomainScalar],
    ) -> FreeModule_generic[_CodomainScalar]: ...
    def _repr_(self) -> str: ...
    def change_ring(
        self,
        R: Parent[_NewScalar],
    ) -> FreeModuleMorphism[_NewScalar, _NewScalar]: ...
    def inverse_image(
        self,
        V: FreeModule_generic[_CodomainScalar],
    ) -> FreeModule_generic[_DomainScalar]: ...
    def lift(
        self,
        x: FreeModuleElement[_CodomainScalar],
    ) -> FreeModuleElement[_DomainScalar]: ...
    preimage_representative = lift
    def eigenvalues(
        self,
        extend: bool = ...,
    ) -> list[RingElement]: ...
    def eigenvectors(
        self,
        extend: bool = ...,
    ) -> list[
        tuple[
            RingElement,
            Sequence[FreeModuleElement[RingElement]],
            int,
        ]
    ]: ...
    def eigenspaces(
        self,
        extend: bool = ...,
    ) -> list[
        tuple[
            RingElement,
            FreeModule_generic_field[FieldElement],
        ]
    ]: ...


class BaseIsomorphism1D(Morphism):
    def _repr_type(self) -> str: ...
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def _richcmp_(self, other: BaseIsomorphism1D, op: int) -> bool: ...


class BaseIsomorphism1D_to_FM(BaseIsomorphism1D):
    def __init__(
        self,
        parent: Homset,
        basis: RingElement | None = ...,
    ) -> None: ...
    def _call_(self, x: RingElement) -> FreeModuleElement[RingElement]: ...


class BaseIsomorphism1D_from_FM(BaseIsomorphism1D):
    def __init__(
        self,
        parent: Homset,
        basis: RingElement | None = ...,
    ) -> None: ...
    def _call_(self, x: FreeModuleElement[RingElement]) -> RingElement: ...


from sage.modules.free_module_homspace import FreeModuleHomspace
