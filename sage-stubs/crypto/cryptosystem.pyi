from __future__ import annotations

from typing import Generic, TypeVar

from sage.rings.integer import Integer
from sage.sets.set import Set_generic
from sage.structure.element import Element
from sage.structure.parent import Parent

_Plaintext = TypeVar("_Plaintext", bound=Element, default=Element)
_Ciphertext = TypeVar("_Ciphertext", bound=Element, default=Element)
_Key = TypeVar("_Key", default=object)
_Message = TypeVar("_Message", bound=Element)


class Cryptosystem(
    Set_generic[Cipher[_Plaintext, _Ciphertext, _Key]],
    Generic[_Plaintext, _Ciphertext, _Key],
):
    def __init__(
        self,
        plaintext_space: Parent[_Plaintext],
        ciphertext_space: Parent[_Ciphertext],
        key_space: Parent | Set_generic,
        block_length: int | Integer = ...,
        period: int | Integer | None = ...,
    ) -> None: ...
    def __eq__(self, right: object) -> bool: ...
    def plaintext_space(self) -> Parent[_Plaintext]: ...
    def cipher_domain(self) -> Parent[_Plaintext]: ...
    def ciphertext_space(self) -> Parent[_Ciphertext]: ...
    def cipher_codomain(self) -> Parent[_Ciphertext]: ...
    def key_space(self) -> Parent | Set_generic: ...
    def block_length(self) -> int | Integer: ...
    def period(self) -> int | Integer: ...


class SymmetricKeyCryptosystem(
    Cryptosystem[_Message, _Message, _Key],
    Generic[_Message, _Key],
):
    def alphabet_size(self) -> int: ...


class PublicKeyCryptosystem(
    Cryptosystem[_Plaintext, _Ciphertext, _Key],
    Generic[_Plaintext, _Ciphertext, _Key],
):
    pass


from sage.crypto.cipher import Cipher
