from collections.abc import Callable, Iterable, Sequence
from typing import Literal, overload

from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer

type SteenrodBasisName = Literal[
    "milnor",
    "serre-cartan",
    "woody",
    "woodz",
    "wall",
    "wall_long",
    "arnona",
    "arnona_long",
    "arnonc",
    "pst_rlex",
    "pst_llex",
    "pst_deg",
    "pst_revz",
    "comm_rlex",
    "comm_llex",
    "comm_deg",
    "comm_revz",
    "comm_rlex_long",
    "comm_llex_long",
    "comm_deg_long",
    "comm_revz_long",
]
type ProfileEntry = int | Integer | PlusInfinity
type ModTwoProfile = tuple[ProfileEntry, ...]
type OddExteriorProfile = tuple[int | Integer, ...]
type OddPrimaryProfile = tuple[ModTwoProfile, OddExteriorProfile]
type ProfileFunction = Callable[[int], ProfileEntry]
type OddExteriorProfileFunction = Callable[[int], int | Integer]
type ModTwoProfileInput = (
    Sequence[ProfileEntry]
    | ProfileFunction
    | PlusInfinity
    | None
)
type OddPrimaryProfileInput = (
    tuple[
        Sequence[ProfileEntry] | ProfileFunction,
        Sequence[int | Integer] | OddExteriorProfileFunction,
    ]
    | PlusInfinity
    | None
)
type SteenrodProfile = ModTwoProfile | OddPrimaryProfile
type SteenrodProfileInput = ModTwoProfileInput | OddPrimaryProfileInput
type TruncationType = Literal[0] | PlusInfinity
type TruncationInput = (
    Literal[0, "auto", "zero", "infinity"]
    | PlusInfinity
)
type IntegerTuple = tuple[int | Integer, ...]
type IntegerPair = tuple[int | Integer, int | Integer]
type PairMonomial = tuple[IntegerPair, ...]
type GenericMilnorMonomial = tuple[IntegerTuple, IntegerTuple]
type GenericAtomicPower = tuple[IntegerPair, int | Integer]
type GenericAtomicMonomial = tuple[
    IntegerTuple,
    tuple[GenericAtomicPower, ...],
]

def get_basis_name(
    basis: str,
    p: int | Integer,
    generic: bool | None = ...,
) -> SteenrodBasisName: ...

@overload
def is_valid_profile(
    profile: Sequence[ProfileEntry],
    truncation_type: TruncationType,
    p: Literal[2] = ...,
    generic: Literal[False] | None = ...,
) -> bool: ...
@overload
def is_valid_profile(
    profile: OddPrimaryProfile,
    truncation_type: TruncationType,
    p: int | Integer = ...,
    generic: Literal[True] | None = ...,
) -> bool: ...
@overload
def is_valid_profile(
    profile: SteenrodProfile,
    truncation_type: TruncationType,
    p: int | Integer = ...,
    generic: bool | None = ...,
) -> bool: ...

@overload
def normalize_profile(
    profile: ModTwoProfileInput,
    precision: int | Integer | None = ...,
    truncation_type: TruncationInput = ...,
    p: Literal[2] = ...,
    generic: Literal[False] | None = ...,
) -> tuple[ModTwoProfile, TruncationType]: ...
@overload
def normalize_profile(
    profile: OddPrimaryProfileInput,
    precision: int | Integer | None = ...,
    truncation_type: TruncationInput = ...,
    p: int | Integer = ...,
    generic: Literal[True] | None = ...,
) -> tuple[OddPrimaryProfile, TruncationType]: ...
@overload
def normalize_profile(
    profile: SteenrodProfileInput,
    precision: int | Integer | None = ...,
    truncation_type: TruncationInput = ...,
    p: int | Integer = ...,
    generic: bool | None = ...,
) -> tuple[SteenrodProfile, TruncationType]: ...

def milnor_mono_to_string(
    mono: IntegerTuple | GenericMilnorMonomial,
    latex: bool = ...,
    generic: bool = ...,
) -> str: ...
def serre_cartan_mono_to_string(
    mono: IntegerTuple,
    latex: bool = ...,
    generic: bool = ...,
) -> str: ...
def wood_mono_to_string(
    mono: PairMonomial,
    latex: bool = ...,
) -> str: ...
def wall_mono_to_string(
    mono: PairMonomial,
    latex: bool = ...,
) -> str: ...
def wall_long_mono_to_string(
    mono: PairMonomial,
    latex: bool = ...,
) -> str: ...
def arnonA_mono_to_string(
    mono: PairMonomial,
    latex: bool = ...,
    p: int | Integer = ...,
) -> str: ...
def arnonA_long_mono_to_string(
    mono: PairMonomial,
    latex: bool = ...,
    p: int | Integer = ...,
) -> str: ...
def pst_mono_to_string(
    mono: PairMonomial | GenericAtomicMonomial,
    latex: bool = ...,
    generic: bool = ...,
) -> str: ...
def comm_mono_to_string(
    mono: PairMonomial | GenericAtomicMonomial,
    latex: bool = ...,
    generic: bool = ...,
) -> str: ...
def comm_long_mono_to_string(
    mono: PairMonomial | GenericAtomicMonomial,
    p: int | Integer,
    latex: bool = ...,
    generic: bool = ...,
) -> str: ...
def convert_perm(
    m: Iterable[int | Integer],
) -> list[int]: ...
