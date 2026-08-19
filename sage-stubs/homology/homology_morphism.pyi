from typing import Generic, TypeVar, overload

from sage.categories.morphism import Morphism
from sage.homology.homology_vector_space_with_basis import (
    CohomologyRing,
    HomologyVectorSpaceWithBasis,
)
from sage.matrix.matrix import Matrix
from sage.structure.element import FieldElement
from sage.structure.parent import Parent
from sage.topology.simplicial_complex_morphism import SimplicialComplexMorphism

_FieldScalar = TypeVar(
    "_FieldScalar",
    bound=FieldElement,
    default=FieldElement,
)

type HomologyModule[_FieldScalar: FieldElement] = (
    HomologyVectorSpaceWithBasis[_FieldScalar]
    | CohomologyRing[_FieldScalar]
)
type HomologyClass = (
    HomologyVectorSpaceWithBasis.Element
    | CohomologyRing.Element
)


class InducedHomologyMorphism(
    Morphism[HomologyClass, HomologyClass],
    Generic[_FieldScalar],
):
    def __init__(
        self,
        map: SimplicialComplexMorphism,
        base_ring: Parent[_FieldScalar] | None = ...,
        cohomology: bool = ...,
    ) -> None: ...
    def domain(self) -> HomologyModule[_FieldScalar]: ...
    def codomain(self) -> HomologyModule[_FieldScalar]: ...
    def base_ring(self) -> Parent[_FieldScalar]: ...

    @overload
    def to_matrix(self, deg: None = ...) -> Matrix[_FieldScalar]: ...
    @overload
    def to_matrix(self, deg: int) -> Matrix[_FieldScalar]: ...

    def __call__(self, elt: HomologyClass) -> HomologyClass: ...
    def __eq__(self, other: object) -> bool: ...
    def is_identity(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def is_injective(self) -> bool: ...
