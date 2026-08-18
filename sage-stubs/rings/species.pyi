from collections.abc import Hashable, Iterable, Iterator, Mapping, Sequence
from typing import TypeAlias

from sage.combinat.free_module import CombinatorialFreeModule
from sage.combinat.integer_vector import IntegerVector
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.misc.fast_methods import WithEqualityById
from sage.monoids.indexed_free_monoid import (
    IndexedFreeAbelianMonoid,
    IndexedFreeAbelianMonoidElement,
)
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.sets.set import Set_object_enumerated
from sage.structure.element import Element, RingElement
from sage.structure.factorization import Factorization
from sage.structure.parent import Parent
from sage.structure.unique_representation import (
    UniqueRepresentation,
    WithPicklingByInitArgs,
)

SpeciesLabel: TypeAlias = Hashable
SpeciesLabels: TypeAlias = Sequence[Iterable[SpeciesLabel]]
DomainPartition: TypeAlias = (
    Mapping[int, Iterable[SpeciesLabel]] | Sequence[Iterable[SpeciesLabel]]
)
SpeciesStructure: TypeAlias = tuple[SpeciesLabel, ...]

def _SymmetricGroup(n: int | Integer) -> PermutationGroup_generic: ...
def _label_sets(
    arity: int,
    labels: SpeciesLabels,
) -> list[tuple[SpeciesLabel, ...]]: ...

class AtomicSpeciesElement(
    WithEqualityById,
    Element,
    WithPicklingByInitArgs,
):
    @staticmethod
    def __classcall__(
        class_: type[AtomicSpeciesElement],
        parent: AtomicSpecies,
        G: PermutationGroup_generic,
        dompart: DomainPartition,
    ) -> AtomicSpeciesElement: ...
    def __init__(
        self,
        parent: AtomicSpecies,
        dis: PermutationGroup_generic,
        domain_partition: DomainPartition,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def grade(self) -> IntegerVector: ...
    def __lt__(self, other: AtomicSpeciesElement) -> bool: ...
    def __le__(self, other: AtomicSpeciesElement) -> bool: ...
    def structures(
        self,
        *labels: Iterable[SpeciesLabel],
    ) -> Iterator[SpeciesStructure]: ...
    def __call__(
        self,
        *args: IndexedFreeAbelianMonoidElement,
    ) -> AtomicSpeciesElement: ...

class AtomicSpecies(
    UniqueRepresentation,
    Parent[AtomicSpeciesElement],
):
    Element: type[AtomicSpeciesElement]
    @staticmethod
    def __classcall__(
        class_: type[AtomicSpecies],
        names: str | Sequence[str],
    ) -> AtomicSpecies: ...
    def __init__(self, names: tuple[str, ...]) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        G: AtomicSpeciesElement | PermutationGroup_generic,
        pi: DomainPartition | None = ...,
        check: bool = ...,
    ) -> AtomicSpeciesElement: ...
    def _rename(self, n: int | Integer) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    def grading_set(self) -> Parent[IntegerVector]: ...
    def subset(
        self,
        size: int | Integer,
    ) -> Set_object_enumerated[AtomicSpeciesElement]: ...
    def graded_component(
        self,
        mc: Sequence[int | Integer],
    ) -> Set_object_enumerated[AtomicSpeciesElement]: ...
    def _an_element_(self) -> AtomicSpeciesElement: ...

def _stabilizer_subgroups(
    G: PermutationGroup_generic,
    X: Iterable[SpeciesLabel],
    a: SpeciesLabel,
    side: str = ...,
    check: bool = ...,
) -> list[PermutationGroup_generic]: ...

class MolecularSpecies(IndexedFreeAbelianMonoid):
    @staticmethod
    def __classcall__(
        class_: type[MolecularSpecies],
        names: str | Sequence[str],
    ) -> MolecularSpecies: ...
    def __init__(self, names: tuple[str, ...]) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        G: IndexedFreeAbelianMonoidElement | PermutationGroup_generic,
        pi: DomainPartition | None = ...,
        check: bool = ...,
    ) -> IndexedFreeAbelianMonoidElement: ...
    def grading_set(self) -> Parent[IntegerVector]: ...
    def subset(
        self,
        size: int | Integer,
    ) -> Set_object_enumerated[IndexedFreeAbelianMonoidElement]: ...
    def graded_component(
        self,
        mc: Sequence[int | Integer],
    ) -> Set_object_enumerated[IndexedFreeAbelianMonoidElement]: ...

class PolynomialSpeciesElement(CombinatorialFreeModule.Element):
    def is_constant(self) -> bool: ...
    def is_virtual(self) -> bool: ...
    def is_molecular(self) -> bool: ...
    def is_atomic(self) -> bool: ...
    def tilde(self) -> PolynomialSpeciesElement: ...
    def hadamard_product(
        self,
        other: PolynomialSpeciesElement,
    ) -> PolynomialSpeciesElement: ...
    def _compose_with_singletons(
        self,
        names: Sequence[str],
        args: Sequence[PolynomialSpeciesElement],
    ) -> PolynomialSpeciesElement: ...
    def _compose_with_weighted_singletons(
        self,
        names: Sequence[str],
        multiplicities: Sequence[Sequence[int | Integer]],
        degrees: Sequence[Sequence[int | Integer]],
    ) -> PolynomialSpeciesElement: ...
    def __call__(
        self,
        *args: PolynomialSpeciesElement,
    ) -> PolynomialSpeciesElement: ...
    def factor(self) -> Factorization: ...
    def structures(
        self,
        *labels: Iterable[SpeciesLabel],
    ) -> Iterator[SpeciesStructure]: ...

class PolynomialSpecies(CombinatorialFreeModule):
    Element: type[PolynomialSpeciesElement]
    def __classcall__(
        cls: type[PolynomialSpecies],
        base_ring: Ring,
        names: str | Sequence[str],
    ) -> PolynomialSpecies: ...
    def __init__(
        self,
        base_ring: Ring,
        names: tuple[str, ...],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        G: PolynomialSpeciesElement
        | RingElement
        | IndexedFreeAbelianMonoidElement
        | PermutationGroup_generic,
        pi: DomainPartition | None = ...,
        check: bool = ...,
    ) -> PolynomialSpeciesElement: ...
    def _first_ngens(self, n: int) -> tuple[PolynomialSpeciesElement, ...]: ...
    def change_ring(self, R: Ring) -> PolynomialSpecies: ...
    def degree_on_basis(
        self,
        m: IndexedFreeAbelianMonoidElement,
    ) -> Integer: ...
    def one_basis(self) -> IndexedFreeAbelianMonoidElement: ...
    def _an_element_(self) -> PolynomialSpeciesElement: ...
    def product_on_basis(
        self,
        H: IndexedFreeAbelianMonoidElement,
        K: IndexedFreeAbelianMonoidElement,
    ) -> PolynomialSpeciesElement: ...
    def _powersum(
        self,
        s: int,
        n: int | Integer,
    ) -> PolynomialSpeciesElement: ...
    def _exponential(
        self,
        multiplicities: Sequence[Sequence[int | Integer]],
        degrees: Sequence[Sequence[int | Integer]],
    ) -> PolynomialSpeciesElement: ...

def _atomic_set_like_species(
    n: int | Integer,
    names: str | Sequence[str],
) -> list[AtomicSpeciesElement]: ...
