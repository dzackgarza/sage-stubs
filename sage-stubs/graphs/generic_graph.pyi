from collections.abc import Callable, Hashable, Iterable
from typing import Literal, Self, overload

from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.rings.integer import Integer
from sage.structure.element import Element


type GraphVertex = Hashable | Element
type GraphLabel = Hashable | Element | None
type GraphEdge = tuple[GraphVertex, GraphVertex] | tuple[GraphVertex, GraphVertex, GraphLabel]


class GenericGraph:
    def order(self) -> int: ...
    def size(self) -> int: ...
    def vertices(
        self,
        sort: bool = False,
        key: Callable[[GraphVertex], GraphLabel] | None = None,
        degree: int | Integer | None = None,
        vertex_property: Callable[[GraphVertex], bool] | None = None,
    ) -> list[GraphVertex]: ...
    def edges(
        self,
        vertices: Iterable[GraphVertex] | GraphVertex | None = None,
        labels: bool = True,
        sort: bool = False,
        key: Callable[[GraphEdge], GraphLabel] | None = None,
        ignore_direction: bool = False,
        sort_vertices: bool = True,
    ) -> list[GraphEdge]: ...
    def add_vertex(self, name: GraphVertex | None = None) -> GraphVertex | None: ...
    def add_vertices(self, vertices: Iterable[GraphVertex | None]) -> list[int] | None: ...
    def add_edge(
        self,
        u: GraphVertex | tuple[GraphVertex, GraphVertex] | tuple[GraphVertex, GraphVertex, GraphLabel] | None,
        v: GraphVertex | None = None,
        label: GraphLabel = None,
    ) -> None: ...
    def degree(
        self,
        vertices: Iterable[GraphVertex] | GraphVertex | None = None,
        labels: bool = False,
    ) -> int | list[int] | dict[GraphVertex, int]: ...
    def is_connected(self) -> bool: ...
    def connected_components(
        self,
        sort: bool = False,
        key: Callable[[GraphVertex], GraphLabel] | None = None,
        forbidden_vertices: Iterable[GraphVertex] | None = None,
    ) -> list[list[GraphVertex]]: ...
    def shortest_path(
        self,
        u: GraphVertex,
        v: GraphVertex,
        by_weight: bool = False,
        algorithm: str | None = None,
        weight_function: Callable[[tuple[GraphVertex, GraphVertex, GraphLabel]], Element | int | float] | None = None,
        check_weight: bool = True,
    ) -> list[GraphVertex]: ...
    def distance(
        self,
        u: GraphVertex,
        v: GraphVertex,
        by_weight: bool = False,
        weight_function: Callable[[tuple[GraphVertex, GraphVertex, GraphLabel]], Element | int | float] | None = None,
        check_weight: bool = True,
    ) -> Element | int | float: ...
    def complement(self, immutable: bool | None = None) -> Self: ...
    @overload
    def subgraph(
        self,
        vertices: Iterable[GraphVertex] | None = None,
        edges: Iterable[GraphEdge] | GraphEdge | None = None,
        inplace: Literal[False] = False,
        vertex_property: Callable[[GraphVertex], bool] | None = None,
        edge_property: Callable[[GraphEdge], bool] | None = None,
        algorithm: str | None = None,
        immutable: bool | None = None,
    ) -> Self: ...
    @overload
    def subgraph(
        self,
        vertices: Iterable[GraphVertex] | None = None,
        edges: Iterable[GraphEdge] | GraphEdge | None = None,
        inplace: Literal[True] = True,
        vertex_property: Callable[[GraphVertex], bool] | None = None,
        edge_property: Callable[[GraphEdge], bool] | None = None,
        algorithm: str | None = None,
        immutable: bool | None = None,
    ) -> None: ...
    @overload
    def automorphism_group(
        self,
        partition: Iterable[Iterable[GraphVertex]] | None = None,
        verbosity: int = 0,
        edge_labels: bool = False,
        order: Literal[False] = False,
        return_group: Literal[True] = True,
        orbits: Literal[False] = False,
        algorithm: str | None = None,
    ) -> PermutationGroup_generic: ...
    @overload
    def automorphism_group(
        self,
        partition: Iterable[Iterable[GraphVertex]] | None = None,
        verbosity: int = 0,
        edge_labels: bool = False,
        order: Literal[True] = True,
        return_group: Literal[False] = False,
        orbits: Literal[False] = False,
        algorithm: str | None = None,
    ) -> Integer: ...
    @overload
    def automorphism_group(
        self,
        partition: Iterable[Iterable[GraphVertex]] | None = None,
        verbosity: int = 0,
        edge_labels: bool = False,
        order: Literal[False] = False,
        return_group: Literal[False] = False,
        orbits: Literal[True] = True,
        algorithm: str | None = None,
    ) -> list[list[GraphVertex]]: ...
    @overload
    def automorphism_group(
        self,
        partition: Iterable[Iterable[GraphVertex]] | None = None,
        verbosity: int = 0,
        edge_labels: bool = False,
        order: bool = False,
        return_group: bool = True,
        orbits: bool = False,
        algorithm: str | None = None,
    ) -> PermutationGroup_generic | Integer | list[list[GraphVertex]] | tuple[PermutationGroup_generic | Integer | list[list[GraphVertex]], ...] | None: ...
