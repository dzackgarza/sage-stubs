from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.map import Map
from sage.rings.morphism import RingHomomorphism
from sage.rings.polynomial.ore_polynomial_ring import OrePolynomialRing
from sage.rings.ring import Ring
from sage.structure.element import RingElement


class OreModules(Category_over_base_ring[RingElement]):
    @staticmethod
    def __classcall_private__(
        cls: type[OreModules],
        ring: Ring,
        twist: Map | OrePolynomialRing,
    ) -> OreModules: ...
    def __init__(self, ore: OrePolynomialRing) -> None: ...
    def __reduce__(
        self,
    ) -> tuple[
        type[OreModules],
        tuple[Ring, OrePolynomialRing],
    ]: ...
    def super_categories(self) -> list[Category]: ...
    def _repr_object_names(self) -> str: ...
    def ore_ring(self, var: str = ...) -> OrePolynomialRing: ...
    def twisting_morphism(self) -> RingHomomorphism | None: ...
    def twisting_derivation(self) -> Map | None: ...
