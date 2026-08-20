from collections.abc import Iterable, Mapping, Sequence
from typing import Self

from sage.structure.unique_representation import UniqueRepresentation
from sage.topology.simplicial_set import (
    AbstractSimplex_class,
    SimplicialSet_arbitrary,
    SimplicialSet_finite,
)
from sage.topology.simplicial_set_morphism import SimplicialSetMorphism

type SimplicialSetData = Mapping[
    AbstractSimplex_class,
    Sequence[AbstractSimplex_class] | None,
]
type SimplicialMaps = Iterable[SimplicialSetMorphism]
type SimplicialFactors = Iterable[SimplicialSet_arbitrary]


class SubSimplicialSet(
    SimplicialSet_finite,
    UniqueRepresentation,
):
    @staticmethod
    def __classcall__(
        self: type[SubSimplicialSet],
        data: SimplicialSetData,
        ambient: SimplicialSet_arbitrary | None = ...,
    ) -> SubSimplicialSet: ...
    def __init__(
        self,
        data: SimplicialSetData,
        ambient: SimplicialSet_arbitrary | None = ...,
    ) -> None: ...
    def inclusion_map(self) -> SimplicialSetMorphism: ...
    def ambient_space(self) -> SimplicialSet_arbitrary: ...


class PullbackOfSimplicialSets(
    SimplicialSet_arbitrary,
    UniqueRepresentation,
):
    @staticmethod
    def __classcall_private__(
        self: type[PullbackOfSimplicialSets],
        maps: SimplicialMaps | None = ...,
    ) -> PullbackOfSimplicialSets: ...
    def __init__(
        self,
        maps: SimplicialMaps | None = ...,
    ) -> None: ...
    def n_skeleton(
        self,
        n: int,
    ) -> PullbackOfSimplicialSets_finite: ...
    def defining_map(self, i: int) -> SimplicialSetMorphism: ...


class PullbackOfSimplicialSets_finite(
    PullbackOfSimplicialSets,
    SimplicialSet_finite,
):
    @staticmethod
    def __classcall_private__(
        self: type[PullbackOfSimplicialSets_finite],
        maps: SimplicialMaps | None = ...,
    ) -> PullbackOfSimplicialSets_finite: ...
    def __init__(
        self,
        maps: SimplicialMaps | None = ...,
    ) -> None: ...
    def structure_map(self, i: int) -> SimplicialSetMorphism: ...
    projection_map = structure_map
    def universal_property(
        self,
        *maps: SimplicialSetMorphism,
    ) -> SimplicialSetMorphism: ...


class Factors:
    def factors(self) -> tuple[SimplicialSet_arbitrary, ...]: ...
    def factor(self, i: int) -> SimplicialSet_arbitrary: ...


class ProductOfSimplicialSets(
    PullbackOfSimplicialSets,
    Factors,
):
    @staticmethod
    def __classcall__(
        cls: type[ProductOfSimplicialSets],
        factors: SimplicialFactors | None = ...,
    ) -> ProductOfSimplicialSets: ...
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...
    def n_skeleton(self, n: int) -> SimplicialSet_finite: ...
    def factor(
        self,
        i: int,
        as_subset: bool = ...,
    ) -> SimplicialSet_arbitrary | SubSimplicialSet: ...


class ProductOfSimplicialSets_finite(
    ProductOfSimplicialSets,
    PullbackOfSimplicialSets_finite,
):
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...
    def projection_map(self, i: int) -> SimplicialSetMorphism: ...
    def wedge_as_subset(self) -> SubSimplicialSet: ...
    def fat_wedge_as_subset(self) -> SubSimplicialSet: ...


class PushoutOfSimplicialSets(
    SimplicialSet_arbitrary,
    UniqueRepresentation,
):
    @staticmethod
    def __classcall_private__(
        cls: type[PushoutOfSimplicialSets],
        maps: SimplicialMaps | None = ...,
        vertex_name: str | None = ...,
    ) -> PushoutOfSimplicialSets: ...
    def __init__(
        self,
        maps: SimplicialMaps | None = ...,
        vertex_name: str | None = ...,
    ) -> None: ...
    def n_skeleton(
        self,
        n: int,
    ) -> PushoutOfSimplicialSets_finite: ...
    def defining_map(self, i: int) -> SimplicialSetMorphism: ...


class PushoutOfSimplicialSets_finite(
    PushoutOfSimplicialSets,
    SimplicialSet_finite,
):
    @staticmethod
    def __classcall_private__(
        cls: type[PushoutOfSimplicialSets_finite],
        maps: SimplicialMaps | None = ...,
        vertex_name: str | None = ...,
    ) -> PushoutOfSimplicialSets_finite: ...
    def __init__(
        self,
        maps: SimplicialMaps | None = ...,
        vertex_name: str | None = ...,
    ) -> None: ...
    def structure_map(self, i: int) -> SimplicialSetMorphism: ...
    def universal_property(
        self,
        *maps: SimplicialSetMorphism,
    ) -> SimplicialSetMorphism: ...


