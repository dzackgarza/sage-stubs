from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from sage.monoids.free_monoid import FreeMonoid
from sage.monoids.string_monoid_element import StringMonoidData, StringMonoidElement
from sage.rings.integer import Integer
from sage.rings.real_mpfr import RealNumber


type CharacteristicFrequencyTable = Literal["beker_piper", "lewand"]


class StringMonoid_class(FreeMonoid):
    Element: type[StringMonoidElement]
    element_class: type[StringMonoidElement]

    def __init__(
        self,
        n: int | Integer,
        alphabet: Sequence[str] = ...,
    ) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    def alphabet(self) -> tuple[str, ...]: ...
    def one(self) -> StringMonoidElement: ...
    def gen(self, i: int | Integer = ...) -> StringMonoidElement: ...
    def gens(self) -> tuple[StringMonoidElement, ...]: ...


class BinaryStringMonoid(StringMonoid_class):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(
        self,
        x: StringMonoidData | StringMonoidElement,
        check: bool = ...,
    ) -> StringMonoidElement: ...
    def encoding(
        self,
        S: str,
        padic: bool = ...,
    ) -> StringMonoidElement: ...


BinaryStrings = BinaryStringMonoid


class OctalStringMonoid(StringMonoid_class):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(
        self,
        x: StringMonoidData | StringMonoidElement,
        check: bool = ...,
    ) -> StringMonoidElement: ...


OctalStrings = OctalStringMonoid


class HexadecimalStringMonoid(StringMonoid_class):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(
        self,
        x: StringMonoidData | StringMonoidElement,
        check: bool = ...,
    ) -> StringMonoidElement: ...
    def encoding(
        self,
        S: str,
        padic: bool = ...,
    ) -> StringMonoidElement: ...


HexadecimalStrings = HexadecimalStringMonoid


class Radix64StringMonoid(StringMonoid_class):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(
        self,
        x: StringMonoidData | StringMonoidElement,
        check: bool = ...,
    ) -> StringMonoidElement: ...


Radix64Strings = Radix64StringMonoid


class AlphabeticStringMonoid(StringMonoid_class):
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __call__(
        self,
        x: StringMonoidData | StringMonoidElement,
        check: bool = ...,
    ) -> StringMonoidElement: ...
    def characteristic_frequency(
        self,
        table_name: CharacteristicFrequencyTable = ...,
    ) -> dict[str, RealNumber]: ...
    def encoding(self, S: str) -> StringMonoidElement: ...


AlphabeticStrings = AlphabeticStringMonoid
