from sage.manifolds.manifold import TopologicalManifold
from sage.structure.sage_object import SageObject

class TopologicalVectorBundle(SageObject):
    def __init__(
        self,
        rank: int,
        name: str,
        base_space: TopologicalManifold,
        field: str = "real",
        latex_name: str | None = None,
    ) -> None: ...
