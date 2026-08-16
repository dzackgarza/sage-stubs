import builtins
from typing import Self

from sage.rings.integer import Integer
from sage.schemes.elliptic_curves.ell_finite_field import EllipticCurve_finite_field
from sage.schemes.elliptic_curves.hom_composite import EllipticCurveHom_composite

class _SageObject: ...

class SIDH:
    def __init__(
        self,
        E: builtins.object,
        PA: builtins.object,
        QA: builtins.object,
        PB: builtins.object,
        QB: builtins.object,
    ) -> None: ...
    @classmethod
    def parameter_set_from_prime(cls, prime: builtins.object) -> Self: ...
    @classmethod
    def named_parameter_set(cls, name: builtins.str) -> Self: ...
    def parameters(
        self,
    ) -> tuple[
        Integer,
        EllipticCurve_finite_field,
        EllipticCurvePoint_finite_field,
        EllipticCurvePoint_finite_field,
        EllipticCurvePoint_finite_field,
        EllipticCurvePoint_finite_field,
    ]: ...
    def alice_secret_key(self) -> Integer: ...
    def bob_secret_key(self) -> Integer: ...
    def alice_public_key(self, alice_secret_key: builtins.object) -> PublicKeySIDH: ...
    def bob_public_key(self, bob_secret_key: builtins.object) -> PublicKeySIDH: ...
    def alice_compute_shared_secret(
        self, alice_secret_key: builtins.object, bob_public_key: builtins.object
    ) -> Integer: ...
    def bob_compute_shared_secret(
        self, bob_secret_key: builtins.object, alice_public_key: builtins.object
    ) -> Integer: ...
    def secret_isogeny_path(
        self,
        start_curve: builtins.object,
        secret_key: builtins.object,
        P: builtins.int,
        Q: builtins.int,
    ) -> tuple[EllipticCurveHom_composite, list[Integer]]: ...
