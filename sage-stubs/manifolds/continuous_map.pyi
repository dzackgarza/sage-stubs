from collections.abc import Mapping, Sequence
from typing import TypeAlias

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.manifolds.chart import Chart
from sage.manifolds.chart_func import MultiCoordFunction
from sage.manifolds.manifold import TopologicalManifold
from sage.manifolds.subset import ManifoldSubset
from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
from sage.structure.element import Element, Expression
from sage.tensor.modules.format_utilities import FormattedExpansion

from .continuous_map_image import ImageManifoldSubset
from .point import ManifoldPoint

_Scalar: TypeAlias = Element | Expression | int | float | complex | str
_CoordinateExpression: TypeAlias = _Scalar | Sequence[_Scalar]
_CoordinateFunctions: TypeAlias = Mapping[tuple[Chart, Chart], _CoordinateExpression]

class ContinuousMap(Morphism):
    _domain: TopologicalManifold
    _codomain: TopologicalManifold
    _coord_expression: dict[tuple[Chart, Chart], MultiCoordFunction]
    _is_isomorphism: bool
    _is_identity: bool
    _name: str | None
    _latex_name: str | None
    _restrictions: dict[tuple[TopologicalManifold, TopologicalManifold], ContinuousMap]
    _restrictions_graph: dict[tuple[TopologicalManifold, TopologicalManifold], ContinuousMap]
    _extensions_graph: dict[tuple[TopologicalManifold, TopologicalManifold], ContinuousMap]
    _inverse: ContinuousMap | None

    def __init__(
        self,
        parent: Homset[TopologicalManifold, TopologicalManifold],
        coord_functions: _CoordinateFunctions | None = None,
        name: str | None = None,
        latex_name: str | None = None,
        is_isomorphism: bool = False,
        is_identity: bool = False,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def _call_(self, point: ManifoldPoint) -> ManifoldPoint: ...
    def is_identity(self) -> bool: ...
    def _composition_(
        self,
        other: ContinuousMap,
        homset: Homset[TopologicalManifold, TopologicalManifold],
    ) -> ContinuousMap: ...
    def image(
        self,
        subset: ManifoldSubset | None = None,
        inverse: ContinuousMap | None = None,
    ) -> ImageManifoldSubset | ManifoldSubset: ...
    def preimage(
        self,
        codomain_subset: ManifoldSubset,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> TopologicalManifold | ManifoldSubset | ManifoldSubsetPullback: ...
    pullback = preimage
    def _mul_(self, other: ContinuousMap) -> ContinuousMap: ...
    def _init_derived(self) -> None: ...
    def _del_derived(self) -> None: ...
    def display(
        self, chart1: Chart | None = None, chart2: Chart | None = None
    ) -> FormattedExpansion: ...
    disp = display
    def coord_functions(
        self, chart1: Chart | None = None, chart2: Chart | None = None
    ) -> MultiCoordFunction: ...
    def expr(
        self, chart1: Chart | None = None, chart2: Chart | None = None
    ) -> tuple[Expression, ...]: ...
    expression = expr
    def set_expr(
        self,
        chart1: Chart,
        chart2: Chart,
        coord_functions: _CoordinateExpression,
    ) -> None: ...
    set_expression = set_expr
    def add_expr(
        self,
        chart1: Chart,
        chart2: Chart,
        coord_functions: _CoordinateExpression,
    ) -> None: ...
    add_expression = add_expr
    def restrict(
        self,
        subdomain: TopologicalManifold,
        subcodomain: TopologicalManifold | None = None,
    ) -> ContinuousMap: ...
    def __invert__(self) -> ContinuousMap: ...
    inverse = __invert__
