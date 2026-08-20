from __future__ import annotations

from typing import Generic, TypeVar

from sage.structure.element import Element
from sage.structure.parent import Parent

_Plaintext = TypeVar("_Plaintext", bound=Element, default=Element)
_Ciphertext = TypeVar("_Ciphertext", bound=Element, default=Element)
_Key = TypeVar("_Key")
_Message = TypeVar("_Message", bound=Element)


class Cipher(
    Element,
    Generic[_Plaintext, _Ciphertext, _Key],
):
    def __init__(
        self,
        parent: Cryptosystem[_Plaintext, _Ciphertext, _Key],
        key: _Key,
    ) -> None: ...
    def parent(self) -> Cryptosystem[_Plaintext, _Ciphertext, _Key]: ...
    def __eq__(self, right: object) -> bool: ...
    def _repr_(self) -> str: ...
    def key(self) -> _Key: ...
    def domain(self) -> Parent[_Plaintext]: ...
    def codomain(self) -> Parent[_Ciphertext]: ...


class SymmetricKeyCipher(
    Cipher[_Message, _Message, _Key],
    Generic[_Message, _Key],
):
    def __init__(
        self,
        parent: SymmetricKeyCryptosystem[_Message, _Key],
        key: _Key,
    ) -> None: ...
    def parent(self) -> SymmetricKeyCryptosystem[_Message, _Key]: ...


class PublicKeyCipher(
    Cipher[_Plaintext, _Ciphertext, _Key],
    Generic[_Plaintext, _Ciphertext, _Key],
):
    def __init__(
        self,
        parent: PublicKeyCryptosystem[_Plaintext, _Ciphertext, _Key],
        key: _Key,
        public: bool = ...,
    ) -> None: ...
    def parent(self) -> PublicKeyCryptosystem[_Plaintext, _Ciphertext, _Key]: ...


from sage.crypto.cryptosystem import (
    Cryptosystem,
    PublicKeyCryptosystem,
    SymmetricKeyCryptosystem,
)
