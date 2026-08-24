from collections.abc import Iterable, Mapping, Sequence
from typing import Generic, Self, TypeVar, overload

from sage.categories.action import Action
from sage.categories.category import Category
from sage.categories.map import Map
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import (
    FreeModule_ambient,
    FreeModule_generic,
    FreeModuleInput,
    GeneratorFamily,
    MatrixSide,
    Module_free_ambient,
    PseudoMorphismData,
    PseudoTwist,
)
from sage.modules.free_module_pseudomorphism import FreeModulePseudoMorphism
from sage.modules.module import Module
from sage.modules.ore_module_element import OreModuleElement
from sage.modules.submodule_helper import SubmoduleHelper
from sage.rings.derivation import RingDerivation
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.polynomial.ore_polynomial_element import OrePolynomial
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing
from sage.structure.element import Element, ModuleElement, RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_CodomainScalar = TypeVar("_CodomainScalar", bound=RingElement)
_SourceElement = TypeVar("_SourceElement", bound=ModuleElement)

type OreModuleNames = str | Sequence[str] | None
type OreTwist[_Scalar: RingElement] = (
    OrePolynomialRing
    | Map[_Scalar, _Scalar]
    | RingDerivation
)
type OreModuleElementInput[_Scalar: RingElement] = (
    OreModuleElement[_Scalar]
    | Iterable[ElementConstructorInput]
)
type OreModuleGenerator[_Scalar: RingElement] = (
    OreModuleElement[_Scalar]
    | OreModule[_Scalar]
    | Iterable[ElementConstructorInput]
)
type OreModuleGenerators[_Scalar: RingElement] = (
    OreModuleGenerator[_Scalar]
    | Sequence[OreModuleGenerator[_Scalar]]
)
type OreSubmoduleData[_Scalar: RingElement] = (
    SubmoduleHelper[_Scalar]
    | Matrix[_Scalar]
    | Sequence[OreModuleElement[_Scalar]]
)
type OreModuleMorphismData[_Scalar: RingElement] = (
    ElementConstructorInput
    | Matrix[_Scalar]
    | OreModuleMorphism[_Scalar]
    | Sequence[OreModuleElement[_Scalar]]
    | Mapping[OreModuleElement[_Scalar], OreModuleElement[_Scalar]]
)


class ScalarAction(Action):
    def _act_(
        self,
        g: Element,
        x: Element,
    ) -> OreModuleElement[_Scalar]: ...


