from collections.abc import Iterable, Mapping
from typing import Literal, overload

from sage.categories.category import Category
from sage.knots.knot import Knot
from sage.knots.knotinfo import KnotInfoBase, KnotInfoSeries, SymmetryMutant
from sage.knots.link import Link
from sage.monoids.indexed_free_monoid import (
    IndexedFreeAbelianMonoid,
    IndexedFreeAbelianMonoidElement,
    IndexedMonoidInput,
    MonomialFactor,
)
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.sets.family import AbstractFamily


type KnotInfoFactor = tuple[KnotInfoBase, SymmetryMutant]
type FreeKnotInfoInput = (
    IndexedMonoidInput[str]
    | Iterable[MonomialFactor[str]]
    | Mapping[str, int | Integer]
    | KnotInfoFactor
    | Knot
    | Link
)


class FreeKnotInfoMonoidElement(
    IndexedFreeAbelianMonoidElement[str],
):
    def parent(self) -> FreeKnotInfoMonoid: ...
    def as_knot(self) -> Knot: ...
    def to_knotinfo(self) -> list[KnotInfoFactor]: ...


class FreeKnotInfoMonoid(IndexedFreeAbelianMonoid[str]):
    Element: type[FreeKnotInfoMonoidElement]
    element_class: type[FreeKnotInfoMonoidElement]
    _index_dict: dict[str, KnotInfoFactor]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeKnotInfoMonoid],
        max_crossing_number: int | Integer = ...,
        prefix: str | None = ...,
        **kwds: object,
    ) -> FreeKnotInfoMonoid: ...
    def __init__(
        self,
        max_crossing_number: int | Integer,
        category: Category | None = ...,
        prefix: str | None = ...,
        **kwds: object,
    ) -> None: ...
    def _from_knotinfo(
        self,
        knotinfo: KnotInfoBase,
        symmetry_mutant: SymmetryMutant,
    ) -> str: ...
    def _set_index_dictionary(
        self,
        max_crossing_number: int | Integer = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: FreeKnotInfoInput | FreeKnotInfoMonoidElement | None = ...,
    ) -> FreeKnotInfoMonoidElement: ...
    def gen(self, x: str) -> FreeKnotInfoMonoidElement: ...
    def gens(self) -> AbstractFamily: ...
    def one(self) -> FreeKnotInfoMonoidElement: ...
    def _check_elements(
        self,
        knot: Knot,
        elems: tuple[FreeKnotInfoMonoidElement, ...],
    ) -> FreeKnotInfoMonoidElement | None: ...
    def _search_composition(
        self,
        max_cr: int | Integer,
        knot: Knot,
        hpoly: LaurentPolynomial,
    ) -> tuple[FreeKnotInfoMonoidElement, ...]: ...
    def _from_knot(
        self,
        knot: Knot,
    ) -> tuple[FreeKnotInfoMonoidElement, ...]: ...

    @overload
    def from_knot(
        self,
        knot: Knot,
        unique: Literal[True] = ...,
    ) -> FreeKnotInfoMonoidElement: ...
    @overload
    def from_knot(
        self,
        knot: Knot,
        unique: Literal[False],
    ) -> list[FreeKnotInfoMonoidElement]: ...

    def inject_variables(
        self,
        select: KnotInfoBase | KnotInfoSeries | int | Integer | None = ...,
        verbose: bool = ...,
    ) -> None: ...
