from collections.abc import Iterator

from sage.combinat.binary_tree import LabelledBinaryTree
from sage.combinat.permutation import Permutation
from sage.combinat.posets.lattices import FiniteLatticePoset
from sage.rings.integer import Integer
from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

class BaxterPermutations(
    UniqueRepresentation,
    Parent[Permutation],
):
    element_class: type[Permutation]

    @staticmethod
    def __classcall_private__(
        classe: type[BaxterPermutations],
        n: int | Integer | None = ...,
    ) -> BaxterPermutations_size | BaxterPermutations_all: ...

class BaxterPermutations_size(BaxterPermutations):
    element_class: type[Permutation]

    def __init__(self, n: int | Integer) -> None: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[Permutation]: ...
    def _an_element_(self) -> Permutation: ...
    def cardinality(self) -> Integer: ...
    def lattice(self) -> FiniteLatticePoset: ...

class BaxterPermutations_all(
    DisjointUnionEnumeratedSets,
    BaxterPermutations,
):
    element_class: type[Permutation]

    def __init__(
        self,
        n: int | Integer | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[Permutation]: ...
    def to_pair_of_twin_binary_trees(
        self,
        p: Permutation,
    ) -> tuple[LabelledBinaryTree, LabelledBinaryTree]: ...
