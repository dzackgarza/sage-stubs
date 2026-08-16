from sage.rings.finite_rings.finite_field_base import FiniteField
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.factory import (
    FactoryArgument,
    FactoryCacheKey,
    FactoryExtraArgs,
    FactoryVersion,
    UniqueFactory,
)

class FiniteFieldFactory(UniqueFactory):
    def __init__(self, *args: object, **kwds: object) -> None: ...
    def create_key_and_extra_args(self, *args: FactoryArgument, **kwds: FactoryArgument) -> tuple[FactoryCacheKey, FactoryExtraArgs]: ...
    def create_object(self, version: FactoryVersion, key: FactoryCacheKey, **kwds: FactoryArgument) -> FiniteField: ...

def GF(q: Integer, name: str = 'a', modulus: int | Polynomial | None = None, proof: bool = True, **kwds: FactoryArgument) -> FiniteField: ...
