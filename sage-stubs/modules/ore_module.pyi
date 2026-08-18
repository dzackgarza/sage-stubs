from collections.abc import Iterable, Mapping, Sequence
from typing import Generic, TypeVar

from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.ore_modules import OreModules
from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_ambient, FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.free_module_pseudomorphism import FreeModulePseudoMorphism
from sage.rings.derivation import RingDerivation
from sage.rings.morphism import RingHomomorphism
from sage.rings.polynomial.ore_polynomial_element import OrePolynomial
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing
from sage.structure.element import RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

type OreModuleNames = str | Sequence[str] | None
type OreModuleGenerator[_Scalar: RingElement] = (
    OreModuleElement[_Scalar]
    | OreModule[_Scalar]
    | Iterable[ElementConstructorInput]
)
type OreModuleMorphismData[_Scalar: RingElement] = (
    Matrix[_Scalar]
    | OreModuleMorphism[_Scalar]
    | Sequence[OreModuleElement[_Scalar]]
    | Mapping[OreModuleElement[_Scalar], OreModuleElement[_Scalar]]
)

class ScalarAction(Action):
    def _act_(
        self,
        a: _Scalar,
        x: OreModuleElement[_Scalar],
    ) -> OreModuleElement[_Scalar]: ...

class OreAction(Action):
    def _act_(
        self,
        P: OrePolynomial,
        x: OreModuleElement[_Scalar],
    ) -> OreModuleElement[_Scalar]: ...

def normalize_names(
    names: OreModuleNames,
    rank: int,
) -> tuple[str, ...] | None: ...

class OreModule(
    UniqueRepresentation,
    FreeModule_ambient[_Scalar],
    Generic[_Scalar],
):
    Element: type[OreModuleElement[_Scalar]]

    @staticmethod
    def __classcall_private__(
        class_: type[OreModule[_Scalar]],
        mat: Matrix[_Scalar],
        twist: OrePolynomialRing | RingHomomorphism | RingDerivation,
        denominator: _Scalar | Factorization | None = ...,
        names: OreModuleNames = ...,
        category: Category | None = ...,
    ) -> OreModule[_Scalar]: ...
    def __init__(
        self,
        mat: Matrix[_Scalar],
        ore: OrePolynomialRing,
        denominator: Factorization | None,
        names: tuple[str, ...] | None,
        category: OreModules,
    ) -> None: ...
    def _element_constructor_(
        self,
        x: OreModuleElement[_Scalar] | Iterable[ElementConstructorInput],
    ) -> OreModuleElement[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _repr_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def _latex_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def is_zero(self) -> bool: ...
    def rename_basis(
        self,
        names: OreModuleNames,
        coerce: bool = ...,
    ) -> OreModule[_Scalar]: ...
    def pseudohom(self) -> FreeModulePseudoMorphism[_Scalar, _Scalar]: ...
    def ore_ring(
        self,
        names: str = ...,
        action: bool = ...,
    ) -> OrePolynomialRing: ...
    def twisting_morphism(self) -> RingHomomorphism | None: ...
    def twisting_derivation(self) -> RingDerivation | None: ...
    def matrix(self) -> Matrix[RingElement]: ...
    action_matrix = matrix
    def over_fraction_field(self) -> OreModule[RingElement]: ...
    def basis(self) -> list[OreModuleElement[_Scalar]]: ...
    def gens(self) -> list[OreModuleElement[_Scalar]]: ...
    def gen(self, i: int) -> OreModuleElement[_Scalar]: ...
    def _an_element_(self) -> OreModuleElement[_Scalar]: ...
    def random_element(
        self,
        *args: object,
        **kwds: object,
    ) -> OreModuleElement[_Scalar]: ...
    def module(self) -> FreeModule_generic[_Scalar]: ...
    def _Hom_(
        self,
        codomain: OreModule[_Scalar],
        category: Category,
    ) -> OreModule_homspace[_Scalar]: ...
    def hom(
        self,
        im_gens: OreModuleMorphismData[_Scalar],
        codomain: OreModule[_Scalar] | None = ...,
    ) -> OreModuleMorphism[_Scalar]: ...
    def multiplication_map(
        self,
        P: OrePolynomial | ElementConstructorInput,
    ) -> OreModuleMorphism[_Scalar]: ...
    def identity_morphism(self) -> OreModuleMorphism[_Scalar]: ...
    def span(
        self,
        gens: OreModuleGenerator[_Scalar] | Sequence[OreModuleGenerator[_Scalar]],
        saturate: bool = ...,
        names: OreModuleNames = ...,
        check: bool = ...,
    ) -> OreSubmodule[_Scalar]: ...
    submodule = span
    def quotient(
        self,
        sub: OreModuleGenerator[_Scalar] | Sequence[OreModuleGenerator[_Scalar]],
        remove_torsion: bool = ...,
        names: OreModuleNames = ...,
        check: bool = ...,
    ) -> OreQuotientModule[_Scalar]: ...
    quo = quotient
    def ambient_modules(self) -> list[OreModule[_Scalar]]: ...
    def ambient_module(self) -> OreModule[_Scalar]: ...
    def is_submodule(self, other: OreModule[_Scalar]) -> bool: ...
    def fitting_index(
        self,
        other: OreModule[_Scalar] | None = ...,
    ) -> RingElement: ...
    def covers(self) -> list[OreModule[_Scalar]]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...

class OreSubmodule(OreModule[_Scalar], Generic[_Scalar]):
    @staticmethod
    def __classcall_private__(
        class_: type[OreSubmodule[_Scalar]],
        ambient: OreModule[_Scalar],
        gens: Matrix[_Scalar] | Sequence[OreModuleElement[_Scalar]],
        saturate: bool,
        names: OreModuleNames,
    ) -> OreSubmodule[_Scalar]: ...
    def ambient_module(self) -> OreModule[_Scalar]: ...
    def over_fraction_field(self) -> OreSubmodule[RingElement]: ...
    def saturate(
        self,
        names: OreModuleNames = ...,
        coerce: bool = ...,
    ) -> OreSubmodule[_Scalar]: ...
    def rename_basis(
        self,
        names: OreModuleNames,
        coerce: bool = ...,
    ) -> OreSubmodule[_Scalar]: ...
    def injection_morphism(self) -> OreModuleMorphism[_Scalar]: ...
    def morphism_restriction(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def morphism_corestriction(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...

class OreQuotientModule(OreModule[_Scalar], Generic[_Scalar]):
    @staticmethod
    def __classcall_private__(
        class_: type[OreQuotientModule[_Scalar]],
        cover: OreModule[_Scalar],
        gens: Matrix[_Scalar] | Sequence[OreModuleElement[_Scalar]],
        remove_torsion: bool,
        names: OreModuleNames,
    ) -> OreQuotientModule[_Scalar]: ...
    def cover(self) -> OreModule[_Scalar]: ...
    def projection_morphism(self) -> OreModuleMorphism[_Scalar]: ...
    def section(self) -> Map[OreModuleElement[_Scalar], OreModuleElement[_Scalar]]: ...
    def morphism_quotient(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...

from sage.modules.ore_module_element import OreModuleElement
from sage.modules.ore_module_homspace import OreModule_homspace
from sage.modules.ore_module_morphism import OreModuleMorphism