class OreAction(Action):
    def _act_(
        self,
        g: Element,
        x: Element,
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
    @staticmethod
    def __classcall_private__(
        class_: type[OreModule[_Scalar]],
        mat: Matrix[_Scalar],
        twist: OreTwist[_Scalar],
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
        category: Category,
    ) -> None: ...
    @overload
    def _element_constructor_(
        self,
        x: OreModuleElementInput[_Scalar],
    ) -> OreModuleElement[_Scalar]: ...
    @overload
    def _element_constructor_(
        self,
        x: FreeModuleInput[_Scalar] | int | Integer = ...,
        coerce: bool = ...,
        copy: bool = ...,
        check: bool = ...,
    ) -> OreModuleElement[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _repr_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def _latex_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def _coerce_map_from_(
        self,
        M: Module[RingElement, _SourceElement],
    ) -> None: ...
    def is_zero(self) -> bool: ...
    def rename_basis(
        self,
        names: OreModuleNames,
        coerce: bool = ...,
    ) -> Self: ...
    @overload
    def pseudohom(self) -> FreeModulePseudoMorphism[_Scalar, _Scalar]: ...
    @overload
    def pseudohom(
        self,
        f: PseudoMorphismData[_Scalar],
        twist: PseudoTwist[_Scalar],
        codomain: FreeModule_generic[_Scalar] | None = ...,
        side: MatrixSide = ...,
    ) -> FreeModulePseudoMorphism[_Scalar, _Scalar]: ...
    def ore_ring(
        self,
        names: str = ...,
        action: bool = ...,
    ) -> OrePolynomialRing: ...
    def twisting_morphism(self) -> Map[_Scalar, _Scalar] | None: ...
    def twisting_derivation(self) -> RingDerivation | None: ...
    def matrix(self) -> Matrix[RingElement]: ...
    def over_fraction_field(self) -> OreModule[RingElement]: ...
    def basis(self) -> list[OreModuleElement[_Scalar]]: ...
    def gens(self) -> list[OreModuleElement[_Scalar]]: ...
    def gen(self, i: int | Integer = ...) -> OreModuleElement[_Scalar]: ...
    def _an_element_(self) -> OreModuleElement[_Scalar]: ...
    def random_element(
        self,
        *args: object,
        **kwds: object,
    ) -> OreModuleElement[_Scalar]: ...
    def module(self) -> FreeModule_ambient[_Scalar]: ...
    @overload
    def _Hom_(
        self,
        codomain: OreModule[_Scalar],
        category: Category | None = ...,
    ) -> OreModule_homspace[_Scalar]: ...
    @overload
    def _Hom_(
        self,
        codomain: FreeModule_generic[_CodomainScalar],
        category: Category | None = ...,
    ) -> FreeModuleHomspace[_Scalar, _CodomainScalar]: ...
    @overload
    def hom(
        self,
        images: OreModuleMorphismData[_Scalar],
        codomain: OreModule[_Scalar] | None = ...,
        side: MatrixSide = ...,
    ) -> OreModuleMorphism[_Scalar]: ...
    @overload
    def hom(
        self,
        images: Sequence[FreeModuleInput[_Scalar]] | Matrix[_Scalar],
        codomain: None = ...,
        side: MatrixSide = ...,
    ) -> FreeModuleMorphism[_Scalar, _Scalar]: ...
    @overload
    def hom(
        self,
        images: Sequence[FreeModuleInput[_CodomainScalar]] | Matrix[_CodomainScalar],
        codomain: FreeModule_generic[_CodomainScalar],
        side: MatrixSide = ...,
    ) -> FreeModuleMorphism[_Scalar, _CodomainScalar]: ...
    def multiplication_map(
        self,
        P: OrePolynomial | ElementConstructorInput,
    ) -> OreModuleMorphism[_Scalar]: ...
    def identity_morphism(self) -> OreModuleMorphism[_Scalar]: ...
    def _span(
        self,
        gens: OreModuleGenerators[_Scalar],
    ) -> Matrix[_Scalar]: ...
    @overload
    def span(
        self,
        gens: OreModuleGenerators[_Scalar],
        saturate: bool = ...,
        names: OreModuleNames = ...,
        check: bool = ...,
    ) -> OreSubmodule[_Scalar]: ...
    @overload
    def span(
        self,
        gens: GeneratorFamily[_Scalar] | Module_free_ambient[_Scalar],
        base_ring: Parent[_Scalar] | None = ...,
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> Module_free_ambient[_Scalar]: ...
    @overload
    def submodule(
        self,
        gens: OreModuleGenerators[_Scalar],
        saturate: bool = ...,
        names: OreModuleNames = ...,
        check: bool = ...,
    ) -> OreSubmodule[_Scalar]: ...
    @overload
    def submodule(
        self,
        gens: GeneratorFamily[_Scalar] | Module_free_ambient[_Scalar],
        check: bool = ...,
        already_echelonized: bool = ...,
    ) -> Module_free_ambient[_Scalar]: ...
    def quotient(
        self,
        sub: OreModuleGenerators[_Scalar],
        remove_torsion: bool = ...,
        names: OreModuleNames = ...,
        check: bool = ...,
    ) -> OreQuotientModule[_Scalar]: ...
    def quo(
        self,
        sub: OreModuleGenerators[_Scalar],
        remove_torsion: bool = ...,
        names: OreModuleNames = ...,
        check: bool = ...,
    ) -> OreQuotientModule[_Scalar]: ...
    def ambient_modules(self) -> list[OreModule[_Scalar]]: ...
    def _pushout_(
        self,
        other: OreModule[_Scalar],
    ) -> OreModule[_Scalar] | None: ...
    def is_submodule(self, other: Module_free_ambient[_Scalar]) -> bool: ...
    def _fitting_index(self) -> _Scalar: ...
    def fitting_index(
        self,
        other: OreModule[_Scalar] | None = ...,
    ) -> RingElement | PlusInfinity: ...
    def covers(self) -> list[OreModule[_Scalar]]: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...


class OreSubmodule(OreModule[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        ambient: OreModule[_Scalar],
        submodule: SubmoduleHelper[_Scalar],
        names: tuple[str, ...] | None,
    ) -> None: ...
    def __reduce__(self) -> tuple[type, tuple[object, ...]]: ...
    def _repr_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def _latex_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def ambient_module(self) -> OreModule[_Scalar]: ...
    def ambient_modules(self) -> list[OreModule[_Scalar]]: ...
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
    def _fitting_index(self) -> _Scalar: ...
    def injection_morphism(self) -> OreModuleMorphism[_Scalar]: ...
    def morphism_restriction(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def morphism_corestriction(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def _hom_change_domain(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def _hom_change_codomain(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...


class OreQuotientModule(OreModule[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        cover: OreModule[_Scalar],
        submodule: SubmoduleHelper[_Scalar],
        names: tuple[str, ...] | None,
    ) -> None: ...
    def __reduce__(self) -> tuple[type, tuple[object, ...]]: ...
    def _repr_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def _latex_element(self, x: OreModuleElement[_Scalar]) -> str: ...
    def over_fraction_field(self) -> OreQuotientModule[RingElement]: ...
    def cover(self) -> OreModule[_Scalar]: ...
    def covers(self) -> list[OreModule[_Scalar]]: ...
    def relations(
        self,
        names: OreModuleNames = ...,
    ) -> OreSubmodule[_Scalar]: ...
    def rename_basis(
        self,
        names: OreModuleNames,
        coerce: bool = ...,
    ) -> OreQuotientModule[_Scalar]: ...
    def projection_morphism(self) -> OreModuleMorphism[_Scalar]: ...
    def morphism_quotient(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def morphism_modulo(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def _hom_change_domain(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...
    def _hom_change_codomain(
        self,
        f: OreModuleMorphism[_Scalar],
    ) -> OreModuleMorphism[_Scalar]: ...


from sage.modules.free_module_homspace import FreeModuleHomspace
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.modules.ore_module_homspace import OreModule_homspace
from sage.modules.ore_module_morphism import OreModuleMorphism
