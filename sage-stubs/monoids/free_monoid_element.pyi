from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import Literal, Never, Self, overload

from sage.combinat.words.finite_word import FiniteWord_class
from sage.monoids.free_monoid import FreeMonoid, FreeMonoidElementInput
from sage.rings.integer import Integer
from sage.structure.element import MonoidElement


class FreeMonoidElement(MonoidElement):
    _element_list: list[tuple[Integer, Integer]]

    def __init__(
        self,
        F: FreeMonoid,
        x: FreeMonoidElementInput,
        check: bool = True,
    ) -> None: ...
    def parent(self) -> FreeMonoid: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[tuple[FreeMonoidElement, Integer]]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

    @overload
    def __call__(
        self,
        *x: FreeMonoidElement,
        **kwds: FreeMonoidElement,
    ) -> FreeMonoidElement: ...
    @overload
    def __call__[_Evaluation](
        self,
        *x: _Evaluation,
        **kwds: _Evaluation,
    ) -> _Evaluation | FreeMonoidElement: ...

    @overload
    def subs(
        self,
        *x: FreeMonoidElement,
        **kwds: FreeMonoidElement,
    ) -> FreeMonoidElement: ...
    @overload
    def subs[_Evaluation](
        self,
        *x: _Evaluation,
        **kwds: _Evaluation,
    ) -> _Evaluation | FreeMonoidElement: ...

    @overload
    def substitute(
        self,
        *x: FreeMonoidElement,
        **kwds: FreeMonoidElement,
    ) -> FreeMonoidElement: ...
    @overload
    def substitute[_Evaluation](
        self,
        *x: _Evaluation,
        **kwds: _Evaluation,
    ) -> _Evaluation | FreeMonoidElement: ...

    def _mul_(self, y: Self) -> Self: ...
    def __mul__(self, y: Self) -> Self: ...
    def __pow__(self, n: int | Integer) -> Self: ...
    def __invert__(self) -> Never: ...
    def __len__(self) -> int: ...
    def _richcmp_(self, other: Self, op: int) -> bool: ...
    def _acted_upon_(
        self,
        x: int | Integer,
        self_on_left: bool,
    ) -> Self | None: ...
    def is_one(self) -> bool: ...
    def to_word(
        self,
        alph: Sequence[str | FreeMonoidElement] | None = None,
    ) -> FiniteWord_class: ...
    @overload
    def to_list(self, indices: Literal[False] = False) -> list[FreeMonoidElement]: ...
    @overload
    def to_list(self, indices: Literal[True]) -> list[int]: ...