class QuotientOfSimplicialSet(PushoutOfSimplicialSets):
    def __init__(
        self,
        inclusion: SimplicialSetMorphism,
        vertex_name: str = ...,
    ) -> None: ...
    def ambient(self) -> SimplicialSet_arbitrary: ...
    def subcomplex(self) -> SimplicialSet_arbitrary: ...
    def n_skeleton(
        self,
        n: int,
    ) -> QuotientOfSimplicialSet_finite: ...


class QuotientOfSimplicialSet_finite(
    QuotientOfSimplicialSet,
    PushoutOfSimplicialSets_finite,
):
    def __init__(
        self,
        inclusion: SimplicialSetMorphism,
        vertex_name: str = ...,
    ) -> None: ...
    def quotient_map(self) -> SimplicialSetMorphism: ...


class SmashProductOfSimplicialSets_finite(
    QuotientOfSimplicialSet_finite,
    Factors,
):
    @staticmethod
    def __classcall__(
        cls: type[SmashProductOfSimplicialSets_finite],
        factors: SimplicialFactors | None = ...,
    ) -> SmashProductOfSimplicialSets_finite: ...
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...


class WedgeOfSimplicialSets(
    PushoutOfSimplicialSets,
    Factors,
):
    @staticmethod
    def __classcall__(
        cls: type[WedgeOfSimplicialSets],
        factors: SimplicialFactors | None = ...,
    ) -> WedgeOfSimplicialSets: ...
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...
    summands = Factors.factors
    summand = Factors.factor


class WedgeOfSimplicialSets_finite(
    WedgeOfSimplicialSets,
    PushoutOfSimplicialSets_finite,
):
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...
    def inclusion_map(self, i: int) -> SimplicialSetMorphism: ...
    def projection_map(self, i: int) -> SimplicialSetMorphism: ...


class DisjointUnionOfSimplicialSets(
    PushoutOfSimplicialSets,
    Factors,
):
    @staticmethod
    def __classcall__(
        cls: type[DisjointUnionOfSimplicialSets],
        factors: SimplicialFactors | None = ...,
    ) -> DisjointUnionOfSimplicialSets: ...
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...
    def n_skeleton(
        self,
        n: int,
    ) -> DisjointUnionOfSimplicialSets_finite: ...
    summands = Factors.factors
    summand = Factors.factor


class DisjointUnionOfSimplicialSets_finite(
    DisjointUnionOfSimplicialSets,
    PushoutOfSimplicialSets_finite,
):
    def __init__(
        self,
        factors: SimplicialFactors | None = ...,
    ) -> None: ...
    def inclusion_map(self, i: int) -> SimplicialSetMorphism: ...


class ConeOfSimplicialSet(
    SimplicialSet_arbitrary,
    UniqueRepresentation,
):
    def __init__(self, base: SimplicialSet_arbitrary) -> None: ...
    def n_skeleton(self, n: int) -> SimplicialSet_finite: ...


class ConeOfSimplicialSet_finite(
    ConeOfSimplicialSet,
    SimplicialSet_finite,
):
    def __init__(self, base: SimplicialSet_finite) -> None: ...
    def base_as_subset(self) -> SubSimplicialSet: ...
    def map_from_base(self) -> SimplicialSetMorphism: ...


class ReducedConeOfSimplicialSet(QuotientOfSimplicialSet):
    def __init__(self, base: SimplicialSet_arbitrary) -> None: ...
    def n_skeleton(self, n: int) -> SimplicialSet_finite: ...


class ReducedConeOfSimplicialSet_finite(
    ReducedConeOfSimplicialSet,
    QuotientOfSimplicialSet_finite,
):
    def __init__(self, base: SimplicialSet_finite) -> None: ...
    def map_from_base(self) -> SimplicialSetMorphism: ...


class SuspensionOfSimplicialSet(QuotientOfSimplicialSet):
    def __init__(self, base: SimplicialSet_arbitrary) -> None: ...
    def n_skeleton(self, n: int) -> SimplicialSet_finite: ...
    def __repr_or_latex__(
        self,
        output_type: str | None = ...,
    ) -> str: ...


class SuspensionOfSimplicialSet_finite(
    SuspensionOfSimplicialSet,
    QuotientOfSimplicialSet_finite,
):
    def __init__(self, base: SimplicialSet_finite) -> None: ...
