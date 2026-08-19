from typing import Never, overload

from sage.geometry.cone import ConvexRationalPolyhedralCone
from sage.geometry.fan import Cone_of_fan, RationalPolyhedralFan
from sage.matrix.matrix import Matrix
from sage.modules.free_module import FreeModule_generic_pid
from sage.modules.free_module_morphism import FreeModuleMorphism
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer


type FanMorphismInput = (
    FreeModuleMorphism[Integer, Integer]
    | Matrix[Integer]
)
type FanMorphismCodomain = (
    RationalPolyhedralFan
    | FreeModule_generic_pid[Integer]
    | None
)
type FanConeTuple = tuple[Cone_of_fan, ...]


class FanMorphism(FreeModuleMorphism[Integer, Integer]):
    def __init__(
        self,
        morphism: FanMorphismInput,
        domain_fan: RationalPolyhedralFan,
        codomain: FanMorphismCodomain = ...,
        subdivide: bool = ...,
        check: bool = ...,
        verbose: bool = ...,
    ) -> None: ...
    def __mul__(self, right: FanMorphism) -> FanMorphism: ...
    def _RISGIS(self) -> tuple[frozenset[int], ...]: ...
    def _chambers(
        self,
    ) -> tuple[list[ConvexRationalPolyhedralCone], list[int]]: ...
    def _construct_codomain_fan(self, check: bool) -> None: ...
    def _latex_(self) -> str: ...
    def _ray_index_map(self) -> tuple[int | None, ...]: ...
    def _repr_(self) -> str: ...
    def _subdivide_domain_fan(
        self,
        check: bool,
        verbose: bool,
    ) -> None: ...
    def _support_error(self) -> Never: ...
    def _validate(self) -> None: ...
    @overload
    def codomain_fan(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> RationalPolyhedralFan: ...
    @overload
    def codomain_fan(
        self,
        dim: int | Integer,
        codim: None = ...,
    ) -> FanConeTuple: ...
    @overload
    def codomain_fan(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> FanConeTuple: ...
    @overload
    def domain_fan(
        self,
        dim: None = ...,
        codim: None = ...,
    ) -> RationalPolyhedralFan: ...
    @overload
    def domain_fan(
        self,
        dim: int | Integer,
        codim: None = ...,
    ) -> FanConeTuple: ...
    @overload
    def domain_fan(
        self,
        dim: None = ...,
        codim: int | Integer = ...,
    ) -> FanConeTuple: ...
    def image_cone(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> Cone_of_fan: ...
    def index(
        self,
        cone: ConvexRationalPolyhedralCone | None = ...,
    ) -> Integer | PlusInfinity: ...
    def is_birational(self) -> bool: ...
    def is_bundle(self) -> bool: ...
    def is_fibration(self) -> bool: ...
    def is_injective(self) -> bool: ...
    def is_surjective(self) -> bool: ...
    def is_dominant(self) -> bool: ...
    def kernel_fan(self) -> RationalPolyhedralFan: ...
    def preimage_cones(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> FanConeTuple: ...
    def preimage_fan(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> RationalPolyhedralFan: ...
    def primitive_preimage_cones(
        self,
        cone: ConvexRationalPolyhedralCone,
    ) -> FanConeTuple: ...
    def factor(
        self,
    ) -> tuple[FanMorphism, FanMorphism, FanMorphism]: ...
    def relative_star_generators(
        self,
        domain_cone: ConvexRationalPolyhedralCone,
    ) -> FanConeTuple: ...
