from collections.abc import Sequence
from typing import Literal, overload

from sage.knots.link import Link, LinkData
from sage.misc.fast_methods import Singleton
from sage.rings.integer import Integer
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.typeset.unicode_art import UnicodeArt


class Knot(Link, Element):
    @staticmethod
    def __classcall_private__(
        self: type[Knot],
        data: LinkData,
        check: bool = ...,
    ) -> Knot: ...
    def __init__(self, data: LinkData, check: bool = ...) -> None: ...
    def _repr_(self) -> str: ...
    def _unicode_art_(self) -> UnicodeArt: ...
    def dt_code(self) -> list[int]: ...
    def arf_invariant(self) -> Literal[0, 1]: ...
    @overload
    def colored_jones_polynomial(
        self,
        N: int | Integer,
        variab: str | None = ...,
        try_inverse: bool = ...,
    ) -> LaurentPolynomial: ...
    @overload
    def colored_jones_polynomial(
        self,
        N: int | Integer,
        variab: Element,
        try_inverse: bool = ...,
    ) -> Element: ...
    def connected_sum(self, other: Knot) -> Knot: ...


class Knots(Singleton, Parent[Knot]):
    Element: type[Knot]
    element_class: type[Knot]

    def __init__(self) -> None: ...
    def _repr_(self) -> str: ...
    def one(self) -> Knot: ...
    def an_element(self) -> Knot: ...
    def from_gauss_code(
        self,
        gauss: Sequence[int | Integer],
    ) -> Knot: ...
    def from_dowker_code(
        self,
        code: Sequence[int | Integer],
    ) -> Knot: ...
    def from_table(
        self,
        n: int | Integer,
        k: int | Integer,
    ) -> Knot: ...
