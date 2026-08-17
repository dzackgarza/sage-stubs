from collections.abc import Callable

from sage.rings.integer import Integer
from sage.rings.padics.pow_computer import PowComputer_class
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import (
    Polynomial,
    Polynomial_generic_dense,
)
from sage.structure.element import Element
from sage.structure.factory import FactoryArgument
from sage.structure.parent import ElementConstructorInput

class PowComputer_relative(PowComputer_class):
    def __init__(
        self,
        prime: Integer,
        cache_limit: int,
        prec_cap: int,
        ram_prec_cap: int,
        in_field: bool,
        poly: Polynomial | None = None,
        shift_seed: Element | None = None,
    ) -> None: ...
    def __reduce__(
        self,
    ) -> tuple[Callable[..., PowComputer_class], tuple[FactoryArgument, ...]]: ...
    def _repr_(self) -> str: ...
    def polynomial(
        self, n: int | None = None, var: str = "x"
    ) -> Polynomial_generic_dense: ...

class PowComputer_relative_eis(PowComputer_relative):
    def __init__(
        self,
        prime: Integer,
        cache_limit: int,
        prec_cap: int,
        ram_prec_cap: int,
        in_field: bool,
        poly: Polynomial | None = None,
        shift_seed: Element | None = None,
    ) -> None: ...
    def invert(
        self, a: Polynomial_generic_dense, prec: int
    ) -> Polynomial_generic_dense: ...
    def px_pow(self, r: int) -> Polynomial_generic_dense: ...
    def pxe_pow(self, r: int) -> Polynomial_generic_dense: ...
    def uniformizer_pow(self, r: int) -> Polynomial_generic_dense: ...

def PowComputer_relative_maker(
    prime: int | Integer,
    cache_limit: ElementConstructorInput,
    prec_cap: ElementConstructorInput,
    ram_prec_cap: ElementConstructorInput,
    in_field: ElementConstructorInput,
    poly: Polynomial | MPolynomial,
    shift_seed: ElementConstructorInput,
    prec_type: ElementConstructorInput,
) -> PowComputer_class: ...
