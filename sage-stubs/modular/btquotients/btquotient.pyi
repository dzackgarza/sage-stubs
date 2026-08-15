from collections.abc import Callable

from sage.graphs.graph import Graph
from sage.interfaces.abc import MagmaElement
from sage.matrix.matrix import Matrix
from sage.modular.dirichlet import DirichletCharacter
from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.structure.parent import Parent
from sage.algebras.quatalg.quaternion_algebra import QuaternionAlgebra_ab


class DoubleCosetReduction:
    parity: int
    label: int
    gamma: Parent
    x: Matrix
    power: int

    def __init__(self, Y: BruhatTitsQuotient, x: Matrix, extrapow: int = 0) -> None: ...

    def sign(self) -> int:
        ...

    def igamma(self, embedding: int | Callable[[Parent], Matrix] | None = None, scale: int = 1) -> Matrix:
        ...

    def t(self, prec: int | None = None) -> Matrix:
        ...


class BruhatTitsTree:
    def __init__(self, p: int | Integer) -> None: ...


class Vertex:
    def __init__(self, p: int | Integer, label: int, rep: Matrix, leaving_edges: list[Edge] | None = None, entering_edges: list[Edge] | None = None, determinant: Integer | None = None, valuation: int | Integer | None = None) -> None: ...


class Edge:
    def __init__(self, p: int | Integer, label: int, rep: Matrix, origin: Vertex, target: Vertex, links: list[Parent] | None = None, opposite: Edge | None = None, determinant: Integer | None = None, valuation: int | Integer | None = None) -> None: ...


class BruhatTitsQuotient:
    def __init__(
        self,
        p: int | Integer,
        Nminus: int | Integer,
        Nplus: int = 1,
        character: DirichletCharacter | None = None,
        use_magma: bool = False,
        seed: int | None = None,
        magma_session: MagmaElement | None = None,
    ) -> None: ...

    def prime(self) -> Integer:
        ...

    def Nminus(self) -> Integer:
        ...

    def Nplus(self) -> Integer:
        ...

    def level(self) -> Integer:
        ...

    def genus(self) -> int:
        ...

    def get_graph(self) -> Graph:
        ...

    def get_vertex_list(self) -> list[Vertex]:
        ...

    def get_edge_list(self) -> list[Edge]:
        ...

    def get_vertex_dict(self) -> dict[Matrix, Vertex]:
        ...

    def get_num_verts(self) -> int:
        ...

    def get_num_ordered_edges(self) -> int:
        ...

    def fundom_rep(self, v1: Matrix) -> Vertex:
        ...

    def get_quaternion_algebra(self) -> QuaternionAlgebra_ab:
        ...

    def get_maximal_order(self, magma: bool = False, force_computation: bool = False) -> Parent | MagmaElement:
        ...

    def get_eichler_order(self, magma: bool = False, force_computation: bool = False) -> Parent | MagmaElement:
        ...

    def get_stabilizers(self) -> list[list[Parent]]:
        ...

    def get_edge_stabilizers(self) -> list[list[Parent]]:
        ...

    def get_vertex_stabs(self) -> list[list[Parent]]:
        ...

    def plot(self) -> Graphics:
        ...

    def plot_fundom(self) -> Graphics:
        ...
