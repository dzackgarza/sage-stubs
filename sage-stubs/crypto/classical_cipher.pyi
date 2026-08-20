from __future__ import annotations

from typing import Literal

from sage.crypto.cipher import SymmetricKeyCipher
from sage.groups.perm_gps.permgroup_element import PermutationGroupElement
from sage.matrix.matrix import Matrix
from sage.monoids.string_monoid_element import StringMonoidElement
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer


type AffineKey = tuple[int | Integer, int | Integer]
type HillKey = Matrix[IntegerMod_abstract]
type ShiftKey = int | Integer
type TranspositionMode = Literal["ECB"]


class AffineCipher(
    SymmetricKeyCipher[StringMonoidElement, AffineKey],
):
    def __init__(
        self,
        parent: AffineCryptosystem,
        key: AffineKey,
    ) -> None: ...
    def parent(self) -> AffineCryptosystem: ...
    def __eq__(self, other: object) -> bool: ...
    def __call__(self, M: StringMonoidElement) -> StringMonoidElement: ...
    def _repr_(self) -> str: ...


class HillCipher(
    SymmetricKeyCipher[StringMonoidElement, HillKey],
):
    def __init__(
        self,
        parent: HillCryptosystem,
        key: HillKey,
    ) -> None: ...
    def parent(self) -> HillCryptosystem: ...
    def __eq__(self, right: object) -> bool: ...
    def __call__(self, M: StringMonoidElement) -> StringMonoidElement: ...
    def _repr_(self) -> str: ...
    def inverse(self) -> HillCipher: ...


class ShiftCipher(
    SymmetricKeyCipher[StringMonoidElement, ShiftKey],
):
    def __init__(
        self,
        parent: ShiftCryptosystem,
        key: ShiftKey,
    ) -> None: ...
    def parent(self) -> ShiftCryptosystem: ...
    def __eq__(self, other: object) -> bool: ...
    def __call__(self, M: StringMonoidElement) -> StringMonoidElement: ...
    def _repr_(self) -> str: ...


class SubstitutionCipher(
    SymmetricKeyCipher[StringMonoidElement, StringMonoidElement],
):
    def __init__(
        self,
        parent: SubstitutionCryptosystem,
        key: StringMonoidElement,
    ) -> None: ...
    def parent(self) -> SubstitutionCryptosystem: ...
    def __eq__(self, right: object) -> bool: ...
    def __call__(self, M: StringMonoidElement) -> StringMonoidElement: ...
    def _repr_(self) -> str: ...
    def inverse(self) -> SubstitutionCipher: ...


class TranspositionCipher(
    SymmetricKeyCipher[StringMonoidElement, PermutationGroupElement],
):
    def __init__(
        self,
        parent: TranspositionCryptosystem,
        key: PermutationGroupElement,
    ) -> None: ...
    def parent(self) -> TranspositionCryptosystem: ...
    def __call__(
        self,
        M: StringMonoidElement,
        mode: TranspositionMode = ...,
    ) -> StringMonoidElement: ...
    def inverse(self) -> TranspositionCipher: ...


class VigenereCipher(
    SymmetricKeyCipher[StringMonoidElement, StringMonoidElement],
):
    def __init__(
        self,
        parent: VigenereCryptosystem,
        key: StringMonoidElement,
    ) -> None: ...
    def parent(self) -> VigenereCryptosystem: ...
    def __call__(
        self,
        M: StringMonoidElement,
        mode: TranspositionMode = ...,
    ) -> StringMonoidElement: ...
    def inverse(self) -> VigenereCipher: ...


from sage.crypto.classical import (
    AffineCryptosystem,
    HillCryptosystem,
    ShiftCryptosystem,
    SubstitutionCryptosystem,
    TranspositionCryptosystem,
    VigenereCryptosystem,
)
