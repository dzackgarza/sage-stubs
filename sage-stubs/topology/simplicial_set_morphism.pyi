from collections.abc import Iterator, Mapping
from typing import TypeVar

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.homology.chain_complex_morphism import ChainComplexMorphism
from sage.homology.homology_morphism import InducedHomologyMorphism
from sage.structure.element import FieldElement, RingElement
from sage.structure.parent import Parent
from sage.topology.simplicial_set import (
    AbstractSimplex_class,
    SimplicialSet_arbitrary,
)
from sage.topology.simplicial_set_constructions import (
    PullbackOfSimplicialSets,
    PullbackOfSimplicialSets_finite,
    PushoutOfSimplicialSets,
    PushoutOfSimplicialSets_finite,
    SubSimplicialSet,
)

_Scalar = TypeVar("_Scalar", bound=RingElement)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)

type SimplicialMapData = Mapping[
    AbstractSimplex_class,
    AbstractSimplex_class,
]
type SimplicialPushout = (
    PushoutOfSimplicialSets
    | PushoutOfSimplicialSets_finite
)
type SimplicialPullback = (
    PullbackOfSimplicialSets
    | PullbackOfSimplicialSets_finite
)


class SimplicialSetHomset(
    Homset[
        SimplicialSetMorphism,
        AbstractSimplex_class,
        AbstractSimplex_class,
    ],
):
    Element: type[SimplicialSetMorphism]
    element_class: type[SimplicialSetMorphism]

    def domain(self) -> SimplicialSet_arbitrary: ...
    def codomain(self) -> SimplicialSet_arbitrary: ...
    def __call__(
        self,
        f: SimplicialMapData,
        check: bool = ...,
    ) -> SimplicialSetMorphism: ...
    def diagonal_morphism(self) -> SimplicialSetMorphism: ...
    def identity(self) -> SimplicialSetMorphism: ...
    one = identity
    def constant_map(
        self,
        point: AbstractSimplex_class | None = ...,
    ) -> SimplicialSetMorphism: ...
    def an_element(self) -> SimplicialSetMorphism: ...
    def __iter__(self) -> Iterator[SimplicialSetMorphism]: ...
    def _latex_(self) -> str: ...


class SimplicialSetMorphism(
    Morphism[AbstractSimplex_class, AbstractSimplex_class],
):
    def __init__(
        self,
        data: SimplicialMapData | None = ...,
        domain: SimplicialSet_arbitrary | None = ...,
        codomain: SimplicialSet_arbitrary | None = ...,
        constant: AbstractSimplex_class | None = ...,
        identity: bool = ...,
        check: bool = ...,
    ) -> None: ...
    def parent(self) -> SimplicialSetHomset: ...
    def domain(self) -> SimplicialSet_arbitrary: ...
    def codomain(self) -> SimplicialSet_arbitrary: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __call__(
        self,
        x: AbstractSimplex_class,
    ) -> AbstractSimplex_class: ...
    def image(
        self,
    ) -> SimplicialSet_arbitrary | SubSimplicialSet: ...
    def is_identity(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def is_injective(self) -> bool: ...
    def is_bijective(self) -> bool: ...
    def is_pointed(self) -> bool: ...
    def is_constant(self) -> bool: ...
    def pushout(
        self,
        *others: SimplicialSetMorphism,
    ) -> SimplicialPushout: ...
    def pullback(
        self,
        *others: SimplicialSetMorphism,
    ) -> SimplicialPullback: ...
    def equalizer(
        self,
        other: SimplicialSetMorphism,
    ) -> SimplicialPullback: ...
    def coequalizer(
        self,
        other: SimplicialSetMorphism,
    ) -> SimplicialPushout: ...
    def mapping_cone(self) -> SimplicialPushout: ...
    def product(
        self,
        *others: SimplicialSetMorphism,
    ) -> SimplicialSetMorphism: ...
    def coproduct(
        self,
        *others: SimplicialSetMorphism,
    ) -> SimplicialSetMorphism: ...
    def suspension(self, n: int = ...) -> SimplicialSetMorphism: ...
    def n_skeleton(
        self,
        n: int,
        domain: SimplicialSet_arbitrary | None = ...,
        codomain: SimplicialSet_arbitrary | None = ...,
    ) -> SimplicialSetMorphism: ...
    def associated_chain_complex_morphism(
        self,
        base_ring: Parent[_Scalar],
        augmented: bool = ...,
        cochain: bool = ...,
    ) -> ChainComplexMorphism[int, _Scalar]: ...
    def induced_homology_morphism(
        self,
        base_ring: Parent[_FieldScalar] | None = ...,
        cohomology: bool = ...,
    ) -> InducedHomologyMorphism[_FieldScalar]: ...
    def _repr_type(self) -> str: ...
    def _repr_defn(self) -> str: ...
