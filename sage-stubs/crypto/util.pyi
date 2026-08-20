from collections.abc import Sequence

from sage.monoids.string_monoid_element import StringMonoidElement
from sage.rings.integer import Integer


type Bit = int | Integer
type BitBlock = str | StringMonoidElement | Sequence[Bit]
type ASCIIInput = str | Sequence[str]


def ascii_integer(B: BitBlock) -> int: ...


def ascii_to_bin(A: ASCIIInput) -> StringMonoidElement: ...


def bin_to_ascii(B: BitBlock) -> str: ...


def has_blum_prime(
    lbound: int | Integer,
    ubound: int | Integer,
) -> bool: ...


def is_blum_prime(n: int | Integer) -> bool: ...


def least_significant_bits(
    n: int | Integer,
    k: int | Integer,
) -> list[int]: ...


def random_blum_prime(
    lbound: int | Integer,
    ubound: int | Integer,
    ntries: int | Integer = ...,
) -> Integer: ...
