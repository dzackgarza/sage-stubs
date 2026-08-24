from typing import Generic, Literal, TypeVar, overload

from sage.algebras.clifford_algebra import ExteriorAlgebraIdeal
from sage.algebras.clifford_algebra_element import CliffordAlgebraElement
from sage.data_structures.bitset import FrozenBitset
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_Scalar = TypeVar(
    "_Scalar",
    bound=RingElement,
    default=RingElement,
)

class GBElement(Generic[_Scalar]):
    def __init__(
        self,
        x: CliffordAlgebraElement[_Scalar],
        ls: FrozenBitset,
        n: int | Integer,
    ) -> None: ...
    def __hash__(self) -> int: ...
    def __richcmp__(
        self,
        other: GBElement[_Scalar],
        op: int,
    ) -> bool: ...

class GroebnerStrategy(Generic[_Scalar]):
    groebner_basis: tuple[CliffordAlgebraElement[_Scalar] | None, ...]

    def __init__(self, I: ExteriorAlgebraIdeal[_Scalar]) -> None: ...
    def compute_groebner(self, reduced: bool = ...) -> None: ...
    def reduce_computed_gb(self) -> None: ...
    def reduce(
        self,
        f: CliffordAlgebraElement[_Scalar],
    ) -> CliffordAlgebraElement[_Scalar]: ...
    @overload
    def sorted_monomials(
        self,
        as_dict: Literal[False] = ...,
    ) -> list[CliffordAlgebraElement[_Scalar]]: ...
    @overload
    def sorted_monomials(
        self,
        as_dict: Literal[True],
    ) -> dict[Integer, CliffordAlgebraElement[_Scalar]]: ...
    @overload
    def sorted_monomials(
        self,
        as_dict: bool,
    ) -> (
        list[CliffordAlgebraElement[_Scalar]]
        | dict[Integer, CliffordAlgebraElement[_Scalar]]
    ): ...
    def monomial_to_int(
        self,
    ) -> dict[CliffordAlgebraElement[_Scalar], Integer]: ...

class GroebnerStrategyNegLex(GroebnerStrategy[_Scalar], Generic[_Scalar]): ...
class GroebnerStrategyDegRevLex(
    GroebnerStrategy[_Scalar],
    Generic[_Scalar],
): ...
class GroebnerStrategyDegLex(GroebnerStrategy[_Scalar], Generic[_Scalar]): ...
