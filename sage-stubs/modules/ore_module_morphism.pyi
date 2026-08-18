from collections.abc import Mapping, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.matrix.matrix import Matrix
from sage.modules.ore_module import OreModule, OreQuotientModule, OreSubmodule
from sage.modules.ore_module_element import OreModuleElement
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import ElementConstructorInput, RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type OreModuleMorphismInput[_Scalar: RingElement] = (
    ElementConstructorInput
    | Matrix[_Scalar]
    | OreModuleMorphism[_Scalar]
    | Sequence[OreModuleElement[_Scalar]]
    | Mapping[OreModuleElement[_Scalar], OreModuleElement[_Scalar]]
)

class OreModuleMorphism(
    Morphism[OreModuleElement[_Scalar], OreModuleElement[_Scalar]],
    Generic[_Scalar],
):
    def __init__(
        self,
        parent: OreModule_homspace[_Scalar],
        im_gens: OreModuleMorphismInput[_Scalar],
        check: bool = ...,
    ) -> None: ...
    def _call_(
        self,
        x: OreModuleElement[_Scalar],
    ) -> OreModuleElement[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def matrix(self) -> Matrix[_Scalar]: ...
    def is_zero(self) -> bool: ...
    def is_identity(self) -> bool: ...
    def __copy__(self) -> Self: ...
    def _add_(self, other: OreModuleMorphism[_Scalar]) -> Self: ...
    def _neg_(self) -> Self: ...
    def _sub_(self, other: OreModuleMorphism[_Scalar]) -> Self: ...
    def _rmul_(self, a: _Scalar) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def is_bijective(self) -> bool: ...
    def is_isomorphism(self) -> bool: ...
    def _composition_(
        self,
        other: OreModuleMorphism[_Scalar],
        homset: OreModule_homspace[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def inverse(self) -> OreModuleMorphism[_Scalar]: ...
    __invert__ = inverse
    def kernel(self, names: str | Sequence[str] | None = ...) -> OreSubmodule[_Scalar]: ...
    def image(
        self,
        saturate: bool = ...,
        names: str | Sequence[str] | None = ...,
    ) -> OreSubmodule[_Scalar]: ...
    def cokernel(
        self,
        remove_torsion: bool = ...,
        names: str | Sequence[str] | None = ...,
    ) -> OreQuotientModule[_Scalar]: ...
    def coimage(
        self,
        names: str | Sequence[str] | None = ...,
    ) -> OreQuotientModule[_Scalar]: ...
    def determinant(self) -> _Scalar: ...
    det = determinant
    def characteristic_polynomial(self, var: str = ...) -> Polynomial: ...
    charpoly = characteristic_polynomial

class OreModuleRetraction(
    Map[OreModuleElement[_Scalar], OreModuleElement[_Scalar]],
    Generic[_Scalar],
):
    def _call_(
        self,
        y: OreModuleElement[_Scalar],
    ) -> OreModuleElement[_Scalar]: ...

class OreModuleSection(
    Map[OreModuleElement[_Scalar], OreModuleElement[_Scalar]],
    Generic[_Scalar],
):
    def _call_(
        self,
        y: OreModuleElement[_Scalar],
    ) -> OreModuleElement[_Scalar]: ...

from sage.modules.ore_module_homspace import OreModule_homspace
