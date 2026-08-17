from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Literal

from sage.combinat.words.finite_word import FiniteWord_class
from sage.monoids.free_monoid_element import FreeMonoidElement
from sage.monoids.monoid import Monoid_class
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer
from sage.structure.element import MonoidElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

type FreeMonoidExponent = int | Integer
type FreeMonoidSyllable = tuple[FreeMonoidExponent, FreeMonoidExponent]
type FreeMonoidElementInput = (
    Literal[1]
    | FreeMonoidElement
    | FiniteWord_class
    | list[FreeMonoidSyllable]
)
type FreeMonoidIndexSet = int | Integer | Parent | Iterable[object]
type FreeMonoidNames = str | Sequence[str]


class FreeMonoid(Monoid_class, UniqueRepresentation):
    Element: type[FreeMonoidElement]
    element_class: type[FreeMonoidElement]

    @staticmethod
    def __classcall_private__(
        cls: type[FreeMonoid],
        index_set: FreeMonoidIndexSet | FreeMonoidNames | None = None,
        names: FreeMonoidNames | int | Integer | None = None,
        commutative: bool = False,
        **kwds: bool | str | int | Integer | Parent,
    ) -> FreeMonoid | Parent[MonoidElement]: ...

    def __init__(
        self,
        n: int | Integer,
        names: FreeMonoidNames | None = None,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        x: FreeMonoidElementInput,
        check: bool = True,
    ) -> FreeMonoidElement: ...
    def __call__(
        self,
        x: FreeMonoidElementInput = 1,
        *,
        check: bool = True,
    ) -> FreeMonoidElement: ...
    def __contains__(self, x: object) -> bool: ...
    def gen(self, i: int | Integer = 0) -> FreeMonoidElement: ...
    def gens(self) -> tuple[FreeMonoidElement, ...]: ...
    def gens_dict(self) -> dict[str, FreeMonoidElement]: ...
    def one(self) -> FreeMonoidElement: ...
    def prod(self, factors: Iterable[FreeMonoidElement]) -> FreeMonoidElement: ...
    def ngens(self) -> int: ...
    def variable_names(self) -> tuple[str, ...]: ...
    def cardinality(self) -> Integer | PlusInfinity: ...
