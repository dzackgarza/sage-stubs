from collections.abc import Callable, Container, Iterable, Iterator
from typing import Generic, Self, TypeVar, overload

from sage.combinat.posets.posets import FinitePoset
from sage.geometry.cone import (
    ConeInput,
    ConeRayInput,
    ConvexRationalPolyhedralCone,
    IntegralRayCollection,
    LatticeInput,
)
from sage.geometry.point_collection import PointCollection
from sage.geometry.toric_lattice import ToricLattice_generic
from sage.geometry.toric_lattice_element import ToricLatticeElement, ToricPlot
from sage.graphs.graph import Graph
from sage.homology.chain_complex import ChainComplex_class
from sage.interfaces.expect import Expect
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.modules.free_module import FreeModule_generic_pid
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.schemes.toric.variety import ToricVariety_field
from sage.structure.formal_sum import FormalSum

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

type FanConeIndex = int | Integer
type FanConeIndices = Iterable[FanConeIndex]
type FanConeInput = ConvexRationalPolyhedralCone | FanConeIndices
type FanConesInput = Iterable[FanConeInput]
type FanRaysInput = ConeInput | None
type FanConeTuple = tuple[Cone_of_fan, ...]
type FanConesByDimension = tuple[FanConeTuple, ...]


def Fan(
    cones: FanConesInput,
    rays: FanRaysInput = ...,
    lattice: LatticeInput | None = ...,
    check: bool = ...,
    normalize: bool = ...,
    is_complete: bool | None = ...,
    virtual_rays: FanRaysInput = ...,
    discard_faces: bool = ...,
    allow_arrangement: bool = ...,
) -> RationalPolyhedralFan: ...


def FaceFan(
    polytope: object,
    lattice: LatticeInput | None = ...,
) -> RationalPolyhedralFan: ...


def NormalFan(
    polytope: object,
    lattice: LatticeInput | None = ...,
) -> RationalPolyhedralFan: ...


def Fan2d(
    rays: ConeInput,
    lattice: LatticeInput | None = ...,
) -> RationalPolyhedralFan: ...


def discard_faces(
    cones: Iterable[ConvexRationalPolyhedralCone],
) -> list[ConvexRationalPolyhedralCone]: ...


def _refine_arrangement_to_fan(
    cones: Iterable[ConvexRationalPolyhedralCone],
) -> list[ConvexRationalPolyhedralCone]: ...


class Cone_of_fan(
    ConvexRationalPolyhedralCone[_Ray, _Lattice],
    Generic[_Ray, _Lattice],
):
    def __init__(
        self,
        ambient: RationalPolyhedralFan[_Ray, _Lattice],
        ambient_ray_indices: Iterable[int | Integer],
    ) -> None: ...
    def _repr_(self) -> str: ...
    def ambient(self) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def star_generator_indices(self) -> tuple[int, ...]: ...
    def star_generators(
        self,
    ) -> tuple[Cone_of_fan[_Ray, _Lattice], ...]: ...


