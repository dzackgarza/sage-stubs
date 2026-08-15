from typing import TYPE_CHECKING, Optional

from sage.rings.integer import Integer
from sage.modular.dirichlet import DirichletCharacter
from sage.graphs.graph import Graph
from sage.quatalg.quaternion_algebra import QuaternionAlgebra_ab
from sage.matrix.matrix import Matrix
class DoubleCosetReduction:
    

    parity: int
    label: int
    gamma: object
    x: object
    power: int

    def __init__(self, Y, x, extrapow: int = 0) -> None: ...

    def sign(self) -> int:
        
        ...

    def igamma(self, embedding=None, scale: int = 1) -> Matrix:
        
        ...

    def t(self, prec: Optional[int] = None) -> Matrix:
        
        ...

class BruhatTitsTree:
    

    def __init__(self, p) -> None: ...

class Vertex:
    

    def __init__(self, parent, vdata, label: int) -> None: ...

class Edge:
    

    def __init__(self, parent, edata, label: int) -> None: ...

class BruhatTitsQuotient:
    

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

    def get_vertex_list(self) -> list:
        
        ...

    def get_edge_list(self) -> list:
        
        ...

    def get_vertex_dict(self) -> dict:
        
        ...

    def get_num_verts(self) -> int:
        
        ...

    def get_num_ordered_edges(self) -> int:
        
        ...

    def fundom_rep(self, v1) -> Vertex:
        
        ...

    def get_quaternion_algebra(self) -> QuaternionAlgebra_ab:
        
        ...

    def get_maximal_order(self, magma=None, force_computation: bool = False) -> object:
        
        ...

    def get_eichler_order(self, magma=None, force_computation: bool = False) -> object:
        
        ...

    def get_stabilizers(self) -> list:
        
        ...

    def get_edge_stabilizers(self) -> list:
        
        ...

    def get_vertex_stabs(self) -> list:
        
        ...

    def plot(self) -> object:
        
        ...

    def plot_fundom(self) -> object:
        
        ...
