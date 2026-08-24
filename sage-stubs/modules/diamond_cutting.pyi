from collections.abc import Sequence
from typing import TypeVar, overload

from sage.geometry.polyhedron.base import Polyhedron_base
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import FieldElement, RingElement
from sage.structure.parent import ElementConstructorInput

_RingScalar = TypeVar("_RingScalar", bound=RingElement)
_FieldScalar = TypeVar("_FieldScalar", bound=FieldElement)


@overload
def plane_inequality(
    v: FreeModuleElement[_RingScalar],
) -> list[_RingScalar]: ...
@overload
def plane_inequality(
    v: Sequence[ElementConstructorInput],
) -> list[RingElement]: ...
def jacobi(M: Matrix[_FieldScalar]) -> Matrix[_FieldScalar]: ...
def diamond_cut(
    V: Polyhedron_base,
    GM: Matrix[_RingScalar],
    C: RingElement | int | float,
    verbose: bool = ...,
) -> Polyhedron_base: ...
def calculate_voronoi_cell(
    basis: Matrix[_RingScalar],
    radius: RingElement | int | float | None = ...,
    verbose: bool = ...,
) -> Polyhedron_base: ...
