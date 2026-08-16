from collections.abc import Callable, Hashable, Iterable, MutableMapping, Sequence
from typing import Generic, TypeVar, overload

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.sets_cat import Sets
from sage.rings.integer import Integer
from sage.structure.category_object import CategoryObject
from sage.structure.element import Element, RingElement

type ParentCallInput = object
type ElementConstructorInput = object
type MembershipInput = object
type SetObjectInput = CategoryObject[Element] | Iterable[Hashable] | None
type AlgebraPrintOption = (
    str
    | bool
    | tuple[str, str]
    | list[str]
    | dict[Hashable, str]
    | Sequence[str]
    | Callable[[Element], Hashable]
    | None
)

_ElementT = TypeVar("_ElementT", bound=Element, default=Element)

class Parent(CategoryObject[_ElementT], Generic[_ElementT]):
    element_class: type[_ElementT]

    def __init__(
        self,
        base: Parent[Element] | None = ...,
        *,
        category: Category | Sequence[Category] | None = ...,
        names: str | tuple[str, ...] | None = ...,
        normalize: bool = ...,
        facade: Parent[Element] | tuple[Parent[Element], ...] | bool | None = ...,
    ) -> None: ...
    @overload
    def Hom[CodomainElementT: Element](
        self,
        codomain: Parent[CodomainElementT],
        category: Sets,
    ) -> Homset[
        SetMorphism[_ElementT, CodomainElementT],
        _ElementT,
        CodomainElementT,
    ]: ...
    @overload
    def Hom[CodomainElementT: Element](
        self,
        codomain: Parent[CodomainElementT],
        category: Category | None = ...,
    ) -> Homset[Map[_ElementT, CodomainElementT], _ElementT, CodomainElementT]: ...
    def _refine_category_(self, category: Category | Sequence[Category]) -> None: ...
    def _init_category_(self, category: Category | Sequence[Category]) -> None: ...
    def _unset_category(self) -> None: ...
    def category(self) -> Category: ...
    def _repr_option(self, key: str) -> bool: ...
    def _test_not_implemented_methods(
        self,
        **options: bool | int | str | None,
    ) -> None: ...
    def variable_names(self) -> tuple[str, ...]: ...
    def _first_ngens(self, n: int | Integer) -> tuple[_ElementT, ...]: ...
    def inject_variables(
        self,
        scope: MutableMapping[str, _ElementT] | None = ...,
        verbose: bool = ...,
    ) -> None: ...
    def __call__(
        self,
        x: object = ...,
        *args: object,
        **kwds: object,
    ) -> _ElementT: ...
    def an_element(self) -> _ElementT: ...
    def some_elements(self) -> list[_ElementT]: ...
    def structure_morphism(self) -> Morphism[Element, _ElementT]: ...
    def zero(self) -> _ElementT: ...
    def base(self) -> Parent[Element] | None: ...
    def base_ring(self) -> Parent[RingElement] | None: ...
    def algebra(
        self,
        base_ring: Parent[RingElement] | None = ...,
        category: Category | None = ...,
        **kwds: AlgebraPrintOption,
    ) -> Parent[Element]: ...
    def _unset_coercions_used(self) -> None: ...
    def _unset_embedding(self) -> None: ...
    def _is_coercion_cached(self, domain: Parent[Element]) -> bool: ...
    def _is_conversion_cached(self, domain: Parent[Element]) -> bool: ...
    def _remove_from_coerce_cache(self, domain: Parent[Element]) -> None: ...
    def register_coercion[SourceElementT: Element](
        self,
        morphism: Map[SourceElementT, _ElementT]
        | Parent[SourceElementT]
        | type[SourceElementT],
    ) -> None: ...
    def register_conversion[SourceElementT: Element](
        self,
        morphism: Map[SourceElementT, _ElementT]
        | Parent[SourceElementT]
        | type[SourceElementT],
    ) -> None: ...
    def register_embedding[CodomainElementT: Element](
        self,
        embedding: Map[_ElementT, CodomainElementT] | Parent[CodomainElementT],
    ) -> None: ...
    def coerce_embedding(self) -> Map[_ElementT, Element] | None: ...
    def _generic_coerce_map[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
    ) -> Map[SourceElementT, _ElementT]: ...
    def _generic_convert_map[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
        category: Category | None = ...,
    ) -> Map[SourceElementT, _ElementT]: ...
    def _convert_method_map[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
        method_name: str | None = ...,
    ) -> Map[SourceElementT, _ElementT] | None: ...
    def convert_method_map[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
        method_name: str,
    ) -> Map[SourceElementT, _ElementT] | None: ...
    def has_coerce_map_from(self, source: Parent[Element]) -> bool: ...
    def coerce_map_from[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
    ) -> Morphism[SourceElementT, _ElementT] | None: ...
    def discover_coerce_map_from[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
    ) -> Map[SourceElementT, _ElementT] | None: ...
    def convert_map_from[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
    ) -> Map[SourceElementT, _ElementT] | None: ...
    def discover_convert_map_from[SourceElementT: Element](
        self,
        source: Parent[SourceElementT],
    ) -> Map[SourceElementT, _ElementT] | None: ...
    def is_exact(self) -> bool: ...
    def _is_numerical(self) -> bool: ...
    def _is_real_numerical(self) -> bool: ...
    def __contains__(self, x: object) -> bool: ...

class Set_generic(Parent[_ElementT], Generic[_ElementT]):
    def object(self) -> Set_generic[_ElementT] | SetObjectInput: ...
    def __bool__(self) -> bool: ...
