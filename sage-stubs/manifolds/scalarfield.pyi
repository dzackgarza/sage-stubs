from collections.abc import Mapping
from typing import TypeAlias

from sage.manifolds.chart import Chart
from sage.manifolds.chart_func import ChartFunction
from sage.manifolds.manifold import TopologicalManifold
from sage.manifolds.scalarfield_algebra import ScalarFieldAlgebra
from sage.rings.ring import Field
from sage.structure.element import CommutativeAlgebraElement, Element, Expression, ModuleElementWithMutability
from sage.tensor.modules.format_utilities import FormattedExpansion

_ScalarExpression: TypeAlias = Element | Expression | int | float | complex | str
_ChartExpression: TypeAlias = _ScalarExpression | ChartFunction
_CoordinateExpression: TypeAlias = _ChartExpression | Mapping[Chart, _ChartExpression]
_ChartSelector: TypeAlias = Chart | str | None

class ScalarField(CommutativeAlgebraElement, ModuleElementWithMutability):
    _name: str | None
    _latex_name: str | None
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _is_zero: bool
    _express: dict[Chart, ChartFunction]

    def __init__(
        self,
        parent: ScalarFieldAlgebra,
        coord_expression: _CoordinateExpression | None = None,
        chart: _ChartSelector = None,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...

    def __bool__(self) -> bool: ...

    def is_trivial_zero(self) -> bool:
        
        ...

    def is_trivial_one(self) -> bool:
        
        ...

    def is_unit(self) -> bool:
        
        ...

    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

    def _init_derived(self) -> None: ...
    def _del_derived(self) -> None: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

    def set_name(self, name: str | None = None, latex_name: str | None = None) -> None: ...

    def domain(self) -> TopologicalManifold:
        
        ...

    def codomain(self) -> Field:
        
        ...

    def copy(self, name: str | None = None, latex_name: str | None = None) -> ScalarField:
        
        ...

    def copy_from(self, other: ScalarField) -> None:
        
        ...

    def coord_function(self, chart: Chart | None = None, from_chart: Chart | None = None) -> ChartFunction:
        
        ...

    def expr(self, chart: Chart | None = None, from_chart: Chart | None = None) -> Expression:
        
        ...

    def set_expr(self, coord_expression: _ScalarExpression, chart: Chart | None = None) -> None:
        
        ...

    def add_expr(self, coord_expression: _ScalarExpression, chart: Chart | None = None) -> None:
        
        ...

    def add_expr_by_continuation(self, chart: Chart, subdomain: TopologicalManifold) -> None:
        
        ...

    def set_restriction(self, rst: ScalarField) -> None: ...

    def display(self, chart: Chart | None = None) -> FormattedExpansion:
        
        ...

    def restrict(self, subdomain: TopologicalManifold) -> ScalarField:
        
        ...

    def common_charts(self, other: ScalarField) -> list[Chart] | None:
        
        ...
