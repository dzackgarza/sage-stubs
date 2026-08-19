from collections.abc import Callable, Iterable, Sequence
from typing import Generic, TypeVar

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.modules.fg_pid.fgp_element import FGP_Element
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.module import Module
from sage.modules.quotient_module import FreeModule_ambient_field_quotient
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import RingElement
from sage.structure.indexed_generators import IndexedGenerators
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.unique_representation import UniqueRepresentation

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)
_NewAlgebraElement = TypeVar("_NewAlgebraElement", bound=RingElement)

type FPRelation = Sequence[ElementConstructorInput]
type FPRelations = Iterable[FPRelation]
type GradedPiecePresentation = (
    FreeModule_ambient_field_quotient[RingElement]
    | FGP_Module_class[RingElement]
)
type GradedPieceElement = (
    FreeModuleElement[RingElement]
    | FGP_Element[RingElement]
)

class FPModule(
    UniqueRepresentation,
    IndexedGenerators[GeneratorIndex],
    Module[_AlgebraElement, FPElement[_AlgebraElement]],
    Generic[_AlgebraElement],
):
    Element: type[FPElement[_AlgebraElement]]

    @staticmethod
    def __classcall__(
        class_: type[FPModule[_AlgebraElement]],
        arg0: Parent[_AlgebraElement]
        | FreeGradedModule[_AlgebraElement]
        | Morphism,
        generator_degrees: Iterable[GeneratorDegree] | None = ...,
        relations: FPRelations = ...,
        names: GeneratorNames = ...,
    ) -> FPModule[_AlgebraElement] | FreeGradedModule[_AlgebraElement]: ...
    def __init__(
        self,
        j: FreeGradedModuleMorphism[_AlgebraElement],
        names: tuple[str, ...] | None,
    ) -> None: ...
    def base_ring(self) -> Parent[_AlgebraElement]: ...
    def defining_homomorphism(
        self,
    ) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def _free_module(self) -> FreeGradedModule[_AlgebraElement]: ...
    def change_ring(
        self,
        algebra: Parent[_NewAlgebraElement],
    ) -> FPModule[_NewAlgebraElement]: ...
    def _from_dict(
        self,
        d: dict[GeneratorIndex, ElementConstructorInput],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> FPElement[_AlgebraElement]: ...
    def _monomial(
        self,
        index: GeneratorIndex,
    ) -> FPElement[_AlgebraElement]: ...
    monomial: Callable[[GeneratorIndex], FPElement[_AlgebraElement]]
    def zero(self) -> FPElement[_AlgebraElement]: ...
    def _element_constructor_(
        self,
        x: FPElement[_AlgebraElement]
        | FreeGradedModuleElement[_AlgebraElement]
        | Iterable[ElementConstructorInput]
        | int,
    ) -> FPElement[_AlgebraElement]: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, m: GeneratorIndex) -> str: ...
    def _latex_term(self, m: GeneratorIndex) -> str: ...
    def connectivity(self) -> GeneratorDegree | PlusInfinity: ...
    def is_trivial(self) -> bool: ...
    def has_relations(self) -> bool: ...
    def an_element(
        self,
        n: GeneratorDegree | None = ...,
    ) -> FPElement[_AlgebraElement]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
        verbose: bool = ...,
    ) -> tuple[FPElement[_AlgebraElement], ...]: ...
    def element_from_coordinates(
        self,
        coordinates: Sequence[ElementConstructorInput],
        n: GeneratorDegree,
    ) -> FPElement[_AlgebraElement]: ...
    def vector_presentation(
        self,
        n: GeneratorDegree,
        verbose: bool = ...,
    ) -> GradedPiecePresentation: ...
    __getitem__ = vector_presentation
    def _Hom_(
        self,
        Y: FPModule[_AlgebraElement] | FreeGradedModule[_AlgebraElement],
        category: Category | None,
    ) -> FPModuleHomspace[_AlgebraElement]: ...
    def generator_degrees(self) -> tuple[GeneratorDegree, ...]: ...
    def generators(self) -> tuple[FPElement[_AlgebraElement], ...]: ...
    gens = generators
    def generator(
        self,
        index: int | Integer,
    ) -> FPElement[_AlgebraElement]: ...
    gen = generator
    def relations(
        self,
    ) -> tuple[FreeGradedModuleElement[_AlgebraElement], ...]: ...
    def relation(
        self,
        index: int | Integer,
    ) -> FreeGradedModuleElement[_AlgebraElement]: ...
    def minimal_presentation(
        self,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def suspension(
        self,
        t: GeneratorDegree,
    ) -> FPModule[_AlgebraElement]: ...
    def submodule_inclusion(
        self,
        spanning_elements: Iterable[FPElement[_AlgebraElement]],
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def resolution(
        self,
        k: int,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> list[FreeGradedModuleMorphism[_AlgebraElement]]: ...

from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import (
    FreeGradedModule,
    GeneratorDegree,
    GeneratorIndex,
    GeneratorNames,
)
from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.homspace import FPModuleHomspace
from sage.modules.fp_graded.morphism import FPModuleMorphism
