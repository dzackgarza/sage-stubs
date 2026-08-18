from collections.abc import Sequence
from typing import TypeVar

from sage.geometry.polyhedron.base import Polyhedron_base
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import FieldElement, RingElement

_RingScalar = TypeVar("_RingScalar", bound=RingElement)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)

def plane_inequality(
    v: Sequence[_RingScalar | int]
    | FreeModuleElement[_RingScalar],
) -> list[_RingScalar | int]: ...
def jacobi(M: Matrix[_FieldScalar]) -> Matrix[_FieldScalar]: ...
def diamond_cut(
    V: Polyhedron_base,
    GM: Matrix[_RingScalar],
    C: _RingScalar | int | float,
    verbose: bool = ...,
) -> Polyhedron_base: ...
def calculate_voronoi_cell(
    basis: Matrix[_RingScalar],
    radius: _RingScalar | int | float | None = ...,
    verbose: bool = ...,
) -> Polyhedron_base: ...
