from sage.crypto.public_key.key_exchange.key_exchange_base import (
    CommutativeKeyExchangeBase,
)
from sage.rings.finite_rings.finite_field_prime_modn import (
    FiniteField_prime_modn,
)
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract
from sage.rings.integer import Integer


class FiniteFieldDiffieHellman(
    CommutativeKeyExchangeBase[
        IntegerMod_abstract,
        IntegerMod_abstract,
        IntegerMod_abstract,
    ],
):
    def __init__(
        self,
        p: int | Integer,
        generator: int | Integer | IntegerMod_abstract,
        proof: bool | None = ...,
    ) -> None: ...
    def secret_key(self) -> IntegerMod_abstract: ...
    def public_key(
        self,
        secret_key: int | Integer | IntegerMod_abstract,
    ) -> IntegerMod_abstract: ...
    def compute_shared_secret(
        self,
        secret_key: int | Integer | IntegerMod_abstract,
        public_key: int | Integer | IntegerMod_abstract,
    ) -> IntegerMod_abstract: ...
    def parameters(
        self,
    ) -> tuple[FiniteField_prime_modn, IntegerMod_abstract]: ...
