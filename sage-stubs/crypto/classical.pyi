from __future__ import annotations

from collections.abc import Sequence
from typing import Literal, overload

from sage.crypto.cryptosystem import SymmetricKeyCryptosystem
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.matrix.matrix import Matrix
from sage.matrix.matrix_space import MatrixSpace
from sage.monoids.string_monoid import AlphabeticStringMonoid, StringMonoid_class
from sage.monoids.string_monoid_element import StringMonoidElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput


type AffineKey = tuple[int | Integer, int | Integer]
type ShiftKey = int | Integer
type HillKey = Matrix[IntegerMod_abstract]
type HillKeyInput = (
    HillKey
    | Sequence[ElementConstructorInput]
    | Sequence[Sequence[ElementConstructorInput]]
)
type TranspositionKeyInput = (
    PermutationGroupElement
    | Sequence[int | Integer]
)
type RankingMethod = Literal[
    "none",
    "chisquare",
    "squared_differences",
]
type AffineCandidates = dict[AffineKey, StringMonoidElement]
type AffineRanking = list[tuple[AffineKey, StringMonoidElement]]
type ShiftCandidates = dict[ShiftKey, StringMonoidElement]
type ShiftRanking = list[tuple[ShiftKey, StringMonoidElement]]


class AffineCryptosystem(
    SymmetricKeyCryptosystem[StringMonoidElement, AffineKey],
):
    def __init__(self, A: AlphabeticStringMonoid) -> None: ...
    def __call__(
        self,
        a: int | Integer,
        b: int | Integer,
    ) -> AffineCipher: ...
    def _repr_(self) -> str: ...
    def key_space(
        self,
    ) -> tuple[IntegerModRing_generic, IntegerModRing_generic]: ...
    def rank_by_chi_square(
        self,
        C: StringMonoidElement,
        pdict: AffineCandidates,
    ) -> AffineRanking: ...
    def rank_by_squared_differences(
        self,
        C: StringMonoidElement,
        pdict: AffineCandidates,
    ) -> AffineRanking: ...
    @overload
    def brute_force(
        self,
        C: StringMonoidElement,
        ranking: Literal["none"] = ...,
    ) -> AffineCandidates: ...
    @overload
    def brute_force(
        self,
        C: StringMonoidElement,
        ranking: Literal["chisquare", "squared_differences"],
    ) -> AffineRanking: ...
    @overload
    def brute_force(
        self,
        C: StringMonoidElement,
        ranking: RankingMethod = ...,
    ) -> AffineCandidates | AffineRanking: ...
    def deciphering(
        self,
        a: int | Integer,
        b: int | Integer,
        C: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def enciphering(
        self,
        a: int | Integer,
        b: int | Integer,
        P: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def encoding(self, S: str) -> StringMonoidElement: ...
    def inverse_key(
        self,
        a: int | Integer,
        b: int | Integer,
    ) -> AffineKey: ...
    def random_key(self) -> tuple[Integer, Integer]: ...


class HillCryptosystem(
    SymmetricKeyCryptosystem[StringMonoidElement, HillKey],
):
    def __init__(
        self,
        S: StringMonoid_class,
        m: int | Integer,
    ) -> None: ...
    def __call__(self, A: HillKeyInput) -> HillCipher: ...
    def _repr_(self) -> str: ...
    def key_space(self) -> MatrixSpace[IntegerMod_abstract]: ...
    def block_length(self) -> int: ...
    def random_key(self) -> HillKey: ...
    def inverse_key(self, A: HillKey) -> HillKey: ...
    def encoding(self, M: str) -> StringMonoidElement: ...
    def deciphering(
        self,
        A: HillKey,
        C: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def enciphering(
        self,
        A: HillKey,
        M: StringMonoidElement,
    ) -> StringMonoidElement: ...


class ShiftCryptosystem(
    SymmetricKeyCryptosystem[StringMonoidElement, ShiftKey],
):
    def __init__(self, A: StringMonoid_class) -> None: ...
    def __call__(self, K: ShiftKey) -> ShiftCipher: ...
    def _repr_(self) -> str: ...
    def key_space(self) -> IntegerModRing_generic: ...
    def rank_by_chi_square(
        self,
        C: StringMonoidElement,
        pdict: ShiftCandidates,
    ) -> ShiftRanking: ...
    def rank_by_squared_differences(
        self,
        C: StringMonoidElement,
        pdict: ShiftCandidates,
    ) -> ShiftRanking: ...
    @overload
    def brute_force(
        self,
        C: StringMonoidElement,
        ranking: Literal["none"] = ...,
    ) -> ShiftCandidates: ...
    @overload
    def brute_force(
        self,
        C: StringMonoidElement,
        ranking: Literal["chisquare", "squared_differences"],
    ) -> ShiftRanking: ...
    @overload
    def brute_force(
        self,
        C: StringMonoidElement,
        ranking: RankingMethod = ...,
    ) -> ShiftCandidates | ShiftRanking: ...
    def deciphering(
        self,
        K: ShiftKey,
        C: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def enciphering(
        self,
        K: ShiftKey,
        P: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def encoding(self, S: str) -> StringMonoidElement: ...
    def inverse_key(self, K: ShiftKey) -> Integer: ...
    def random_key(self) -> Integer: ...


class SubstitutionCryptosystem(
    SymmetricKeyCryptosystem[
        StringMonoidElement,
        StringMonoidElement,
    ],
):
    def __init__(self, S: StringMonoid_class) -> None: ...
    def __call__(self, K: StringMonoidElement) -> SubstitutionCipher: ...
    def _repr_(self) -> str: ...
    def key_space(self) -> StringMonoid_class: ...
    def random_key(self) -> StringMonoidElement: ...
    def inverse_key(
        self,
        K: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def encoding(self, M: str) -> StringMonoidElement: ...
    def deciphering(
        self,
        K: StringMonoidElement,
        C: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def enciphering(
        self,
        K: StringMonoidElement,
        M: StringMonoidElement,
    ) -> StringMonoidElement: ...


class TranspositionCryptosystem(
    SymmetricKeyCryptosystem[
        StringMonoidElement,
        PermutationGroupElement,
    ],
):
    def __init__(
        self,
        S: StringMonoid_class,
        n: int | Integer,
    ) -> None: ...
    def __call__(
        self,
        K: TranspositionKeyInput,
    ) -> TranspositionCipher: ...
    def _repr_(self) -> str: ...
    def key_space(self) -> PermutationGroup_generic: ...
    def random_key(self) -> PermutationGroupElement: ...
    def inverse_key(
        self,
        K: TranspositionKeyInput,
        check: bool = ...,
    ) -> PermutationGroupElement: ...
    def encoding(self, M: str) -> StringMonoidElement: ...
    def deciphering(
        self,
        K: TranspositionKeyInput,
        C: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def enciphering(
        self,
        K: TranspositionKeyInput,
        M: StringMonoidElement,
    ) -> StringMonoidElement: ...


class VigenereCryptosystem(
    SymmetricKeyCryptosystem[
        StringMonoidElement,
        StringMonoidElement,
    ],
):
    def __init__(
        self,
        S: StringMonoid_class,
        n: int | Integer,
    ) -> None: ...
    def __call__(self, K: StringMonoidElement) -> VigenereCipher: ...
    def _repr_(self) -> str: ...
    def key_space(self) -> StringMonoid_class: ...
    def period(self) -> int | Integer: ...
    def random_key(self) -> StringMonoidElement: ...
    def inverse_key(
        self,
        K: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def encoding(self, M: str) -> StringMonoidElement: ...
    def deciphering(
        self,
        K: StringMonoidElement,
        C: StringMonoidElement,
    ) -> StringMonoidElement: ...
    def enciphering(
        self,
        K: StringMonoidElement,
        M: StringMonoidElement,
    ) -> StringMonoidElement: ...


from sage.crypto.classical_cipher import (
    AffineCipher,
    HillCipher,
    ShiftCipher,
    SubstitutionCipher,
    TranspositionCipher,
    VigenereCipher,
)
