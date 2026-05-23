from sage.manifolds.scalarfield import ScalarField
from sage.manifolds.manifold import TopologicalManifold
from sage.structure.parent import Parent

class ScalarFieldAlgebra(Parent):
    element_class: type[ScalarField]
    _domain: TopologicalManifold
    def zero(self) -> ScalarField: ...
    def one(self) -> ScalarField: ...
