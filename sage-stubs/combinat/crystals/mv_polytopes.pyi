from collections.abc import Iterable

from sage.combinat.crystals.pbw_crystal import (
    PBWCrystal,
    PBWCrystalElement,
)
from sage.combinat.crystals.pbw_datum import CartanIndex
from sage.combinat.root_system.cartan_type import CartanType_abstract
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.structure.element import Element
from sage.structure.parent import Parent

class MVPolytope(PBWCrystalElement):
    def parent(self) -> MVPolytopes: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _polytope_vertices(
        self,
        P: Parent,
    ) -> list[Element]: ...
    def polytope(
        self,
        P: Parent | None = ...,
    ) -> Polyhedron_base: ...
    def plot(
        self,
        P: Parent | None = ...,
        **options: object,
    ) -> Graphics: ...

class MVPolytopes(PBWCrystal):
    Element: type[MVPolytope]
    element_class: type[MVPolytope]
    module_generators: tuple[MVPolytope, ...]

    def __init__(self, cartan_type: CartanType_abstract) -> None: ...
    def _repr_(self) -> str: ...
    def _element_constructor_(
        self,
        lusztig_datum: Iterable[int | Integer],
        long_word: Iterable[CartanIndex] | None = ...,
    ) -> MVPolytope: ...
    def highest_weight_vector(self) -> MVPolytope: ...
    def set_latex_options(
        self,
        *,
        projection: object = ...,
        mark_endpoints: bool = ...,
        P: Parent | None = ...,
        circle_size: float = ...,
    ) -> None: ...
    def latex_options(self) -> dict[str, object]: ...
