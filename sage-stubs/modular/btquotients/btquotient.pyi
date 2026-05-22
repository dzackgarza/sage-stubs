from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from sage.rings.integer import Integer
    from sage.modular.dirichlet import DirichletCharacter
    from sage.graphs.graph import Graph
    from sage.quatalg.quaternion_algebra import QuaternionAlgebra_ab
    from sage.matrix.matrix import Matrix

class DoubleCosetReduction:
    """Edges in the Bruhat-Tits tree represented by cosets of matrices in GL_2."""

    parity: int
    label: int
    gamma: object
    x: object
    power: int

    def __init__(self, Y, x, extrapow: int = 0) -> None: ...

    def sign(self) -> int:
        """Return the sign: +1 or -1."""
        ...

    def igamma(self, embedding=None, scale: int = 1) -> Matrix:
        """Return the inverse gamma as a p-adic matrix."""
        ...

    def t(self, prec: Optional[int] = None) -> Matrix:
        """Return t as a p-adic matrix."""
        ...

class BruhatTitsTree:
    """The Bruhat-Tits tree of GL_2(QQ_p)."""

    def __init__(self, p) -> None: ...

class Vertex:
    """A vertex in the Bruhat-Tits tree."""

    def __init__(self, parent, vdata, label: int) -> None: ...

class Edge:
    """An edge in the Bruhat-Tits tree."""

    def __init__(self, parent, edata, label: int) -> None: ...

class BruhatTitsQuotient:
    """Quotient of the Bruhat-Tits tree by an arithmetic quaternionic group."""

    def __init__(
        self,
        p,
        Nminus,
        Nplus: int = 1,
        character: Optional[DirichletCharacter] = None,
        use_magma: bool = False,
        seed: Optional[int] = None,
        magma_session = None,
    ) -> None: ...

    def prime(self) -> Integer:
        """Return the prime p."""
        ...

    def Nminus(self) -> Integer:
        """Return Nminus, the discriminant of the quaternion algebra."""
        ...

    def Nplus(self) -> Integer:
        """Return Nplus, the tame level."""
        ...

    def level(self) -> Integer:
        """Return the level."""
        ...

    def genus(self) -> int:
        """Return the genus."""
        ...

    def get_graph(self) -> Graph:
        """Return the quotient graph."""
        ...

    def get_vertex_list(self) -> list:
        """Return the list of vertices."""
        ...

    def get_edge_list(self) -> list:
        """Return the list of edges."""
        ...

    def get_vertex_dict(self) -> dict:
        """Return the dictionary of vertices."""
        ...

    def get_num_verts(self) -> int:
        """Return the number of vertices."""
        ...

    def get_num_ordered_edges(self) -> int:
        """Return the number of ordered edges."""
        ...

    def fundom_rep(self, v1) -> Vertex:
        """Return the fundamental domain representative of v1."""
        ...

    def get_quaternion_algebra(self) -> QuaternionAlgebra_ab:
        """Return the quaternion algebra."""
        ...

    def get_maximal_order(self, magma=None, force_computation: bool = False) -> object:
        """Return a maximal order of the quaternion algebra."""
        ...

    def get_eichler_order(self, magma=None, force_computation: bool = False) -> object:
        """Return an Eichler order."""
        ...

    def get_stabilizers(self) -> list:
        """Return the stabilizers of vertices and edges."""
        ...

    def get_edge_stabilizers(self) -> list:
        """Return the stabilizers of edges."""
        ...

    def get_vertex_stabs(self) -> list:
        """Return the stabilizers of vertices."""
        ...

    def plot(self) -> object:
        """Plot the graph."""
        ...

    def plot_fundom(self) -> object:
        """Plot the fundamental domain."""
        ...
