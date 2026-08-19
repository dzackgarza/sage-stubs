from collections.abc import Sequence
from typing import Literal

from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.integer import Integer

type IntegerTuple = tuple[int | Integer, ...]
type OddMilnorMonomial = tuple[IntegerTuple, IntegerTuple]
type SteenrodCoefficient = int | Integer | FiniteRingElement

def milnor_multiplication(
    r: IntegerTuple,
    s: IntegerTuple,
) -> dict[IntegerTuple, Literal[1]]: ...
def multinomial(
    values: Sequence[int | Integer],
) -> int | Integer | None: ...
def milnor_multiplication_odd(
    m1: OddMilnorMonomial,
    m2: OddMilnorMonomial,
    p: int | Integer,
) -> dict[OddMilnorMonomial, FiniteRingElement]: ...
def multinomial_odd(
    values: Sequence[int | Integer],
    p: int | Integer,
) -> FiniteRingElement: ...
def binomial_mod2(
    n: int | Integer,
    k: int | Integer,
) -> Literal[0, 1]: ...
def binomial_modp(
    n: int | Integer,
    k: int | Integer,
    p: int | Integer,
) -> int | FiniteRingElement: ...
def adem(
    a: int | Integer,
    b: int | Integer,
    c: int | Integer = ...,
    p: int | Integer = ...,
    generic: bool | None = ...,
) -> dict[IntegerTuple, SteenrodCoefficient]: ...
def make_mono_admissible(
    mono: IntegerTuple,
    p: int | Integer = ...,
    generic: bool | None = ...,
) -> dict[IntegerTuple, SteenrodCoefficient]: ...
