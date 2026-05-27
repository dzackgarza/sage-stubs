from collections.abc import Mapping, Sequence
from typing import Protocol, TypeAlias

from sage.manifolds.chart import Chart
from sage.manifolds.manifold import TopologicalManifold
from sage.manifolds.subset import ManifoldSubset
from sage.plot.graphics import Graphics
from sage.plot.plot3d.base import Graphics3d
from sage.structure.element import Element, Expression

_Scalar: TypeAlias = Element | Expression | int | float | complex | str
_Coordinates: TypeAlias = tuple[_Scalar, ...]
_CoordinateInput: TypeAlias = Sequence[_Scalar]
_Parameters: TypeAlias = Mapping[Expression, _Scalar]

class _PointMap(Protocol):
    def __call__(self, point: ManifoldPoint) -> ManifoldPoint: ...

class ManifoldPoint(Element):
    _manifold: TopologicalManifold
    _coordinates: dict[Chart, _Coordinates]
    _name: str | None
    _latex_name: str | None

    def __init__(
        self,
        parent: ManifoldSubset,
        coords: _CoordinateInput | None = None,
        chart: Chart | None = None,
        name: str | None = None,
        latex_name: str | None = None,
        check_coords: bool = True,
    ) -> None: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def coordinates(
        self, chart: Chart | None = None, old_chart: Chart | None = None
    ) -> _Coordinates: ...
    def coord(self, chart: Chart | None = None, old_chart: Chart | None = None) -> _Coordinates: ...
    def set_coordinates(
        self, coords: _CoordinateInput, chart: Chart | None = None
    ) -> None: ...
    def set_coord(self, coords: _CoordinateInput, chart: Chart | None = None) -> None: ...
    def add_coordinates(
        self, coords: _CoordinateInput, chart: Chart | None = None
    ) -> None: ...
    def add_coord(self, coords: _CoordinateInput, chart: Chart | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def plot(
        self,
        chart: Chart | None = None,
        ambient_coords: Sequence[Expression] | None = None,
        mapping: _PointMap | None = None,
        label: str | None = None,
        parameters: _Parameters | None = None,
        **kwds: _Scalar | None,
    ) -> Graphics | Graphics3d: ...
