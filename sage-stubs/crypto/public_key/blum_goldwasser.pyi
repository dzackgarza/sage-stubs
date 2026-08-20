from collections.abc import Sequence

from sage.crypto.cryptosystem import PublicKeyCryptosystem
from sage.monoids.string_monoid_element import StringMonoidElement
from sage.rings.integer import Integer


type Bit = int | Integer
type BitBlock = list[int]
type BlumGoldwasserPlaintext = (
    str
    | StringMonoidElement
    | Sequence[Bit]
)
type BlumGoldwasserCiphertext = tuple[list[BitBlock], Integer]
type BlumGoldwasserPrivateKey = tuple[
    int | Integer,
    int | Integer,
    int | Integer,
    int | Integer,
]
type BlumGoldwasserPublicKey = int | Integer


class BlumGoldwasser(PublicKeyCryptosystem):
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def decrypt(
        self,
        C: BlumGoldwasserCiphertext,
        K: BlumGoldwasserPrivateKey,
    ) -> list[BitBlock]: ...
    def encrypt(
        self,
        P: BlumGoldwasserPlaintext,
        K: BlumGoldwasserPublicKey,
        seed: int | Integer | None = ...,
    ) -> BlumGoldwasserCiphertext: ...
    def private_key(
        self,
        p: int | Integer,
        q: int | Integer,
    ) -> BlumGoldwasserPrivateKey: ...
    def public_key(
        self,
        p: int | Integer,
        q: int | Integer,
    ) -> BlumGoldwasserPublicKey: ...
    def random_key(
        self,
        lbound: int | Integer,
        ubound: int | Integer,
        ntries: int | Integer = ...,
    ) -> tuple[Integer, tuple[Integer, Integer, Integer, Integer]]: ...
