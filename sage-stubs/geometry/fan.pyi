from collections.abc import Container, Iterable, Iterator, Sequence
from typing import Generic, TypeVar, overload

from sage.combinat.posets.posets import FinitePoset
from sage.geometry.cone import ConvexRationalPolyhedralCone, IntegralRayCollection
from sage.geometry.lattice_polytope import LatticePolytopeClass
from sage.geometry.point_collection import PointCollection
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.geometry.toric_lattice import ToricLattice_generic
from sage.geometry.toric_lattice_element import ToricLatticeElement, ToricPlot
from sage.graphs.graph import Graph
from sage.homology.chain_complex import ChainComplex_class
from sage.interfaces.expect import Expect
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module import FreeModule_generic_pid
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.ideal import Ideal_generic
from sage.rings.integer import Integer
from sage.rings.ring import Ring
from sage.schemes.toric.variety import ToricVariety_field
from sage.structure.element import RingElement
from sage.structure.formal_sum import FormalSum
from sage.structure.parent import ElementConstructorInput

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

type FanRayInput = (
    FreeModuleElement[RingElement]
    | Sequence[ElementConstructorInput]
)
type FanRaysInput = Iterable[FanRayInput] | PointCollection
type FanConeInput = (
    ConvexRationalPolyhedralCone
    | Sequence[int | Integer]
)
type FanConesInput = Iterable[FanConeInput]
type FanPolytope = LatticePolytopeClass | Polyhedron_base
type FanConeTuple[
    _Ray: FreeModuleElement[Integer],
    _Lattice: FreeModule_generic_pid[Integer],
] = tuple[Cone_of_fan[_Ray, _Lattice], ...]
type FanConesByDimension[
    _Ray: FreeModuleElement[Integer],
    _Lattice: FreeModule_generic_pid[Integer],
] = tuple[FanConeTuple[_Ray, _Lattice], ...]

@overload
def Fan(
    cones: FanConesInput | ConvexRationalPolyhedralCone,
    rays: FanRaysInput | None = ...,
    lattice: ToricLattice_generic | None = ...,
    check: bool = ...,
    normalize: bool = ...,
    is_complete: bool | None = ...,
    virtual_rays: FanRaysInput | None = ...,
    discard_faces: bool = ...,
    allow_arrangement: bool = ...,
) -> RationalPolyhedralFan[ToricLatticeElement, ToricLattice_generic]: ...
@overload
def Fan(
    cones: FanConesInput | ConvexRationalPolyhedralCone,
    rays: FanRaysInput | None,
    lattice: _Lattice,
    check: bool = ...,
    normalize: bool = ...,
    is_complete: bool | None = ...,
    virtual_rays: FanRaysInput | None = ...,
    discard_faces: bool = ...,
    allow_arrangement: bool = ...,
) -> RationalPolyhedralFan[FreeModuleElement[Integer], _Lattice]: ...

@overload
def FaceFan(
    polytope: FanPolytope,
    lattice: ToricLattice_generic | None = ...,
) -> RationalPolyhedralFan[ToricLatticeElement, ToricLattice_generic]: ...
@overload
def FaceFan(
    polytope: FanPolytope,
    lattice: _Lattice,
) -> RationalPolyhedralFan[FreeModuleElement[Integer], _Lattice]: ...

@overload
def NormalFan(
    polytope: FanPolytope,
    lattice: ToricLattice_generic | None = ...,
) -> RationalPolyhedralFan[ToricLatticeElement, ToricLattice_generic]: ...
@overload
def NormalFan(
    polytope: FanPolytope,
    lattice: _Lattice,
) -> RationalPolyhedralFan[FreeModuleElement[Integer], _Lattice]: ...

@overload
def Fan2d(
    rays: FanRaysInput,
    lattice: ToricLattice_generic | None = ...,
) -> RationalPolyhedralFan[ToricLatticeElement, ToricLattice_generic]: ...
@overload
def Fan2d(
    rays: FanRaysInput,
    lattice: _Lattice,
) -> RationalPolyhedralFan[FreeModuleElement[Integer], _Lattice]: ...

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
        ambient_ray_indices: Iterable[int],
    ) -> None: ...
    def ambient(self) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def _repr_(self) -> str: ...
    def star_generator_indices(self) -> tuple[int, ...]: ...
    def star_generators(self) -> FanConeTuple[_Ray, _Lattice]: ...

