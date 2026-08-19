from collections.abc import Sequence
from typing import Never, Self, overload

from sage.modules.free_module_element import FreeModuleElement
from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.plot.graphics import Graphics
from sage.plot.plot3d.base import Graphics3d
from sage.rings.integer import Integer


type ToricPlot = Graphics | Graphics3d


class ToricLatticeElement(Vector_integer_dense):
    def parent(self) -> ToricLattice_generic: ...
    def __richcmp__(
        self,
        other: ToricLatticeElement,
        op: int,
    ) -> bool: ...
    def __hash__(self) -> int: ...
    @overload
    def _act_on_(
        self,
        other: ToricLatticeElement,
        self_on_left: bool,
    ) -> Integer: ...
    @overload
    def _act_on_(
        self,
        other: Vector_integer_dense,
        self_on_left: bool,
    ) -> Integer: ...
    @overload
    def _act_on_(
        self,
        other: object,
        self_on_left: bool,
    ) -> object: ...
    def _dot_product_(
        self,
        right: FreeModuleElement,
    ) -> Never: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def __reduce__(
        self,
    ) -> tuple[object, tuple[object, ...]]: ...
    def plot(self, **options: object) -> ToricPlot: ...
    def __neg__(self) -> Self: ...
    def _add_(self, other: ToricLatticeElement) -> Self: ...
    def _sub_(self, other: ToricLatticeElement) -> Self: ...
    def _rmul_(self, scalar: int | Integer) -> Self: ...
    def _lmul_(self, scalar: int | Integer) -> Self: ...


def unpickle_v1(
    parent: ToricLattice_generic,
    entries: Sequence[int | Integer],
    degree: int,
    immutable: bool,
) -> ToricLatticeElement: ...


from sage.geometry.toric_lattice import ToricLattice_generic
