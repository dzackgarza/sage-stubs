from collections.abc import Iterator, Sequence
from typing import Literal

from sage.algebras.steenrod.steenrod_algebra import SteenrodBasisKey
from sage.algebras.steenrod.steenrod_algebra_misc import (
    GenericAtomicMonomial,
    GenericMilnorMonomial,
    ModTwoProfile,
    OddPrimaryProfile,
    PairMonomial,
    SteenrodBasisName,
    TruncationType,
)
from sage.matrix.matrix0 import Matrix
from sage.rings.finite_rings.element_base import FiniteRingElement
from sage.rings.integer import Integer

type SteenrodGenericFlag = bool | Literal["auto"]
type IntegerTuple = tuple[int | Integer, ...]
type MilnorBasisKey = IntegerTuple | GenericMilnorMonomial
type SerreCartanBasisKey = IntegerTuple
type AtomicBasisKey = PairMonomial | GenericAtomicMonomial
type SteenrodBasis = tuple[SteenrodBasisKey, ...]

def convert_to_milnor_matrix(
    n: int | Integer,
    basis: str,
    p: int | Integer = ...,
    generic: SteenrodGenericFlag = ...,
) -> Matrix[FiniteRingElement]: ...
def convert_from_milnor_matrix(
    n: int | Integer,
    basis: str,
    p: int | Integer = ...,
    generic: SteenrodGenericFlag = ...,
) -> Matrix[FiniteRingElement]: ...
def steenrod_algebra_basis(
    n: int | Integer,
    basis: str = ...,
    p: int | Integer = ...,
    *,
    profile: ModTwoProfile | OddPrimaryProfile | None = ...,
    truncation_type: TruncationType | None = ...,
    generic: bool | None = ...,
    **kwds: object,
) -> SteenrodBasis: ...
def restricted_partitions(
    n: int | Integer,
    l: Sequence[int | Integer],
    no_repeats: bool = ...,
) -> Iterator[list[int | Integer]]: ...
def xi_degrees(
    n: int | Integer,
    p: int | Integer = ...,
    reverse: bool = ...,
) -> list[int | Integer]: ...
def milnor_basis(
    n: int | Integer,
    p: int | Integer = ...,
    *,
    profile: ModTwoProfile | OddPrimaryProfile | None = ...,
    truncation_type: TruncationType | None = ...,
    generic: bool | None = ...,
    **kwds: object,
) -> tuple[MilnorBasisKey, ...]: ...
def serre_cartan_basis(
    n: int | Integer,
    p: int | Integer = ...,
    bound: int | Integer = ...,
    **kwds: object,
) -> tuple[SerreCartanBasisKey, ...]: ...
def atomic_basis(
    n: int | Integer,
    basis: str,
    **kwds: object,
) -> tuple[PairMonomial, ...]: ...
def arnonC_basis(
    n: int | Integer,
    bound: int | Integer = ...,
) -> tuple[IntegerTuple, ...]: ...
def atomic_basis_odd(
    n: int | Integer,
    basis: str,
    p: int | Integer,
    *,
    profile: OddPrimaryProfile | None = ...,
    truncation_type: TruncationType | None = ...,
    generic: bool | None = ...,
    **kwds: object,
) -> tuple[GenericAtomicMonomial, ...]: ...
def steenrod_basis_error_check(
    dim: int | Integer,
    p: int | Integer,
    *,
    generic: bool | None = ...,
    **kwds: object,
) -> None: ...
