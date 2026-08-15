from typing import TYPE_CHECKING, Optional

from sage.manifolds.chart import Chart
from sage.manifolds.manifold import TopologicalManifold
class ScalarField:
    
    _name: str | None
    _latex_name: str | None
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _is_zero: bool
    _express: dict

    def __init__(
        self,
        parent,
        coord_expression=None,
        chart: Chart | None = None,
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

    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

    def _init_derived(self) -> None: ...
    def _del_derived(self) -> None: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

    def set_name(self, name: str | None = None, latex_name: str | None = None) -> None: ...

    def domain(self) -> TopologicalManifold:
        
        ...

    def codomain(self):
        
        ...

    def copy(self, name: str | None = None, latex_name: str | None = None) -> ScalarField:
        
        ...

    def copy_from(self, other: ScalarField) -> None:
        
        ...

    def coord_function(self, chart: Chart | None = None, from_chart: Chart | None = None):
        
        ...

    def expr(self, chart: Chart | None = None, from_chart: Chart | None = None):
        
        ...

    def set_expr(self, coord_expression, chart: Chart | None = None) -> None:
        
        ...

    def add_expr(self, coord_expression, chart: Chart | None = None) -> None:
        
        ...

    def add_expr_by_continuation(self, chart: Chart, subdomain: TopologicalManifold) -> None:
        
        ...

    def display(self, chart: Chart | None = None):
        
        ...

    def restrict(self, subdomain: TopologicalManifold) -> ScalarField:
        
        ...

    def common_charts(self, other: ScalarField):
        
        ...
