from typing import Self

from sage.crypto.public_key.key_exchange.key_exchange_base import KeyExchangeBase
from sage.rings.finite_rings.element_base import FinitePolyExtElement
from sage.rings.integer import Integer
from sage.schemes.elliptic_curves.ell_finite_field import (
    EllipticCurve_finite_field,
)
from sage.schemes.elliptic_curves.ell_point import (
    EllipticCurvePoint_finite_field,
)
from sage.schemes.elliptic_curves.hom_composite import (
    EllipticCurveHom_composite,
)


type SecretKeySIDH = int | Integer
type PublicKeySIDH = tuple[
    EllipticCurve_finite_field,
    EllipticCurvePoint_finite_field,
    EllipticCurvePoint_finite_field,
]
type SIDHParameters = tuple[
    Integer,
    EllipticCurve_finite_field,
    EllipticCurvePoint_finite_field,
    EllipticCurvePoint_finite_field,
    EllipticCurvePoint_finite_field,
    EllipticCurvePoint_finite_field,
]


class SIDH(
    KeyExchangeBase[
        Integer,
        PublicKeySIDH,
        Integer,
        PublicKeySIDH,
        FinitePolyExtElement,
    ],
):
    def __init__(
        self,
        E: EllipticCurve_finite_field,
        PA: EllipticCurvePoint_finite_field,
        QA: EllipticCurvePoint_finite_field,
        PB: EllipticCurvePoint_finite_field,
        QB: EllipticCurvePoint_finite_field,
    ) -> None: ...
    @classmethod
    def parameter_set_from_prime(
        cls,
        prime: int | Integer,
    ) -> Self: ...
    @classmethod
    def named_parameter_set(cls, name: str) -> Self: ...
    def parameters(self) -> SIDHParameters: ...
    def alice_secret_key(self) -> Integer: ...
    def bob_secret_key(self) -> Integer: ...
    def alice_public_key(
        self,
        alice_secret_key: SecretKeySIDH,
    ) -> PublicKeySIDH: ...
    def bob_public_key(
        self,
        bob_secret_key: SecretKeySIDH,
    ) -> PublicKeySIDH: ...
    def alice_compute_shared_secret(
        self,
        alice_secret_key: SecretKeySIDH,
        bob_public_key: PublicKeySIDH,
    ) -> FinitePolyExtElement: ...
    def bob_compute_shared_secret(
        self,
        bob_secret_key: SecretKeySIDH,
        alice_public_key: PublicKeySIDH,
    ) -> FinitePolyExtElement: ...
    def secret_isogeny_path(
        self,
        start_curve: EllipticCurve_finite_field,
        secret_key: SecretKeySIDH,
        P: EllipticCurvePoint_finite_field,
        Q: EllipticCurvePoint_finite_field,
    ) -> tuple[EllipticCurveHom_composite, list[Integer]]: ...
