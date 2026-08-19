from collections.abc import Iterable
from typing import Literal, Self

from sage.combinat.composition import Composition
from sage.combinat.partition import Partition
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.combinat.root_system.weyl_group import (
    WeylGroupElement,
    WeylGroup_gens,
    WeylGroup_permutation,
)
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.matrix.matrix import Matrix
from sage.rings.integer import Integer
from sage.sets.family import AbstractFamily
from sage.structure.list_clone import ClonableArray
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

type ReflectionSide = Literal["left", "right"]
type CyclicType = Literal["increasing", "decreasing"]
type AffinePermutationElement = (
    AffinePermutationTypeA
    | AffinePermutationTypeB
    | AffinePermutationTypeC
    | AffinePermutationTypeD
    | AffinePermutationTypeG
)
type AffinePermutationParent = (
    AffinePermutationGroupTypeA
    | AffinePermutationGroupTypeB
    | AffinePermutationGroupTypeC
    | AffinePermutationGroupTypeD
    | AffinePermutationGroupTypeG
)
type WeylGroupType = WeylGroup_gens | WeylGroup_permutation

class AffinePermutation(ClonableArray[Integer]):
    k: int
    n: int
    N: int

    def __init__(
        self,
        parent: AffinePermutationGroupGeneric,
        lst: Iterable[int | Integer],
        check: bool = ...,
    ) -> None: ...
    def parent(self) -> AffinePermutationGroupGeneric: ...
    def _repr_(self) -> str: ...
    def __rmul__(self, q: Self) -> Self: ...
    def __lmul__(self, q: Self) -> Self: ...
    def __mul__(self, q: Self) -> Self: ...
    def __invert__(self) -> Self: ...
    inverse = __invert__
    def check(self) -> None: ...
    def value(
        self,
        i: int | Integer,
        base_window: bool = ...,
    ) -> Integer: ...
    def position(self, i: int | Integer) -> Integer | Literal[False]: ...
    def apply_simple_reflection(
        self,
        i: int | Integer,
        side: ReflectionSide = ...,
    ) -> Self: ...
    def apply_simple_reflection_right(
        self,
        i: int | Integer,
    ) -> Self: ...
    def apply_simple_reflection_left(
        self,
        i: int | Integer,
    ) -> Self: ...
    def __call__(self, i: int | Integer) -> Integer: ...
    def has_right_descent(self, i: int | Integer) -> bool: ...
    def has_left_descent(self, i: int | Integer) -> bool: ...
    def has_descent(
        self,
        i: int | Integer,
        side: ReflectionSide = ...,
    ) -> bool: ...
    def descents(
        self,
        side: ReflectionSide = ...,
    ) -> list[int]: ...
    def length(self) -> int: ...
    def is_i_grassmannian(
        self,
        i: int | Integer = ...,
        side: ReflectionSide = ...,
    ) -> bool: ...
    def index_set(self) -> tuple[int, ...]: ...
    def lower_covers(
        self,
        side: ReflectionSide = ...,
    ) -> list[Self]: ...
    def is_one(self) -> bool: ...
    def reduced_word(self) -> list[int]: ...
    def signature(self) -> int: ...
    def to_weyl_group_element(self) -> WeylGroupElement: ...
    def grassmannian_quotient(
        self,
        i: int | Integer = ...,
        side: ReflectionSide = ...,
    ) -> tuple[Self, Self]: ...

