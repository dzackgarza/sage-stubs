from collections.abc import Callable

from sage.rings.integer import Integer
from sage.rings.padics.pow_computer import PowComputer_class
from sage.rings.polynomial.multi_polynomial import MPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.element import Element
from sage.structure.factory import FactoryArgument
from sage.structure.parent import ElementConstructorInput

class PowComputer_flint(PowComputer_class):
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
    def polynomial(self, n: int | None = None, var: str = "x") -> Polynomial: ...

class PowComputer_flint_1step(PowComputer_flint):
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
    def _repr_(self) -> str: ...
    def __richcmp__(self, other: PowComputer_class, op: int) -> bool: ...
    def polynomial(self, _n: int | None = None, var: str = "x") -> Polynomial: ...

class PowComputer_flint_unram(PowComputer_flint_1step):
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

class PowComputer_flint_eis(PowComputer_flint_1step):
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

def PowComputer_flint_maker(
    prime: int | Integer,
    cache_limit: ElementConstructorInput,
    prec_cap: ElementConstructorInput,
    ram_prec_cap: ElementConstructorInput,
    in_field: ElementConstructorInput,
    poly: Polynomial | MPolynomial,
    prec_type: ElementConstructorInput,
) -> PowComputer_class: ...
