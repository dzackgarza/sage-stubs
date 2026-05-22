from sage.manifolds.scalarfield import ScalarField
from sage.structure.parent import Parent

class ScalarFieldAlgebra(Parent):
    element_class: type[ScalarField]
    def zero(self) -> ScalarField: ...
    def one(self) -> ScalarField: ...