class RationalPolyhedralFan(
    IntegralRayCollection[_Ray, _Lattice],
    Container[Cone_of_fan[_Ray, _Lattice]],
    Generic[_Ray, _Lattice],
):
    def __init__(
        self,
        cones: Iterable[Sequence[int | Integer]],
        rays: Iterable[_Ray],
        lattice: _Lattice,
        is_complete: bool | None = ...,
        virtual_rays: Iterable[_Ray] | PointCollection | None = ...,
    ) -> None: ...
    def __contains__(self, x: object) -> bool: ...
    def _sage_input_(
        self,
        sib: object,
        coerced: bool,
    ) -> object: ...
    def _macaulay2_init_(
        self,
        macaulay2: Expect | None = ...,
    ) -> str: ...
    def __iter__(self) -> Iterator[Cone_of_fan[_Ray, _Lattice]]: ...
    @overload
    def __call__(
        self,
        dim: int | Integer,
        codim: None = ...,
    ) -> FanConeTuple[_Ray, _Lattice]: ...
    @overload
    def __call__(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> FanConeTuple[_Ray, _Lattice]: ...
    @overload
    def __call__(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> FanConesByDimension[_Ray, _Lattice]: ...
    def _compute_cone_lattice(self) -> None: ...
    def _contains(self, cone: object) -> bool: ...
    def support_contains(self, *args: object) -> bool: ...
    def cartesian_product(
        self,
        other: RationalPolyhedralFan,
        lattice: FreeModule_generic_pid[Integer] | None = ...,
    ) -> RationalPolyhedralFan[
        FreeModuleElement[Integer],
        FreeModule_generic_pid[Integer],
    ]: ...
    def __neg__(self) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def common_refinement(
        self,
        other: RationalPolyhedralFan[_Ray, _Lattice],
    ) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    @overload
    def _ray_to_cones(self, i: None = ...) -> tuple[tuple[int, ...], ...]: ...
    @overload
    def _ray_to_cones(self, i: int | Integer) -> tuple[int, ...]: ...
    def _subdivide_stellar(
        self,
        new_rays: Iterable[_Ray] | PointCollection,
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
    ) -> FanConeTuple[_Ray, _Lattice]: ...
    @overload
    def cones(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> FanConeTuple[_Ray, _Lattice]: ...
    @overload
    def cones(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> FanConesByDimension[_Ray, _Lattice]: ...
    def contains(self, cone: object) -> bool: ...
    def embed(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> Cone_of_fan[_Ray, _Lattice]: ...
    def Gale_transform(self) -> Matrix[Integer]: ...
    def is_polytopal(self) -> bool: ...
    def generating_cone(
        self,
        n: int | Integer,
    ) -> Cone_of_fan[_Ray, _Lattice]: ...
    def generating_cones(self) -> FanConeTuple[_Ray, _Lattice]: ...
    def n_generating_cones(self) -> int: ...
    def vertex_graph(self) -> Graph: ...
    def is_complete(self) -> bool: ...
    def is_equivalent(self, other: object) -> bool: ...
    def is_isomorphic(self, other: object) -> bool: ...
    def _2d_echelon_forms(self) -> frozenset[Matrix[Integer]]: ...
    def _2d_echelon_form(self) -> Matrix[Integer]: ...
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
    def plot(self, **options: object) -> ToricPlot: ...
    def subdivide(
        self,
        new_rays: Iterable[_Ray] | PointCollection | None = ...,
        make_simplicial: bool = ...,
        algorithm: str = ...,
        verbose: bool = ...,
    ) -> RationalPolyhedralFan[_Ray, _Lattice]: ...
    def virtual_rays(
        self,
        *indices: int,
    ) -> PointCollection[_Ray, _Lattice, Integer]: ...
    def primitive_collections(self) -> list[frozenset[int]]: ...
    def Stanley_Reisner_ideal(self, ring: Ring) -> Ideal_generic: ...
    def linear_equivalence_ideal(self, ring: Ring) -> Ideal_generic: ...
    def oriented_boundary(
        self,
        cone: Cone_of_fan[_Ray, _Lattice] | RationalPolyhedralFan[_Ray, _Lattice],
    ) -> FormalSum: ...
    def toric_variety(
        self,
        *args: object,
        **kwds: object,
    ) -> ToricVariety_field: ...
    def complex(
        self,
        base_ring: Ring,
        extended: bool = ...,
    ) -> ChainComplex_class: ...

from sage.geometry.fan_morphism import FanMorphism
