from collections.abc import Iterable, Sequence
from typing import Generic, TypeVar

from sage.modules.free_module import FreeModule_quotient
from sage.modules.fp_graded.element import FPElement
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.modules.fp_graded.free_module import (
    FreeGradedModule,
    GeneratorDegree,
    GeneratorNames,
)
from sage.modules.module import Module
from sage.rings.infinity import PlusInfinity
from sage.structure.element import ElementConstructorInput, RingElement
from sage.structure.indexed_generators import IndexedGenerators
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)
_NewAlgebraElement = TypeVar("_NewAlgebraElement", bound=RingElement)

type FPRelation = Sequence[ElementConstructorInput]
type FPRelations = Sequence[FPRelation]

class FPModule(
    UniqueRepresentation,
    IndexedGenerators[tuple[int, ...]],
    Module,
    Generic[_AlgebraElement],
):
    Element: type[FPElement[int, _AlgebraElement]]

    @staticmethod
    def __classcall__(
        class_: type[FPModule[_AlgebraElement]],
        arg0: Parent[_AlgebraElement]
        | FreeGradedModule[_AlgebraElement]
        | FreeGradedModuleMorphism[_AlgebraElement],
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
    def defining_homomorphism(self) -> FreeGradedModuleMorphism[_AlgebraElement]: ...
    def change_ring(
        self,
        algebra: Parent[_NewAlgebraElement],
    ) -> FPModule[_NewAlgebraElement]: ...
    def _element_constructor_(
        self,
        x: FPElement[int, _AlgebraElement]
        | FreeGradedModuleElement[int, _AlgebraElement]
        | Sequence[ElementConstructorInput]
        | int,
    ) -> FPElement[int, _AlgebraElement]: ...
    def monomial(self, index: int) -> FPElement[int, _AlgebraElement]: ...
    def zero(self) -> FPElement[int, _AlgebraElement]: ...
    def _repr_(self) -> str: ...
    def connectivity(self) -> GeneratorDegree | PlusInfinity: ...
    def is_trivial(self) -> bool: ...
    def has_relations(self) -> bool: ...
    def an_element(
        self,
        n: GeneratorDegree | None = ...,
    ) -> FPElement[int, _AlgebraElement]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
        verbose: bool = ...,
    ) -> tuple[FPElement[int, _AlgebraElement], ...]: ...
    def element_from_coordinates(
        self,
        coordinates: Sequence[RingElement],
        n: GeneratorDegree,
    ) -> FPElement[int, _AlgebraElement]: ...
    def vector_presentation(
        self,
        n: GeneratorDegree,
        verbose: bool = ...,
    ) -> FreeModule_quotient[RingElement]: ...
    __getitem__ = vector_presentation
    def _Hom_(
        self,
        Y: FPModule[_AlgebraElement] | FreeGradedModule[_AlgebraElement],
        category: object | None,
    ) -> FPModuleHomspace[_AlgebraElement]: ...
    def generator_degrees(self) -> tuple[GeneratorDegree, ...]: ...
    def generators(self) -> tuple[FPElement[int, _AlgebraElement], ...]: ...
    gens = generators
    def generator(self, index: int | GeneratorDegree) -> FPElement[int, _AlgebraElement]: ...
    gen = generator
    def relations(self) -> tuple[FreeGradedModuleElement[int, _AlgebraElement], ...]: ...
    def relation(
        self,
        index: int,
    ) -> FreeGradedModuleElement[int, _AlgebraElement]: ...
    def minimal_presentation(
        self,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def suspension(self, t: GeneratorDegree) -> FPModule[_AlgebraElement]: ...
    def submodule_inclusion(
        self,
        spanning_elements: Iterable[FPElement[int, _AlgebraElement]],
    ) -> FPModuleMorphism[_AlgebraElement]: ...
    def resolution(
        self,
        k: int,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> list[FPModuleMorphism[_AlgebraElement]]: ...

from sage.modules.fp_graded.free_morphism import FreeGradedModuleMorphism
from sage.modules.fp_graded.homspace import FPModuleHomspace
from sage.modules.fp_graded.morphism import FPModuleMorphism
