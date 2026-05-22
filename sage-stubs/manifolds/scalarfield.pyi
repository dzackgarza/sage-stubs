from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from sage.manifolds.chart import Chart
    from sage.manifolds.manifold import TopologicalManifold

class ScalarField:
    """Scalar field on a topological manifold."""
    _name: Optional[str]
    _latex_name: Optional[str]
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _is_zero: bool
    _express: dict

    def __init__(
        self,
        parent,
        coord_expression=None,
        chart: Optional[Chart] = None,
        name: Optional[str] = None,
        latex_name: Optional[str] = None,
    ) -> None: ...

    def __bool__(self) -> bool: ...

    def is_trivial_zero(self) -> bool:
        """Check if self is trivially equal to zero without any simplification."""
        ...

    def is_trivial_one(self) -> bool:
        """Check if self is trivially equal to one without any simplification."""
        ...

    def is_unit(self) -> bool:
        """Return True iff self is not trivially zero in at least one expression."""
        ...

    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

    def _init_derived(self) -> None: ...
    def _del_derived(self) -> None: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...

    def set_name(self, name: Optional[str] = None, latex_name: Optional[str] = None) -> None: ...

    def domain(self) -> TopologicalManifold:
        """Return the open subset on which the scalar field is defined."""
        ...

    def codomain(self):
        """Return the codomain of the scalar field."""
        ...

    def copy(self, name: Optional[str] = None, latex_name: Optional[str] = None) -> ScalarField:
        """Return an exact copy of the scalar field."""
        ...

    def copy_from(self, other: ScalarField) -> None:
        """Make self a copy of other."""
        ...

    def coord_function(self, chart: Optional[Chart] = None, from_chart: Optional[Chart] = None):
        """Return the function of the coordinates representing the scalar field."""
        ...

    def expr(self, chart: Optional[Chart] = None, from_chart: Optional[Chart] = None):
        """Return the coordinate expression of the scalar field."""
        ...

    def set_expr(self, coord_expression, chart: Optional[Chart] = None) -> None:
        """Set the coordinate expression of the scalar field."""
        ...

    def add_expr(self, coord_expression, chart: Optional[Chart] = None) -> None:
        """Add a coordinate expression to the scalar field."""
        ...

    def add_expr_by_continuation(self, chart: Chart, subdomain: TopologicalManifold) -> None:
        """Complete the coordinate definition using analytic continuation."""
        ...

    def display(self, chart: Optional[Chart] = None):
        """Display the scalar field."""
        ...

    def restrict(self, subdomain: TopologicalManifold) -> ScalarField:
        """Return the restriction of the scalar field to a subdomain."""
        ...

    def common_charts(self, other: ScalarField):
        """Find common charts where both scalar fields are known."""
        ...
