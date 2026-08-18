from collections.abc import Iterable, Sequence
from typing import Generic, Self, TypeVar

from sage.categories.category import Category
from sage.combinat.free_module import CombinatorialFreeModule
from sage.modules.free_module import FreeModule_ambient
from sage.modules.fp_graded.free_element import FreeGradedModuleElement
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import ElementConstructorInput, RingElement
from sage.structure.parent import Parent

_AlgebraElement = TypeVar(
    "_AlgebraElement",
    bound=RingElement,
    default=RingElement,
)
_NewAlgebraElement = TypeVar("_NewAlgebraElement", bound=RingElement)

type GeneratorDegree = int | Integer
type GeneratorNames = str | Sequence[str] | None

class FreeGradedModule(CombinatorialFreeModule, Generic[_AlgebraElement]):
    Element: type[FreeGradedModuleElement[int, _AlgebraElement]]

    @staticmethod
    def __classcall__(
        class_: type[FreeGradedModule[_AlgebraElement]],
        algebra: Parent[_AlgebraElement],
        generator_degrees: Iterable[GeneratorDegree],
        category: Category | None = ...,
        names: GeneratorNames = ...,
        prefix: str | None = ...,
        **kwds: object,
    ) -> FreeGradedModule[_AlgebraElement]: ...
    def __init__(
        self,
        algebra: Parent[_AlgebraElement],
        generator_degrees: tuple[GeneratorDegree, ...],
        category: Category,
        names: tuple[str, ...] | None = ...,
        **kwds: object,
    ) -> None: ...
    def base_ring(self) -> Parent[_AlgebraElement]: ...
    def change_ring(
        self,
        algebra: Parent[_NewAlgebraElement],
    ) -> FreeGradedModule[_NewAlgebraElement]: ...
    def _repr_(self) -> str: ...
    def generator_degrees(self) -> tuple[GeneratorDegree, ...]: ...
    def is_trivial(self) -> bool: ...
    def connectivity(self) -> GeneratorDegree | PlusInfinity: ...
    def _element_constructor_(
        self,
        coefficients: FreeGradedModuleElement[int, _AlgebraElement]
        | Sequence[ElementConstructorInput]
        | int,
    ) -> FreeGradedModuleElement[int, _AlgebraElement]: ...
    def an_element(
        self,
        n: GeneratorDegree | None = ...,
    ) -> FreeGradedModuleElement[int, _AlgebraElement]: ...
    def basis_elements(
        self,
        n: GeneratorDegree,
    ) -> tuple[FreeGradedModuleElement[int, _AlgebraElement], ...]: ...
    def element_from_coordinates(
        self,
        coordinates: Sequence[RingElement],
        n: GeneratorDegree,
    ) -> FreeGradedModuleElement[int, _AlgebraElement]: ...
    def vector_presentation(
        self,
        n: GeneratorDegree,
    ) -> FreeModule_ambient[RingElement]: ...
    __getitem__ = vector_presentation
    def generator(
        self,
        index: int | Integer,
    ) -> FreeGradedModuleElement[int, _AlgebraElement]: ...
    gen = generator
    def generators(self) -> tuple[FreeGradedModuleElement[int, _AlgebraElement], ...]: ...
    gens = generators
    def _Hom_(
        self,
        Y: FreeGradedModule[_AlgebraElement] | FPModule[_AlgebraElement],
        category: Category | None,
    ) -> FreeGradedModuleHomspace[_AlgebraElement]: ...
    def suspension(self, t: GeneratorDegree) -> FreeGradedModule[_AlgebraElement]: ...
    def has_relations(self) -> bool: ...
    def relations(self) -> tuple[()]: ...
    def resolution(
        self,
        k: int,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> list[FPModuleMorphism[_AlgebraElement]]: ...
    def minimal_presentation(
        self,
        top_dim: GeneratorDegree | None = ...,
        verbose: bool = ...,
    ) -> FPModuleMorphism[_AlgebraElement]: ...

from sage.modules.fp_graded.free_homspace import FreeGradedModuleHomspace
from sage.modules.fp_graded.module import FPModule
from sage.modules.fp_graded.morphism import FPModuleMorphism
