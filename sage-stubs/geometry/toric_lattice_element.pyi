from collections.abc import Sequence
from typing import Never

from sage.modules.vector_integer_dense import Vector_integer_dense
from sage.plot.graphics import Graphics
from sage.plot.plot3d.base import Graphics3d
from sage.rings.integer import Integer
from sage.structure.parent import ElementConstructorInput


type ToricPlot = Graphics | Graphics3d


class ToricLatticeElement(Vector_integer_dense):
    def parent(self) -> ToricLattice_generic: ...
    def __hash__(self) -> int: ...
    def _act_on_(
        self,
        other: object,
        self_on_left: bool,
    ) -> object: ...
    def _dot_product_(self, right: object) -> Never: ...
    def _latex_(self) -> str: ...
    def _repr_(self) -> str: ...
    def plot(self, **options: object) -> ToricPlot: ...


def unpickle_v1(
    parent: ToricLattice_generic,
    entries: Sequence[int | Integer | ElementConstructorInput],
    degree: int | Integer,
    immutable: bool,
) -> ToricLatticeElement: ...


from sage.geometry.toric_lattice import ToricLattice_generic
