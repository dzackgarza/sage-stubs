from collections.abc import Container, Hashable, Iterable, Iterator, Sequence
from typing import Generic, Literal, Self, TypeVar, overload

from sage.combinat.posets.posets import FinitePoset
from sage.geometry.convex_set import ConvexSet_closed
from sage.geometry.point_collection import PointCollection
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.geometry.relative_interior import RelativeInterior
from sage.geometry.toric_lattice import (
    ToricLattice_ambient,
    ToricLattice_generic,
    ToricLattice_quotient,
    ToricLattice_sublattice,
    ToricLattice_sublattice_with_basis,
)
from sage.geometry.toric_lattice_element import ToricLatticeElement, ToricPlot
from sage.interfaces.expect import Expect
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import (
    FreeModule_generic,
    FreeModule_generic_field,
    FreeModule_generic_pid,
)
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.rings.integer_ring import IntegerRing_class
from sage.rings.rational import Rational
from sage.rings.rational_field import RationalField
from sage.structure.element import Element, FieldElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent
from sage.structure.sage_object import SageObject

_Ray = TypeVar(
    "_Ray",
    bound=FreeModuleElement[Integer],
    default=ToricLatticeElement,
)
_Lattice = TypeVar(
    "_Lattice",
    bound=FreeModule_generic_pid[Integer],
    default=ToricLattice_generic,
)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)
_Scalar = TypeVar("_Scalar", bound=RingElement)


type ConeRayInput = (
    FreeModuleElement[RingElement]
    | Sequence[ElementConstructorInput]
)
type ConeRayInputs = Iterable[ConeRayInput]
type ConeInput = ConeRayInputs | PointCollection | Polyhedron_base
type LatticeInput = ToricLattice_generic | FreeModule_generic_pid[Integer]
type IntegralPointCollection = PointCollection[
    FreeModuleElement[Integer],
    FreeModule_generic_pid[Integer],
    Integer,
]
type ToricPointCollection = PointCollection[
    ToricLatticeElement,
    ToricLattice_generic,
    Integer,
]
type RationalCone = ConvexRationalPolyhedralCone[
    FreeModuleElement[Integer],
    FreeModule_generic_pid[Integer],
]
type ToricCone = ConvexRationalPolyhedralCone[
    ToricLatticeElement,
    ToricLattice_generic,
]
type ConeFaceTuple = tuple[ConvexRationalPolyhedralCone, ...]
type ConeFacesByDimension = tuple[ConeFaceTuple, ...]


@overload
def Cone(
    rays: ConeInput,
    lattice: ToricLattice_generic | None = ...,
    check: bool = ...,
    normalize: bool = ...,
) -> ToricCone: ...
@overload
def Cone(
    rays: ConeInput,
    lattice: FreeModule_generic_pid[Integer],
    check: bool = ...,
    normalize: bool = ...,
) -> RationalCone: ...


def integral_length(
    v: FreeModuleElement[RingElement],
) -> Rational: ...


@overload
def normalize_rays(
    rays: ConeRayInputs,
    lattice: ToricLattice_generic,
) -> list[ToricLatticeElement]: ...
@overload
def normalize_rays(
    rays: ConeRayInputs,
    lattice: FreeModule_generic_pid[Integer],
) -> list[FreeModuleElement[Integer]]: ...


def classify_cone_2d(
    ray0: FreeModuleElement[Integer],
    ray1: FreeModuleElement[Integer],
    check: bool = ...,
) -> tuple[Integer, Integer]: ...


@overload
def random_cone(
    lattice: ToricLattice_generic | None = ...,
    min_ambient_dim: int | Integer = ...,
    max_ambient_dim: int | Integer = ...,
    min_rays: int | Integer = ...,
    max_rays: int | Integer = ...,
    strictly_convex: bool | None = ...,
    solid: bool | None = ...,
) -> ToricCone: ...
@overload
def random_cone(
    lattice: FreeModule_generic_pid[Integer],
    min_ambient_dim: int | Integer = ...,
    max_ambient_dim: int | Integer = ...,
    min_rays: int | Integer = ...,
    max_rays: int | Integer = ...,
    strictly_convex: bool | None = ...,
    solid: bool | None = ...,
) -> RationalCone: ...


