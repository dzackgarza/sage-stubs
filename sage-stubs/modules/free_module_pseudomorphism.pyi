from collections.abc import Sequence
from typing import Generic, Literal, TypeVar

from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.derivation import RingDerivation
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

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

type MatrixSide = Literal["left", "right"]
type OreModuleNames = str | Sequence[str] | None
type PseudoMatrixData[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | Sequence[Sequence[ElementConstructorInput]]
)


class FreeModulePseudoMorphism(
    Morphism[
        FreeModuleElement[_DomainScalar],
        FreeModuleElement[_CodomainScalar],
    ],
    Generic[_DomainScalar, _CodomainScalar],
):
    def __init__(
        self,
        parent: FreeModulePseudoHomspace[_DomainScalar],
        f: PseudoMatrixData[_CodomainScalar]
        | FreeModulePseudoMorphism[_DomainScalar, _CodomainScalar]
        | FreeModuleMorphism[_DomainScalar, _CodomainScalar],
        side: MatrixSide,
    ) -> None: ...
    def _call_(
        self,
        x: FreeModuleElement[_DomainScalar],
    ) -> FreeModuleElement[_CodomainScalar]: ...
    def _repr_(self) -> str: ...
    def matrix(self) -> Matrix[_CodomainScalar]: ...
    def twisting_derivation(self) -> RingDerivation | None: ...
    def twisting_morphism(
        self,
    ) -> Map[_DomainScalar, _CodomainScalar] | None: ...
    def side(self) -> MatrixSide: ...
    def side_switch(
        self,
    ) -> FreeModulePseudoMorphism[_DomainScalar, _CodomainScalar]: ...
    def __nonzero__(self) -> bool: ...
    def _richcmp_(
        self,
        other: FreeModulePseudoMorphism[_DomainScalar, _CodomainScalar],
        op: int,
    ) -> bool: ...
    def _composition_(
        self,
        right: Morphism,
        homset: Homset,
    ) -> FreeModulePseudoMorphism[_DomainScalar, _CodomainScalar] | Morphism: ...
    def ore_module(
        self,
        names: OreModuleNames = ...,
    ) -> OreModule[_CodomainScalar]: ...
    def _test_nonzero_equal(self, tester: object) -> None: ...


from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.free_module_pseudohomspace import FreeModulePseudoHomspace
from sage.modules.ore_module import OreModule
