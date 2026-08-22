from typing import Generic, Literal, TypeVar

from sage.categories.homset import HomsetWithBase
from sage.categories.map import Map
from sage.matrix.matrix_space import MatrixSpace
from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.free_module_pseudomorphism import (
    FreeModulePseudoMorphism,
    PseudoMatrixData,
)
from sage.rings.derivation import RingDerivation
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing
from sage.structure.element import RingElement
from sage.structure.sequence import Sequence_generic
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type MatrixSide = Literal["left", "right"]
type PseudoTwist[_Scalar: RingElement] = (
    OrePolynomialRing
    | Map[_Scalar, _Scalar]
    | RingDerivation
)
type PseudoMorphismData[_Scalar: RingElement] = (
    PseudoMatrixData[_Scalar]
    | FreeModulePseudoMorphism[_Scalar, _Scalar]
    | FreeModuleMorphism[_Scalar, _Scalar]
)


class FreeModulePseudoHomspace(
    UniqueRepresentation,
    HomsetWithBase[
        FreeModulePseudoMorphism[_Scalar, _Scalar],
        FreeModuleElement[_Scalar],
        FreeModuleElement[_Scalar],
    ],
    Generic[_Scalar],
):
    Element: type[FreeModulePseudoMorphism[_Scalar, _Scalar]]
    element_class: type[FreeModulePseudoMorphism[_Scalar, _Scalar]]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeModulePseudoHomspace[_Scalar]],
        domain: FreeModule_generic[_Scalar],
        codomain: FreeModule_generic[_Scalar],
        twist: PseudoTwist[_Scalar],
    ) -> FreeModulePseudoHomspace[_Scalar]: ...
    def __init__(
        self,
        domain: FreeModule_generic[_Scalar],
        codomain: FreeModule_generic[_Scalar],
        ore: OrePolynomialRing,
    ) -> None: ...
    def _element_constructor_(
        self,
        f: PseudoMorphismData[_Scalar],
        side: MatrixSide = ...,
    ) -> FreeModulePseudoMorphism[_Scalar, _Scalar]: ...
    def __reduce__(
        self,
    ) -> tuple[
        type[FreeModulePseudoHomspace[_Scalar]],
        tuple[
            FreeModule_generic[_Scalar],
            FreeModule_generic[_Scalar],
            PseudoTwist[_Scalar],
        ],
    ]: ...
    def _repr_(self) -> str: ...
    def ore_ring(self, var: str = ...) -> OrePolynomialRing: ...
    def matrix_space(self) -> MatrixSpace[_Scalar]: ...
    def basis(self, side: MatrixSide = ...) -> Sequence_generic: ...
    def _test_additive_associativity(self, tester: object) -> None: ...
    def _test_distributivity(self, tester: object) -> None: ...
    def _test_one(self, tester: object) -> None: ...
    def _test_zero(self, tester: object) -> None: ...
