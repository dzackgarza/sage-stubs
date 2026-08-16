from collections.abc import Callable, Iterator, Sequence

from sage.categories.category import Category
from sage.combinat.combinat import CombinatorialElement
from sage.combinat.partition import Partition
from sage.combinat.skew_partition import SkewPartition
from sage.combinat.skew_tableau import SkewTableau
from sage.combinat.words.word import Word_class
from sage.rings.integer import Integer
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression

type _Entry = int | Integer | None
type _Row = Sequence[_Entry]
type _Rows = Sequence[_Row]
type _MutableRows = list[list[_Entry]]
type _PartitionLike = Partition | Sequence[int | Integer]
type _SkewPartitionLike = SkewPartition | Sequence[Sequence[int | Integer]]
type _SkewTableauExpr = list[_PartitionLike | _MutableRows]
type _RecursiveNode = list[_PartitionLike | list[int]]
type _GraphResult = list[int] | list[Polynomial] | list[_SkewTableauExpr]
type _GraphFunction = Callable[
    [
        list[_GraphResult],
        list[_RecursiveNode],
        _SkewPartitionLike,
        Sequence[int | Integer],
        int,
    ],
    _GraphResult,
]
type _InversionPosition = tuple[int, tuple[int, int]]
type _InversionPair = tuple[_InversionPosition, _InversionPosition]

class RibbonTableau(SkewTableau):
    def __init__(
        self, parent: RibbonTableaux, rt: _Rows | tuple[_Row, ...]
    ) -> None: ...
    def length(self) -> int: ...
    def to_word(self) -> Word_class: ...

class RibbonTableaux(UniqueRepresentation, Parent):
    def __init__(self) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(self, rt: _Rows | tuple[_Row, ...]) -> RibbonTableau: ...
    def from_expr(self, l: _SkewTableauExpr) -> RibbonTableau: ...
    Element: type[RibbonTableau]

class RibbonTableaux_shape_weight_length(RibbonTableaux):
    def __init__(
        self, shape: SkewPartition, weight: tuple[int | Integer, ...], length: int
    ) -> None: ...
    def __iter__(self) -> Iterator[RibbonTableau]: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: object) -> bool: ...
    def cardinality(self) -> Integer: ...

def insertion_tableau(
    self, perm: list[int], evaluation: int, tableau: _SkewTableauExpr, length: int
) -> _SkewTableauExpr | None: ...
def count_rec(
    self,
    current: list[_RecursiveNode],
    part: _SkewPartitionLike,
    weight: list[int],
    length: int,
) -> list[int]: ...
def list_rec(
    self,
    current: list[_RecursiveNode],
    part: _SkewPartitionLike,
    weight: list[int],
    length: int,
) -> list[_SkewTableauExpr | None]: ...
def spin_rec(
    self,
    nexts: list[list[Polynomial]],
    current: list[_RecursiveNode],
    part: SkewPartition,
    weight: list[int],
    length: int,
) -> list[Polynomial]: ...
def spin_polynomial_square(self, weight: list[int], length: int) -> Polynomial: ...
def spin_polynomial(self, weight: list[int], length: int) -> Expression: ...
def cospin_polynomial(self, weight: list[int], length: int) -> Polynomial: ...
def graph_implementation_rec(
    self, weight: list[int], length: int, function: _GraphFunction
) -> _GraphResult: ...

class MultiSkewTableau(CombinatorialElement[SkewTableau]):
    def __init__(self, x: Sequence[SkewTableau]) -> None: ...
    def size(self) -> int: ...
    def weight(self) -> list[int]: ...
    def shape(self) -> list[SkewPartition]: ...
    def inversion_pairs(self) -> list[_InversionPair]: ...
    def inversions(self) -> int: ...
    def _inversion_pairs_from_position(
        self, k: int, ij: tuple[int, int]
    ) -> list[_InversionPair]: ...

class MultiSkewTableaux(UniqueRepresentation, Parent):
    def __init__(self, category: Category | None = None) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(self, rt: Sequence[SkewTableau]) -> MultiSkewTableau: ...
    Element: type[MultiSkewTableau]

class SemistandardMultiSkewTableaux(MultiSkewTableaux):
    def __init__(
        self, shape: tuple[SkewPartition, ...] | Category | None, weight: Partition
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[MultiSkewTableau]: ...
