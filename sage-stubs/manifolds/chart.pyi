from collections.abc import Callable, Mapping, Sequence
from typing import Protocol, TypeAlias, overload

from sage.manifolds.calculus_method import CalculusMethod
from sage.manifolds.chart_func import ChartFunction, ChartFunctionRing, MultiCoordFunction
from sage.manifolds.manifold import TopologicalManifold
from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
from sage.sets.condition_set import ConditionSet
from sage.structure.element import Element, Expression

_Scalar: TypeAlias = Element | Expression | int | float | complex | str
_Period: TypeAlias = Element | Expression | int | float | complex | tuple[_Scalar, _Scalar] | None
_Coordinates: TypeAlias = tuple[Expression, ...]
_RestrictionClause: TypeAlias = Expression | Sequence[Expression] | tuple[Expression, ...] | frozenset[Expression]
_RestrictionInput: TypeAlias = (
    _RestrictionClause | Callable[..., _RestrictionClause] | None
)
_Parameters: TypeAlias = Mapping[Expression, _Scalar]
_Substitutions: TypeAlias = Mapping[Expression, _Scalar]
_CoordinateTransformations: TypeAlias = Expression | Sequence[Expression]

class _VectorSpaceCodomain(Protocol):
    def dimension(self) -> int: ...

_ChartCodomain: TypeAlias = _VectorSpaceCodomain | ConditionSet

class _CoordinatePoint(Protocol):
    def coord(self, chart: Chart) -> tuple[_Scalar, ...]: ...

class _CoordinateSubset(Protocol):
    def __contains__(self, coordinate_vector: tuple[_Scalar, ...]) -> bool: ...

class CoordChange:
    def __init__(self, chart1: Chart, chart2: Chart, *transformations: Expression) -> None: ...
    def inverse(self) -> CoordChange: ...
    def display(self) -> str: ...

class Chart:
    
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _sindex: int
    _xx: _Coordinates
    _periods: tuple[_Period, ...] | None
    _restrictions: frozenset[_RestrictionClause]

    @staticmethod
    def __classcall__(
        cls: type[Chart],
        domain: TopologicalManifold,
        coordinates: str = "",
        calc_method: str | None = None,
        names: Sequence[str] | None = None,
        coord_restrictions: _RestrictionInput = None,
        **coordinate_options: tuple[_Period, ...],
    ) -> Chart: ...

    def __init__(
        self,
        domain: TopologicalManifold,
        coordinates: _Coordinates,
        calc_method: str | None = None,
        periods: tuple[_Period, ...] | None = None,
        coord_restrictions: frozenset[_RestrictionClause] | None = None,
    ) -> None: ...

    @classmethod
    def _parse_coordinates(
        cls, domain: TopologicalManifold, coordinates: str | Sequence[str]
    ) -> tuple[_Coordinates, dict[str, tuple[_Period, ...]]]: ...

    @staticmethod
    def _normalize_coord_restrictions(
        coordinates: _Coordinates, coord_restrictions: _RestrictionInput
    ) -> frozenset[_RestrictionClause]: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _first_ngens(self, n: int) -> _Coordinates: ...
    @overload
    def __getitem__(self, i: slice) -> _Coordinates: ...
    @overload
    def __getitem__(self, i: int) -> Expression: ...

    def __call__(self, point: _CoordinatePoint) -> tuple[_Scalar, ...]: ...

    def domain(self) -> TopologicalManifold: ...

    def manifold(self) -> TopologicalManifold: ...

    def periods(self) -> tuple[_Period, ...] | None: ...

    def add_restrictions(self, restrictions: _RestrictionInput) -> None: ...

    def restrict(
        self, subset: TopologicalManifold, restrictions: _RestrictionInput = None
    ) -> Chart: ...

    def valid_coordinates(
        self, *coordinates: _Scalar, parameters: _Parameters | None = None
    ) -> bool: ...

    def _check_restrictions(
        self, restrict: _RestrictionClause, substitutions: _Substitutions
    ) -> bool: ...

    def codomain(self) -> _ChartCodomain: ...

    def _restrict_set(
        self,
        universe: _VectorSpaceCodomain,
        coord_restrictions: _RestrictionClause,
    ) -> _ChartCodomain: ...

    def transition_map(
        self,
        other: Chart,
        transformations: _CoordinateTransformations,
        intersection_name: str | None = None,
        restrictions1: _RestrictionInput = None,
        restrictions2: _RestrictionInput = None,
    ) -> CoordChange: ...

    def preimage(
        self,
        codomain_subset: _CoordinateSubset,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> ManifoldSubsetPullback: ...

    def pullback(
        self,
        codomain_subset: _CoordinateSubset,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> ManifoldSubsetPullback: ...

    def function_ring(self) -> ChartFunctionRing: ...

    def function(
        self,
        expression: _Scalar,
        calc_method: str | None = None,
        expansion_symbol: Expression | None = None,
        order: int | None = None,
    ) -> ChartFunction: ...

    def zero_function(self) -> ChartFunction: ...

    def one_function(self) -> ChartFunction: ...

    def calculus_method(self) -> CalculusMethod: ...

    def multifunction(self, *expressions: _Scalar) -> MultiCoordFunction: ...


class RealChart(Chart):
    ...
