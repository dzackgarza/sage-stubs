import builtins
from collections.abc import (
    Hashable,
)

from sage.geometry.voronoi_diagram import VoronoiDiagram
from sage.rings.number_field.number_field import NumberField
from sage.structure.element import Element

class _SageObject: ...

roots_interval_cache: _SageObject

def braid_from_piecewise(self) -> _SageObject: ...
def discrim(self) -> tuple[Element, ...]: ...
def corrected_voronoi_diagram(self) -> VoronoiDiagram: ...
def orient_circuit(
    self,
    convex: builtins.bool = ...,
    precision: builtins.int = ...,
    verbose: builtins.bool = ...,
) -> tuple[Element, ...]: ...
def voronoi_cells(
    self, vertical_lines: builtins.object = ...
) -> tuple[Element, ...]: ...
def followstrand(
    self,
    factors: builtins.object,
    x0: builtins.object,
    x1: builtins.object,
    y0a: builtins.object,
    prec: builtins.int = ...,
) -> list[tuple]: ...
def newton(self, x0: builtins.object, i0: builtins.object) -> _SageObject: ...
def fieldI(self) -> NumberField: ...
def roots_interval(self, x0: builtins.object) -> dict[Hashable, Element]: ...
def roots_interval_cached(self, x0: builtins.object) -> dict[Hashable, Element]: ...
def populate_roots_interval_cache(self) -> None: ...
def braid_in_segment(
    self,
    x0: builtins.object,
    x1: builtins.object,
    precision: builtins.dict[_SageObject, _SageObject] = ...,
) -> _SageObject: ...
def geometric_basis(
    self,
    E: builtins.object,
    EC0: builtins.object,
    p: builtins.int,
    dual_graph: builtins.object,
    vertical_regions: builtins.dict[_SageObject, _SageObject] = ...,
) -> tuple[list, dict]: ...
def vertical_lines_in_braidmon(self) -> list[int]: ...
def strand_components(
    self, pols: builtins.object, p1: builtins.object
) -> tuple[list, dict]: ...
def braid_monodromy(
    self,
    arrangement: builtins.tuple[_SageObject, ...] = ...,
    vertical: builtins.bool = ...,
) -> tuple[Element, ...]: ...
def conjugate_positive_form(self) -> list[list]: ...
def conjugate_positive_form_p(self) -> _SageObject: ...
def braid2rels(self) -> list[Element]: ...
def braid2rels_p(self) -> _SageObject: ...
def relation(self, b: builtins.object) -> _SageObject: ...
def fundamental_group_from_braid_mon(
    self,
    degree: builtins.int = ...,
    simplified: builtins.bool = ...,
    projective: builtins.bool = ...,
    puiseux: builtins.bool = ...,
    vertical: builtins.list[_SageObject] = ...,
) -> _SageObject: ...
def fundamental_group(
    self,
    simplified: builtins.bool = ...,
    projective: builtins.bool = ...,
    puiseux: builtins.bool = ...,
) -> _SageObject: ...
def fundamental_group_arrangement(
    self,
    simplified: builtins.bool = ...,
    projective: builtins.bool = ...,
    puiseux: builtins.bool = ...,
    vertical: builtins.bool = ...,
    braid_data: builtins.object = ...,
) -> _SageObject: ...
