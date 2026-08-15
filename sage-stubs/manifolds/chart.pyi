from typing import TYPE_CHECKING, Optional, overload, Any
from collections.abc import Callable

from sage.manifolds.manifold import TopologicalManifold
from sage.structure.element import Element

class Chart:
    
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _sindex: int
    _xx: tuple[str, ...]
    _periods: tuple[Any, ...] | None
    _restrictions: frozenset[Any]

    @staticmethod
    def __classcall__(
        cls: type[Chart],
        domain: TopologicalManifold,
        coordinates: str = "",
        calc_method: str | None = None,
        names: Any = None,
        coord_restrictions: Any = None,
        **coordinate_options: Any,
    ) -> Chart: ...

    def __init__(
        self,
        domain: TopologicalManifold,
        coordinates: str,
        calc_method: str | None = None,
        periods: tuple[Any, ...] | None = None,
        coord_restrictions: Any = None,
    ) -> None: ...

    @classmethod
    def _parse_coordinates(cls: type[Chart], domain: TopologicalManifold, coordinates: str) -> tuple[str, ...]:
        
        ...

    @staticmethod
    def _normalize_coord_restrictions(coordinates: Any, coord_restrictions: Any) -> frozenset[Any]: ...

    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def _first_ngens(self, n: int) -> tuple[str, ...]: ...
    def __getitem__(self, i: int) -> str:
        
        ...

    def __call__(self, point: Any) -> tuple[Any, ...]:
        
        ...

    def domain(self) -> TopologicalManifold:
        
        ...

    def manifold(self) -> TopologicalManifold:
        
        ...

    def periods(self) -> tuple[Any, ...] | None:
        
        ...

    def add_restrictions(self, restrictions: Any) -> None: ...

    def restrict(self, subset: TopologicalManifold, restrictions: Any = None) -> Chart:
        
        ...

    def valid_coordinates(self, *coordinates: Any, **kwds: Any) -> bool:
        
        ...

    def _check_restrictions(self, restrict: Any, substitutions: Any) -> bool:
        
        ...

    def codomain(self) -> Any:
        
        ...

    def _restrict_set(self, universe: Any, coord_restrictions: Any) -> Any:
        
        ...

    def transition_map(
        self,
        other: Chart,
        transformations: Any,
        intersection_name: str | None = None,
        restrictions1: Any = None,
        restrictions2: Any = None,
    ) -> Any:
        
        ...

    def preimage(self, codomain_subset: Any, name: str | None = None, latex_name: str | None = None) -> Any:
        
        ...

    def pullback(self, codomain_subset: Any, name: str | None = None, latex_name: str | None = None) -> Any:
        
        ...

    def function_ring(self) -> Any:
        
        ...

    def function(self, expression: Any, calc_method: str | None = None, expansion_symbol: Any = None, order: int | None = None) -> Any:
        
        ...

    def zero_function(self) -> Any:
        
        ...

    def one_function(self) -> Any:
        
        ...

    def calculus_method(self) -> str:
        
        ...

    def multifunction(self, *expressions: Any) -> Any:
        
        ...


class RealChart(Chart):
    ...
