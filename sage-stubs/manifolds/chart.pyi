from typing import TYPE_CHECKING, Optional, overload

if TYPE_CHECKING:
    from sage.manifolds.manifold import TopologicalManifold

class Chart:
    """Chart on a topological manifold."""
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _sindex: int
    _xx: tuple
    _periods: Optional[tuple]
    _restrictions: frozenset

    @staticmethod
    def __classcall__(
        cls,
        domain: TopologicalManifold,
        coordinates: str = "",
        calc_method: Optional[str] = None,
        names=None,
        coord_restrictions=None,
        **coordinate_options,
    ) -> Chart: ...

    def __init__(
        self,
        domain: TopologicalManifold,
        coordinates,
        calc_method: Optional[str] = None,
        periods: Optional[tuple] = None,
        coord_restrictions=None,
    ) -> None: ...

    @classmethod
    def _parse_coordinates(cls, domain: TopologicalManifold, coordinates):
        """Initialization of the coordinates as symbolic variables."""
        ...

    @staticmethod
    def _normalize_coord_restrictions(coordinates, coord_restrictions) -> frozenset: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _first_ngens(self, n: int): ...
    def __getitem__(self, i):
        """Access to the coordinates."""
        ...

    def __call__(self, point):
        """Return the coordinates of a given point."""
        ...

    def domain(self) -> TopologicalManifold:
        """Return the open subset on which the chart is defined."""
        ...

    def manifold(self) -> TopologicalManifold:
        """Return the manifold on which the chart is defined."""
        ...

    def periods(self) -> Optional[tuple]:
        """Return the coordinate periods."""
        ...

    def add_restrictions(self, restrictions) -> None: ...

    def restrict(self, subset: TopologicalManifold, restrictions=None) -> Chart:
        """Return the restriction of self to some open subset of its domain."""
        ...

    def valid_coordinates(self, *coordinates, **kwds) -> bool:
        """Check whether a tuple of coordinates can be the coordinates of a point."""
        ...

    def _check_restrictions(self, restrict, substitutions) -> bool:
        """Recursive helper function to check the validity of coordinates."""
        ...

    def codomain(self):
        """Return the codomain of self as a set."""
        ...

    def _restrict_set(self, universe, coord_restrictions):
        """Return a set corresponding to coordinate restrictions."""
        ...

    def transition_map(
        self,
        other: Chart,
        transformations,
        intersection_name: Optional[str] = None,
        restrictions1=None,
        restrictions2=None,
    ):
        """Construct the transition map between the current chart and another one."""
        ...

    def preimage(self, codomain_subset, name: Optional[str] = None, latex_name: Optional[str] = None):
        """Return the preimage (pullback) of codomain_subset under self."""
        ...

    def pullback(self, codomain_subset, name: Optional[str] = None, latex_name: Optional[str] = None):
        """Alias for preimage."""
        ...

    def function_ring(self):
        """Return the ring of coordinate functions on self."""
        ...

    def function(self, expression, calc_method: Optional[str] = None, expansion_symbol=None, order: Optional[int] = None):
        """Define a coordinate function to the base field."""
        ...

    def zero_function(self):
        """Return the zero function of the coordinates."""
        ...

    def one_function(self):
        """Return the constant function of the coordinates equal to one."""
        ...

    def calculus_method(self):
        """Return the interface governing the calculus engine for expressions."""
        ...

    def multifunction(self, *expressions):
        """Define a coordinate function to some Cartesian power of the base field."""
        ...


class RealChart(Chart):
    """Chart on a topological manifold over RR."""
    ...
