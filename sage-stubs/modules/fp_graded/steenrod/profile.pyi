from collections.abc import Iterable
from typing import Literal, overload

from sage.rings.integer import Integer
from sage.structure.element import RingElement

type ProfileEntry = int | Integer
type ModTwoProfile = tuple[ProfileEntry, ...]
type OddPrimaryProfile = tuple[ModTwoProfile, ModTwoProfile]
type SteenrodProfile = ModTwoProfile | OddPrimaryProfile
type ModTwoSupport = Iterable[ProfileEntry]
type OddPrimarySupport = tuple[
    Iterable[ProfileEntry],
    Iterable[ProfileEntry],
]
type SteenrodSupport = ModTwoSupport | OddPrimarySupport
type SteenrodProfileInput = RingElement | SteenrodSupport

@overload
def profile_elt(
    elt: RingElement | ModTwoSupport,
    char: Literal[2] = ...,
) -> ModTwoProfile: ...
@overload
def profile_elt(
    elt: SteenrodProfileInput,
    char: int | Integer,
) -> SteenrodProfile: ...

@overload
def enveloping_profile_elements(
    alist: Iterable[RingElement | ModTwoSupport],
    char: Literal[2] = ...,
) -> ModTwoProfile: ...
@overload
def enveloping_profile_elements(
    alist: Iterable[SteenrodProfileInput],
    char: int | Integer,
) -> SteenrodProfile: ...

@overload
def find_min_profile(
    prof: ModTwoSupport,
    char: Literal[2] = ...,
) -> ModTwoProfile: ...
@overload
def find_min_profile(
    prof: SteenrodSupport,
    char: int | Integer,
) -> SteenrodProfile: ...