class IntegralRayCollection(
    SageObject,
    Hashable,
    Iterable[_Ray],
    Generic[_Ray, _Lattice],
):
    def __init__(
        self,
        rays: Iterable[_Ray],
        lattice: _Lattice,
    ) -> None: ...
    def __richcmp__(
        self,
        other: IntegralRayCollection,
        op: int,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[_Ray]: ...
    def cartesian_product(
        self,
        other: IntegralRayCollection,
        lattice: FreeModule_generic_pid[Integer] | None = ...,
    ) -> IntegralRayCollection[
        FreeModuleElement[Integer],
        FreeModule_generic_pid[Integer],
    ]: ...
    def __neg__(
        self,
    ) -> IntegralRayCollection[_Ray, _Lattice]: ...
    def dim(self) -> int: ...
    dimension = dim
    def lattice(self) -> _Lattice: ...
    @overload
    def ambient_vector_space(
        self,
        base_field: None = ...,
    ) -> FreeModule_generic_field[Rational]: ...
    @overload
    def ambient_vector_space(
        self,
        base_field: Parent[_FieldScalar],
    ) -> FreeModule_generic_field[_FieldScalar]: ...
    def dual_lattice(self) -> FreeModule_generic_pid[Integer]: ...
    def lattice_dim(self) -> int: ...
    ambient_dim = lattice_dim
    def n_rays(self) -> int: ...
    nrays = n_rays
    def plot(self, **options: object) -> ToricPlot: ...
    def ray(self, n: int | Integer) -> _Ray: ...
    @overload
    def rays(self) -> PointCollection[_Ray, _Lattice, Integer]: ...
    @overload
    def rays(
        self,
        indices: Iterable[int],
    ) -> PointCollection[_Ray, _Lattice, Integer]: ...
    @overload
    def rays(
        self,
        *indices: int,
    ) -> PointCollection[_Ray, _Lattice, Integer]: ...
    def codim(self) -> int: ...
    codimension = codim
    @overload
    def span(
        self,
        base_ring: None | IntegerRing_class = ...,
    ) -> FreeModule_generic_pid[Integer]: ...
    @overload
    def span(
        self,
        base_ring: Parent[_Scalar],
    ) -> FreeModule_generic[_Scalar]: ...
    def _macaulay2_init_(
        self,
        macaulay2: Expect | None = ...,
    ) -> str: ...


class ConvexRationalPolyhedralCone(
    IntegralRayCollection[_Ray, _Lattice],
    Container[_Ray],
    ConvexSet_closed,
):
    def __init__(
        self,
        rays: Iterable[_Ray] | None = ...,
        lattice: _Lattice | None = ...,
        ambient: object | None = ...,
        ambient_ray_indices: Iterable[int] | None = ...,
        PPL: object | None = ...,
    ) -> None: ...
    def __contains__(self, point: object) -> bool: ...
    def _sage_input_(
        self,
        sib: object,
        coerced: bool,
    ) -> object: ...
    def _PPL_cone(self) -> object: ...
    def _macaulay2_init_(
        self,
        macaulay2: Expect | None = ...,
    ) -> str: ...
    def _contains(
        self,
        point: object,
        region: str = ...,
    ) -> bool: ...
    def interior_contains(self, point: object) -> bool: ...
    def interior(self) -> RelativeInterior: ...
    def relative_interior_contains(self, point: object) -> bool: ...
    def relative_interior(self) -> RelativeInterior: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def _some_elements_(self) -> tuple[FreeModuleElement[RingElement], ...]: ...
    def _sort_faces(
        self,
        faces: Iterable[ConvexRationalPolyhedralCone],
    ) -> ConeFaceTuple: ...
    def adjacent(self) -> ConeFaceTuple: ...
    def ambient(self) -> object: ...
    def ambient_ray_indices(self) -> tuple[int, ...]: ...
    def contains(self, point: object) -> bool: ...
    def cartesian_product(
        self,
        other: ConvexRationalPolyhedralCone,
        lattice: FreeModule_generic_pid[Integer] | None = ...,
    ) -> RationalCone: ...
    def dual(self) -> RationalCone: ...
    def embed(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> ConvexRationalPolyhedralCone: ...
    def face_lattice(self) -> FinitePoset: ...
    @overload
    def faces(
        self,
        dim: int | Integer,
        codim: None = ...,
    ) -> ConeFaceTuple: ...
    @overload
    def faces(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> ConeFaceTuple: ...
    @overload
    def faces(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> ConeFacesByDimension: ...
    def facet_normals(self) -> IntegralPointCollection: ...
    def facet_of(self) -> ConeFaceTuple: ...
    def facets(self) -> ConeFaceTuple: ...
    def incidence_matrix(self) -> Matrix[Integer]: ...
    def intersection(
        self,
        other: ConvexRationalPolyhedralCone,
    ) -> RationalCone: ...
    __and__ = intersection
    def is_equivalent(
        self,
        other: ConvexRationalPolyhedralCone,
    ) -> bool: ...
    def is_face_of(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> bool: ...
    def is_isomorphic(
        self,
        other: ConvexRationalPolyhedralCone,
    ) -> bool: ...
    def is_simplicial(self) -> bool: ...
    def is_smooth(self) -> bool: ...
    def is_empty(self) -> bool: ...
    def is_trivial(self) -> bool: ...
    def is_strictly_convex(self) -> bool: ...
    is_pointed = is_strictly_convex
    def linear_subspace(self) -> FreeModule_generic_field[Rational]: ...
    def lines(self) -> PointCollection[_Ray, _Lattice, Integer]: ...
    def polyhedron(self) -> Polyhedron_base: ...
    def an_affine_basis(
        self,
    ) -> tuple[FreeModuleElement[RingElement], ...]: ...
    def strict_quotient(self) -> RationalCone: ...
    def solid_restriction(self) -> RationalCone: ...
    def _split_ambient_lattice(self) -> None: ...
    def sublattice(self) -> ToricLattice_sublattice_with_basis: ...
    def sublattice_quotient(self) -> ToricLattice_quotient: ...
    def sublattice_complement(
        self,
    ) -> ToricLattice_sublattice_with_basis: ...
    def orthogonal_sublattice(self) -> ToricLattice_sublattice: ...
    def relative_quotient(
        self,
        subcone: ConvexRationalPolyhedralCone,
    ) -> RationalCone: ...
    def relative_orthogonal_quotient(
        self,
        supercone: ConvexRationalPolyhedralCone,
    ) -> RationalCone: ...
    def semigroup_generators(self) -> IntegralPointCollection: ...
    def Hilbert_basis(self) -> IntegralPointCollection: ...
    def Hilbert_coefficients(
        self,
        point: object,
        solver: str | None = ...,
        verbose: bool = ...,
    ) -> FreeModuleElement[Integer]: ...
    def is_solid(self) -> bool: ...
    def is_proper(self) -> bool: ...
    def is_full_space(self) -> bool: ...
    def lineality(self) -> int: ...
    def is_relatively_open(self) -> bool: ...
    def discrete_complementarity_set(self) -> object: ...
    def lyapunov_like_basis(self) -> list[Matrix[Rational]]: ...
    def lyapunov_rank(self) -> int: ...
    @overload
    def random_element(
        self,
        ring: IntegerRing_class = ...,
    ) -> _Ray: ...
    @overload
    def random_element(
        self,
        ring: RationalField,
    ) -> FreeModuleElement[Rational]: ...
    def positive_operators_gens(
        self,
        K2: ConvexRationalPolyhedralCone | None = ...,
    ) -> list[Matrix[Rational]]: ...
    def _cross_positive_operators_dual(self) -> RationalCone: ...
    def cross_positive_operators_gens(self) -> list[Matrix[Rational]]: ...
    def Z_operators_gens(self) -> list[Matrix[Rational]]: ...
    def max_angle(
        self,
        other: ConvexRationalPolyhedralCone | None = ...,
        exact: bool = ...,
        epsilon: RingElement | int | float = ...,
    ) -> RingElement | float: ...
    def irreducible_factors(self) -> ConeFaceTuple: ...
    def is_reducible(self) -> bool: ...