class RationalPolyhedralFan(
    IntegralRayCollection[_Ray, _Lattice],
    Callable[..., object],
    Container[object],
    Generic[_Ray, _Lattice],
):
    def __init__(
        self,
        cones: Iterable[Iterable[int | Integer]],
        rays: Iterable[_Ray],
        lattice: _Lattice,
        is_complete: bool | None = ...,
        virtual_rays: Iterable[_Ray] | None = ...,
    ) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    @overload
    def __call__(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> Self: ...
    @overload
    def __call__(
        self,
        dim: int | Integer,
        codim: None = ...,
    ) -> tuple[Cone_of_fan[_Ray, _Lattice], ...]: ...
    @overload
    def __call__(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> tuple[Cone_of_fan[_Ray, _Lattice], ...]: ...
    def __richcmp__(
        self,
        other: object,
        op: int,
    ) -> bool: ...
    def _sage_input_(
        self,
        sib: object,
        coerced: bool,
    ) -> object: ...
    def _macaulay2_init_(
        self,
        macaulay2: Expect | None = ...,
    ) -> object: ...
    def __iter__(
        self,
    ) -> Iterator[Cone_of_fan[_Ray, _Lattice]]: ...
    def _compute_cone_lattice(self) -> None: ...
    def _contains(
        self,
        cone: object,
    ) -> bool: ...
    def support_contains(self, *point: object) -> bool: ...
    def cartesian_product(
        self,
        other: RationalPolyhedralFan,
        lattice: FreeModule_generic_pid[Integer] | None = ...,
    ) -> RationalPolyhedralFan: ...
    def __neg__(self) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def common_refinement(
        self,
        other: RationalPolyhedralFan,
    ) -> RationalPolyhedralFan: ...
    def _latex_(self) -> str: ...
    @overload
    def _ray_to_cones(
        self,
        i: None = ...,
    ) -> tuple[frozenset[int], ...]: ...
    @overload
    def _ray_to_cones(
        self,
        i: int | Integer,
    ) -> frozenset[int]: ...
    def _repr_(self) -> str: ...
    def _subdivide_stellar(
        self,
        new_rays: Iterable[_Ray],
        verbose: bool,
    ) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def cone_containing(
        self,
        *points: object,
    ) -> Cone_of_fan[_Ray, _Lattice]: ...
    def cone_lattice(self) -> FinitePoset: ...
    def f_vector(self) -> tuple[int, ...]: ...
    def __getstate__(self) -> dict[str, object]: ...
    @overload
    def cones(
        self,
        dim: int | Integer,
        codim: None = ...,
    ) -> tuple[Cone_of_fan[_Ray, _Lattice], ...]: ...
    @overload
    def cones(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> tuple[Cone_of_fan[_Ray, _Lattice], ...]: ...
    @overload
    def cones(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> tuple[tuple[Cone_of_fan[_Ray, _Lattice], ...], ...]: ...
    def contains(
        self,
        cone: object,
    ) -> bool: ...
    def embed(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> Cone_of_fan[_Ray, _Lattice]: ...
    def Gale_transform(self) -> Matrix_integer_dense: ...
    def is_polytopal(self) -> bool: ...
    def generating_cone(
        self,
        n: int | Integer,
    ) -> Cone_of_fan[_Ray, _Lattice]: ...
    def generating_cones(
        self,
    ) -> tuple[Cone_of_fan[_Ray, _Lattice], ...]: ...
    def vertex_graph(self) -> Graph: ...
    def is_complete(self) -> bool: ...
    def is_equivalent(
        self,
        other: RationalPolyhedralFan,
    ) -> bool: ...
    def is_isomorphic(
        self,
        other: RationalPolyhedralFan,
    ) -> bool: ...
    def _2d_echelon_forms(
        self,
    ) -> frozenset[Matrix_integer_dense]: ...
    def _2d_echelon_form(self) -> Matrix_integer_dense: ...
    def isomorphism(
        self,
        other: RationalPolyhedralFan,
    ) -> FanMorphism: ...
    def is_simplicial(self) -> bool: ...
    def is_smooth(
        self,
        codim: int | Integer | None = ...,
    ) -> bool: ...
    def make_simplicial(
        self,
        **kwds: object,
    ) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def n_generating_cones(self) -> int: ...
    ngenerating_cones = n_generating_cones
    def plot(self, **options: object) -> ToricPlot: ...
    def subdivide(
        self,
        new_rays: Iterable[ConeRayInput] | None = ...,
        make_simplicial: bool = ...,
        algorithm: str = ...,
        verbose: bool = ...,
    ) -> RationalPolyhedralFan: ...
    def virtual_rays(
        self,
        *indices: int | Integer | Iterable[int | Integer],
    ) -> PointCollection[_Ray, _Lattice, Integer]: ...
    def primitive_collections(self) -> list[frozenset[int]]: ...
    def Stanley_Reisner_ideal(
        self,
        ring: Ring,
    ) -> Ideal_generic: ...
    def linear_equivalence_ideal(
        self,
        ring: Ring,
    ) -> Ideal_generic: ...
    def oriented_boundary(
        self,
        cone: Cone_of_fan[_Ray, _Lattice]
        | RationalPolyhedralFan[_Ray, _Lattice],
    ) -> FormalSum: ...
    def toric_variety(
        self,
        *args: object,
        **kwds: object,
    ) -> ToricVariety_field: ...
    def complex(
        self,
        base_ring: Ring = ...,
        extended: bool = ...,
    ) -> ChainComplex_class: ...


from sage.geometry.fan_morphism import FanMorphism
