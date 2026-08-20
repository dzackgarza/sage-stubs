from abc import abstractmethod
from collections.abc import Hashable
from typing import Generic, Self, TypeVar

from sage.structure.sage_object import SageObject

_AliceSecret = TypeVar("_AliceSecret")
_AlicePublic = TypeVar("_AlicePublic")
_BobSecret = TypeVar("_BobSecret")
_BobPublic = TypeVar("_BobPublic")
_Secret = TypeVar("_Secret")
_Public = TypeVar("_Public")
_SharedSecret = TypeVar("_SharedSecret")


class KeyExchangeBase(
    SageObject,
    Generic[
        _AliceSecret,
        _AlicePublic,
        _BobSecret,
        _BobPublic,
        _SharedSecret,
    ],
):
    @abstractmethod
    def alice_secret_key(self) -> _AliceSecret: ...
    @abstractmethod
    def alice_public_key(
        self,
        alice_secret_key: _AliceSecret,
    ) -> _AlicePublic: ...
    @abstractmethod
    def bob_secret_key(self) -> _BobSecret: ...
    @abstractmethod
    def bob_public_key(
        self,
        bob_secret_key: _BobSecret,
    ) -> _BobPublic: ...
    @abstractmethod
    def alice_compute_shared_secret(
        self,
        alice_secret_key: _AliceSecret,
        bob_public_key: _BobPublic,
    ) -> _SharedSecret: ...
    @abstractmethod
    def bob_compute_shared_secret(
        self,
        bob_secret_key: _BobSecret,
        alice_public_key: _AlicePublic,
    ) -> _SharedSecret: ...
    @abstractmethod
    def parameters(self) -> tuple[Hashable, ...]: ...
    def alice_key_pair(self) -> tuple[_AliceSecret, _AlicePublic]: ...
    def bob_key_pair(self) -> tuple[_BobSecret, _BobPublic]: ...
    def do_key_exchange(
        self,
    ) -> tuple[
        _AliceSecret,
        _AlicePublic,
        _BobSecret,
        _BobPublic,
        _SharedSecret,
    ]: ...
    @classmethod
    def named_parameter_set(cls, name: str) -> Self: ...
    def _repr_(self) -> str: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def _test_key_exchange(self, **options: object) -> None: ...


class CommutativeKeyExchangeBase(
    KeyExchangeBase[
        _Secret,
        _Public,
        _Secret,
        _Public,
        _SharedSecret,
    ],
    Generic[_Secret, _Public, _SharedSecret],
):
    @abstractmethod
    def secret_key(self) -> _Secret: ...
    @abstractmethod
    def public_key(self, secret_key: _Secret) -> _Public: ...
    @abstractmethod
    def compute_shared_secret(
        self,
        secret_key: _Secret,
        public_key: _Public,
    ) -> _SharedSecret: ...
    def alice_secret_key(self) -> _Secret: ...
    def alice_public_key(self, alice_secret_key: _Secret) -> _Public: ...
    def bob_secret_key(self) -> _Secret: ...
    def bob_public_key(self, bob_secret_key: _Secret) -> _Public: ...
    def alice_compute_shared_secret(
        self,
        alice_sk: _Secret,
        bob_pk: _Public,
    ) -> _SharedSecret: ...
    def bob_compute_shared_secret(
        self,
        bob_sk: _Secret,
        alice_pk: _Public,
    ) -> _SharedSecret: ...