class AffinePermutationTypeA(AffinePermutation):
    def parent(self) -> AffinePermutationGroupTypeA: ...
    def apply_simple_reflection_right(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeA: ...
    def apply_simple_reflection_left(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeA: ...
    def to_type_a(self) -> AffinePermutationTypeA: ...
    def flip_automorphism(self) -> AffinePermutationTypeA: ...
    def promotion(self) -> AffinePermutationTypeA: ...
    def maximal_cyclic_factor(
        self,
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
        verbose: bool = ...,
    ) -> list[int]: ...
    def maximal_cyclic_decomposition(
        self,
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
        verbose: bool = ...,
    ) -> list[list[int]]: ...
    def to_lehmer_code(
        self,
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
    ) -> Composition: ...
    def is_fully_commutative(self) -> bool: ...
    def to_bounded_partition(
        self,
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
    ) -> Partition: ...
    def to_core(
        self,
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
    ) -> Partition: ...
    def to_dominant(
        self,
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
    ) -> AffinePermutationTypeA: ...
    def tableau_of_word(
        self,
        w: Iterable[int | Integer],
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
        alpha: Iterable[int | Integer] | None = ...,
    ) -> list[list[int]]: ...

class AffinePermutationTypeC(AffinePermutation):
    def parent(self) -> AffinePermutationGroupTypeC: ...
    def value(self, i: int | Integer) -> Integer: ...
    def apply_simple_reflection_right(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeC: ...
    def apply_simple_reflection_left(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeC: ...
    def to_type_a(self) -> AffinePermutationTypeA: ...

class AffinePermutationTypeB(AffinePermutationTypeC):
    def parent(self) -> AffinePermutationGroupTypeB: ...
    def apply_simple_reflection_right(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeB: ...
    def apply_simple_reflection_left(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeB: ...

class AffinePermutationTypeD(AffinePermutationTypeC):
    def parent(self) -> AffinePermutationGroupTypeD: ...
    def apply_simple_reflection_right(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeD: ...
    def apply_simple_reflection_left(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeD: ...

class AffinePermutationTypeG(AffinePermutation):
    def parent(self) -> AffinePermutationGroupTypeG: ...
    def apply_simple_reflection_right(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeG: ...
    def apply_simple_reflection_left(
        self,
        i: int | Integer,
    ) -> AffinePermutationTypeG: ...
    def to_type_a(self) -> AffinePermutationTypeA: ...


def AffinePermutationGroup(
    cartan_type: CartanType_abstract | Iterable[object] | str,
) -> AffinePermutationParent: ...

class AffinePermutationGroupGeneric(
    UniqueRepresentation,
    Parent[AffinePermutation],
):
    Element: type[AffinePermutation]
    element_class: type[AffinePermutation]
    k: int
    n: int
    N: int

    def __init__(
        self,
        cartan_type: CartanType_abstract | Iterable[object] | str,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        window: Iterable[int | Integer],
    ) -> AffinePermutation: ...
    def weyl_group(self) -> WeylGroupType: ...
    def classical(
        self,
    ) -> PermutationGroup_generic | WeylGroupType: ...
    def cartan_type(self) -> CartanType_abstract: ...
    def cartan_matrix(self) -> Matrix: ...
    def is_crystallographic(self) -> bool: ...
    def index_set(self) -> tuple[int, ...]: ...
    def reflection_index_set(self) -> tuple[int, ...]: ...
    def rank(self) -> int: ...
    def simple_reflections(self) -> AbstractFamily: ...
    def from_reduced_word(
        self,
        word: Iterable[int | Integer],
    ) -> AffinePermutation: ...
    def random_element(
        self,
        n: int | Integer | None = ...,
    ) -> AffinePermutation: ...
    def from_word(
        self,
        w: Iterable[int | Integer],
    ) -> AffinePermutation: ...
    def _an_element_(self) -> AffinePermutation: ...

class AffinePermutationGroupTypeA(AffinePermutationGroupGeneric):
    Element: type[AffinePermutationTypeA]
    element_class: type[AffinePermutationTypeA]
    def _element_constructor_(
        self,
        window: Iterable[int | Integer],
    ) -> AffinePermutationTypeA: ...
    def one(self) -> AffinePermutationTypeA: ...
    def from_reduced_word(
        self,
        word: Iterable[int | Integer],
    ) -> AffinePermutationTypeA: ...
    def from_word(
        self,
        w: Iterable[int | Integer],
    ) -> AffinePermutationTypeA: ...
    def from_lehmer_code(
        self,
        C: Iterable[int | Integer],
        typ: CyclicType = ...,
        side: ReflectionSide = ...,
    ) -> AffinePermutationTypeA: ...

class AffinePermutationGroupTypeC(AffinePermutationGroupGeneric):
    Element: type[AffinePermutationTypeC]
    element_class: type[AffinePermutationTypeC]
    def _element_constructor_(
        self,
        window: Iterable[int | Integer],
    ) -> AffinePermutationTypeC: ...
    def one(self) -> AffinePermutationTypeC: ...
    def from_reduced_word(
        self,
        word: Iterable[int | Integer],
    ) -> AffinePermutationTypeC: ...
    def from_word(
        self,
        w: Iterable[int | Integer],
    ) -> AffinePermutationTypeC: ...

class AffinePermutationGroupTypeB(AffinePermutationGroupTypeC):
    Element: type[AffinePermutationTypeB]
    element_class: type[AffinePermutationTypeB]
    def _element_constructor_(
        self,
        window: Iterable[int | Integer],
    ) -> AffinePermutationTypeB: ...
    def one(self) -> AffinePermutationTypeB: ...
    def from_reduced_word(
        self,
        word: Iterable[int | Integer],
    ) -> AffinePermutationTypeB: ...
    def from_word(
        self,
        w: Iterable[int | Integer],
    ) -> AffinePermutationTypeB: ...

class AffinePermutationGroupTypeD(AffinePermutationGroupTypeC):
    Element: type[AffinePermutationTypeD]
    element_class: type[AffinePermutationTypeD]
    def _element_constructor_(
        self,
        window: Iterable[int | Integer],
    ) -> AffinePermutationTypeD: ...
    def one(self) -> AffinePermutationTypeD: ...
    def from_reduced_word(
        self,
        word: Iterable[int | Integer],
    ) -> AffinePermutationTypeD: ...
    def from_word(
        self,
        w: Iterable[int | Integer],
    ) -> AffinePermutationTypeD: ...

class AffinePermutationGroupTypeG(AffinePermutationGroupGeneric):
    Element: type[AffinePermutationTypeG]
    element_class: type[AffinePermutationTypeG]
    def _element_constructor_(
        self,
        window: Iterable[int | Integer],
    ) -> AffinePermutationTypeG: ...
    def one(self) -> AffinePermutationTypeG: ...
    def from_reduced_word(
        self,
        word: Iterable[int | Integer],
    ) -> AffinePermutationTypeG: ...
    def from_word(
        self,
        w: Iterable[int | Integer],
    ) -> AffinePermutationTypeG: ...
