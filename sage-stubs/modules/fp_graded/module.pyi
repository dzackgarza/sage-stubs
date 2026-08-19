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
_GroundElement = TypeVar(
    "_GroundElement",
    bound=RingElement,
    default=RingElement,
)
_NewAlgebraElement = TypeVar("_NewAlgebraElement", bound=RingElement)

type FPRelation = Sequence[ElementConstructorInput]
type FPRelations = Iterable[FPRelation]
type GradedPiecePresentation[_GroundElement: RingElement] = (
    FreeModule_ambient_field_quotient[_GroundElement]
    | FGP_Module_class[_GroundElement]
)
type GradedPieceElement[_GroundElement: RingElement] = (
    FreeModuleElement[_GroundElement]
    | FGP_Element[_GroundElement]
)

class FPModule(
    UniqueRepresentation,
    IndexedGenerators[GeneratorIndex],
    Module[
        _AlgebraElement,
        FPElement[_AlgebraElement, _GroundElement],
    ],
    Generic[_AlgebraElement, _GroundElement],
):
    Element: type[FPElement[_AlgebraElement, _GroundElement]]

    @staticmethod
    def __classcall__(
        class_: type[FPModule[_AlgebraElement, _GroundElement]],
        arg0: Parent[_AlgebraElement]
        | FreeGradedModule[_AlgebraElement, _GroundElement]
        | Morphism,
        generator_degrees: Iterable[GeneratorDegree] | None = ...,
        relations: FPRelations = ...,
        names: GeneratorNames = ...,
    ) -> (
        FPModule[_AlgebraElement, _GroundElement]
        | FreeGradedModule[_AlgebraElement, _GroundElement]
    ): ...
    def __init__(
        self,
        j: FreeGradedModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ],
        names: tuple[str, ...] | None,
    ) -> None: ...
    def base_ring(self) -> Parent[_AlgebraElement]: ...
    def defining_homomorphism(
        self,
    ) -> FreeGradedModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def _free_module(
        self,
    ) -> FreeGradedModule[_AlgebraElement, _GroundElement]: ...
    def change_ring(
        self,
        algebra: Parent[_NewAlgebraElement],
    ) -> FPModule[_NewAlgebraElement, RingElement]: ...
    def _from_dict(
        self,
        d: dict[GeneratorIndex, ElementConstructorInput],
        coerce: bool = ...,
        remove_zeros: bool = ...,
    ) -> FPElement[_AlgebraElement, _GroundElement]: ...
    def _monomial(
        self,
        index: GeneratorIndex,
    ) -> FPElement[_AlgebraElement, _GroundElement]: ...
    monomial: Callable[
        [GeneratorIndex],
        FPElement[_AlgebraElement, _GroundElement],
    ]
    def zero(self) -> FPElement[_AlgebraElement, _GroundElement]: ...
    def _element_constructor_(
        self,
        x: FPElement[_AlgebraElement, _GroundElement]
        | FreeGradedModuleElement[_AlgebraElement, _GroundElement]
        | Iterable[ElementConstructorInput]
        | int,
    ) -> FPElement[_AlgebraElement, _GroundElement]: ...
    def _repr_(self) -> str: ...
    def _repr_term(self, m: GeneratorIndex) -> str: ...
    def _latex_term(self, m: GeneratorIndex) -> str: ...
    def connectivity(self) -> GeneratorDegree | PlusInfinity: ...
    def is_trivial(self) -> bool: ...
    def has_relations(self) -> bool: ...
    def an_element(
        self,
        n: GeneratorDegree | None = ...,
    ) -> FPElement[_AlgebraElement, _GroundElement]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
        verbose: bool = ...,
    ) -> tuple[FPElement[_AlgebraElement, _GroundElement], ...]: ...
    def element_from_coordinates(
        self,
        coordinates: GradedPieceElement[_GroundElement]
        | Sequence[ElementConstructorInput],
        n: GeneratorDegree,
    ) -> FPElement[_AlgebraElement, _GroundElement]: ...
    def vector_presentation(
        self,
        n: GeneratorDegree,
        verbose: bool = ...,
    ) -> GradedPiecePresentation[_GroundElement]: ...
    __getitem__ = vector_presentation
    def _Hom_(
        self,
        Y: FPModule[_AlgebraElement, _GroundElement]
        | FreeGradedModule[_AlgebraElement, _GroundElement],
        category: Category | None,
    ) -> FPModuleHomspace[_AlgebraElement, _GroundElement]: ...
    def generator_degrees(self) -> tuple[GeneratorDegree, ...]: ...
    def generators(
        self,
    ) -> tuple[FPElement[_AlgebraElement, _GroundElement], ...]: ...
    gens = generators
    def generator(
        self,
        index: int | Integer,
    ) -> FPElement[_AlgebraElement, _GroundElement]: ...
    gen = generator
    def relations(
        self,
    ) -> tuple[
        FreeGradedModuleElement[
            _AlgebraElement,
            _GroundElement,
        ],
        ...,
    ]: ...
    def relation(
        self,
        index: int | Integer,
    ) -> FreeGradedModuleElement[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def minimal_presentation(
        self,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def suspension(
        self,
        t: GeneratorDegree,
    ) -> FPModule[_AlgebraElement, _GroundElement]: ...
    def submodule_inclusion(
        self,
        spanning_elements: Iterable[
            FPElement[_AlgebraElement, _GroundElement]
        ],
    ) -> FPModuleMorphism[
        _AlgebraElement,
        _GroundElement,
    ]: ...
    def resolution(
        self,
        k: int,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> list[
        FreeGradedModuleMorphism[
            _AlgebraElement,
            _GroundElement,
        ]
    ]: ...

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
