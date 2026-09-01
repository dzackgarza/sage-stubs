from collections.abc import Callable, Hashable, Iterable, Sequence

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.pushout import ConstructionFunctor
from sage.modules.free_module_element import FreeModuleElement
from sage.modules.module import Module
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.rings.ring import CommutativeRing, Ring
from sage.sets.family import AbstractFamily
from sage.structure.element import (
    CommutativeRingElement,
    ModuleElement,
    RingElement,
)
from sage.structure.indexed_generators import IndexedGenerators
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.typeset.ascii_art import AsciiArt
from sage.typeset.unicode_art import UnicodeArt

type CombinatorialCoercionResult = (
    Callable[[Parent, ModuleElement], ModuleElement]
    | Morphism[ModuleElement, ModuleElement]
    | None
)


class CombinatorialFreeModule(
    UniqueRepresentation,
    Module,
    IndexedGenerators[AbstractFamily],
):
    class Element(ModuleElement): ...

    def __init__(
        self,
        R: CommutativeRing,
        basis_keys: Iterable[Hashable] | AbstractFamily | None = ...,
        element_class: type[ModuleElement] | None = ...,
        category: Category | tuple[Category, ...] | None = ...,
        prefix: str | None = ...,
        names: str | tuple[str, ...] | None = ...,
        **kwds: object,
    ) -> None: ...
    def base_ring(self) -> CommutativeRing: ...
    def _coerce_map_from_(
        self,
        R: Parent | type,
        /,
    ) -> CombinatorialCoercionResult: ...
    def basis(self) -> AbstractFamily: ...
    def an_element(self) -> Element: ...
    def some_elements(self) -> list[Element]: ...
    def ngens(self) -> int: ...
    def gen(self, i: int) -> Element: ...
    def construction(
        self,
    ) -> tuple[ConstructionFunctor, Parent] | None: ...
    def change_ring(self, R: Ring) -> CombinatorialFreeModule: ...
    def dimension(self) -> int | Integer | PlusInfinity: ...
    def is_exact(self) -> bool: ...
    def set_order(self, order: Iterable[Hashable]) -> None: ...
    def get_order(self) -> list[Hashable]: ...
    def get_order_key(self) -> Callable[[Hashable], int]: ...
    def from_vector(
        self,
        vector: FreeModuleElement,
        order: Iterable[Hashable] | None = ...,
        coerce: bool = ...,
    ) -> Element: ...
    def sum(self, iter_of_elements: Iterable[Element]) -> Element: ...
    def linear_combination(
        self,
        iter_of_elements_coeff: Iterable[
            tuple[Element, CommutativeRingElement]
        ],
        factor_on_left: bool = ...,
    ) -> Element: ...
    def term(
        self,
        index: Hashable,
        coeff: CommutativeRingElement = ...,
    ) -> Element: ...
    def monomial(self, index: Hashable) -> Element: ...
    def sum_of_terms(
        self,
        terms: Iterable[tuple[Hashable, CommutativeRingElement]],
        distinct: bool = ...,
    ) -> Element: ...
    def zero(self) -> Element: ...


class CombinatorialFreeModule_Tensor(CombinatorialFreeModule):
    @staticmethod
    def __classcall_private__(
        class_: type[CombinatorialFreeModule_Tensor],
        modules: Sequence[CombinatorialFreeModule],
        **options: object,
    ) -> CombinatorialFreeModule_Tensor: ...
    def __init__(
        self,
        modules: tuple[CombinatorialFreeModule, ...],
        **options: object,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def tensor_factors(self) -> tuple[CombinatorialFreeModule, ...]: ...
    def _ascii_art_term(self, term: Sequence[Hashable]) -> AsciiArt: ...
    def _unicode_art_term(self, term: Sequence[Hashable]) -> UnicodeArt: ...
    def _latex_(self) -> str: ...
    def _repr_term(self, term: Sequence[Hashable]) -> str: ...
    def _latex_term(self, term: Sequence[Hashable]) -> str: ...
    def tensor_constructor(
        self,
        modules: Sequence[CombinatorialFreeModule],
    ) -> Callable[..., CombinatorialFreeModule.Element]: ...
    def _tensor_of_elements(
        self,
        elements: Sequence[CombinatorialFreeModule.Element],
    ) -> CombinatorialFreeModule.Element: ...
    def _coerce_map_from_(
        self,
        R: Parent | type,
        /,
    ) -> CombinatorialCoercionResult: ...
