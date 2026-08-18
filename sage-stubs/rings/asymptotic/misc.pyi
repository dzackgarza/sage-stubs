from collections.abc import Callable, Hashable, Iterable, Mapping
from typing import Never, TypeVar, overload

from sage.categories.category import Category
from sage.rings.asymptotic.asymptotic_ring import AsymptoticExpansion, AsymptoticRing
from sage.structure.element import Element
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.sage_object import SageCoercionAtom, SageObject

_T = TypeVar("_T")
_E = TypeVar("_E", bound=BaseException)
type LocalValue = SageCoercionAtom | Callable[..., SageCoercionAtom]
type SubcategoryMapping = Iterable[tuple[Category, Category, bool]]
type AxiomMapping = Iterable[tuple[str, str, bool]]

def repr_short_to_parent(s: str) -> Parent: ...
def parent_to_repr_short(P: Parent) -> str: ...
def split_str_by_op(
    string: str,
    op: str | None,
    strip_parentheses: bool = ...,
) -> tuple[str, ...]: ...
def repr_op(
    left: object,
    op: str,
    right: object | None = ...,
    latex: bool = ...,
) -> str: ...
def combine_exceptions(e: _E, *f: BaseException) -> _E: ...
def substitute_raise_exception(element: Element, e: BaseException) -> Never: ...
@overload
def bidirectional_merge_overlapping(
    A: list[_T],
    B: list[_T],
    key: Callable[[_T], Hashable] | None = ...,
) -> tuple[list[_T], list[_T]]: ...
@overload
def bidirectional_merge_overlapping(
    A: tuple[_T, ...],
    B: tuple[_T, ...],
    key: Callable[[_T], Hashable] | None = ...,
) -> tuple[tuple[_T, ...], tuple[_T, ...]]: ...
@overload
def bidirectional_merge_sorted(
    A: list[_T],
    B: list[_T],
    key: Callable[[_T], Hashable] | None = ...,
) -> tuple[list[_T], list[_T]]: ...
@overload
def bidirectional_merge_sorted(
    A: tuple[_T, ...],
    B: tuple[_T, ...],
    key: Callable[[_T], Hashable] | None = ...,
) -> tuple[list[_T], list[_T]]: ...
def log_string(element: object, base: object | None = ...) -> str: ...
def strip_symbolic(expression: _T) -> _T | Element: ...

class NotImplementedOZero(NotImplementedError):
    exact_part: AsymptoticExpansion | ElementConstructorInput
    def __init__(
        self,
        asymptotic_ring: AsymptoticRing | None = ...,
        var: str | None = ...,
        exact_part: AsymptoticExpansion | ElementConstructorInput = ...,
    ) -> None: ...

class NotImplementedBZero(NotImplementedError):
    exact_part: AsymptoticExpansion | ElementConstructorInput
    def __init__(
        self,
        asymptotic_ring: AsymptoticRing | None = ...,
        var: str | None = ...,
        exact_part: AsymptoticExpansion | ElementConstructorInput = ...,
    ) -> None: ...

def transform_category(
    category: Category,
    subcategory_mapping: SubcategoryMapping,
    axiom_mapping: AxiomMapping,
    initial_category: Category | None = ...,
) -> Category: ...

class Locals(dict[str, LocalValue]):
    def __getitem__(self, key: str) -> LocalValue: ...
    def __setitem__(self, key: str, value: LocalValue) -> Never: ...
    def __hash__(self) -> int: ...
    def default_locals(self) -> dict[str, Callable[..., SageObject]]: ...

class WithLocals(SageObject):
    @staticmethod
    def _convert_locals_(locals: Mapping[str, LocalValue] | Locals | None) -> Locals: ...
    def locals(self, locals: Mapping[str, LocalValue] | Locals | None = ...) -> Locals: ...
