import builtins

from sage.rings.finite_rings.finite_field_prime_modn import FiniteField_prime_modn
from sage.rings.finite_rings.integer_mod import IntegerMod_abstract

class _SageObject: ...

class FiniteFieldDiffieHellman:
    def __init__(
        self,
        p: builtins.int,
        generator: builtins.object,
        proof: builtins.bool | None = ...,
    ) -> None: ...
    def secret_key(self) -> IntegerMod_abstract: ...
    def public_key(self, secret_key: builtins.object) -> IntegerMod_abstract: ...
    def compute_shared_secret(
        self, secret_key: builtins.object, public_key: builtins.object
    ) -> IntegerMod_abstract: ...
    def parameters(self) -> tuple[FiniteField_prime_modn, IntegerMod_abstract]: ...
