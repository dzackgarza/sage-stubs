from collections.abc import Iterable

from sage.rings.integer import Integer
from sage.structure.element import RingElement

type ModTwoProfile = tuple[int, ...]
type OddPrimaryProfile = tuple[tuple[int, ...], tuple[int, ...]]
type SteenrodProfile = ModTwoProfile | OddPrimaryProfile
type ModTwoSupport = Iterable[int]
type OddPrimarySupport = tuple[Iterable[int], Iterable[int]]
type SteenrodSupport = ModTwoSupport | OddPrimarySupport
type SteenrodProfileInput = RingElement | SteenrodSupport

def profile_elt(
    elt: SteenrodProfileInput,
    char: int | Integer = ...,
) -> SteenrodProfile: ...
def enveloping_profile_elements(
    alist: Iterable[SteenrodProfileInput],
    char: int | Integer = ...,
) -> SteenrodProfile: ...
def find_min_profile(
    prof: SteenrodSupport,
    char: int | Integer = ...,
) -> SteenrodProfile: ...
