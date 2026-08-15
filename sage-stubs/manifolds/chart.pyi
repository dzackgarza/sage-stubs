from typing import TYPE_CHECKING, Optional, overload, Any, Callable

from sage.manifolds.manifold import TopologicalManifold
from sage.structure.element import Element

class Chart:
    
    _domain: TopologicalManifold
    _manifold: TopologicalManifold
    _sindex: int
    _xx: tuple[str, ...]
    _periods: Optional[tuple[Any, ...]]
    _restrictions: frozenset[Any]

    @staticmethod
    def __classcall__(
        cls: type[Chart],
        domain: TopologicalManifold,
        coordinates: str = "",
        calc_method: Optional[str] = None,
        names: Any = None,
        coord_restrictions: Any = None,
        **coordinate_options: Any,
    ) -> Chart: ...

    def __init__(
        self,
        domain: TopologicalManifold,
        coordinates: str,
        calc_method: Optional[str] = None,
        periods: Optional[tuple[Any, ...]] = None,
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

    def periods(self) -> Optional[tuple[Any, ...]]:
        
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
        intersection_name: Optional[str] = None,
        restrictions1: Any = None,
        restrictions2: Any = None,
    ) -> Any:
        
        ...

    def preimage(self, codomain_subset: Any, name: Optional[str] = None, latex_name: Optional[str] = None) -> Any:
        
        ...

    def pullback(self, codomain_subset: Any, name: Optional[str] = None, latex_name: Optional[str] = None) -> Any:
        
        ...

    def function_ring(self) -> Any:
        
        ...

    def function(self, expression: Any, calc_method: Optional[str] = None, expansion_symbol: Any = None, order: Optional[int] = None) -> Any:
        
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
