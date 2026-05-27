from typing import TypeAlias

from sage.manifolds.differentiable.manifold import DifferentiableManifold
from sage.manifolds.differentiable.multivectorfield import MultivectorField, MultivectorFieldParal
from sage.manifolds.differentiable.scalarfield import DiffScalarField
from sage.manifolds.differentiable.vectorfield import VectorField
from sage.manifolds.differentiable.vectorfield_module import VectorFieldModule

from sage.manifolds.differentiable.diff_form import DiffForm

_PoissonDomain: TypeAlias = DifferentiableManifold | VectorFieldModule

class PoissonTensorField(MultivectorField):
    def __init__(
        self,
        manifold: _PoissonDomain,
        name: str | None = "varpi",
        latex_name: str | None = "\\varpi",
    ) -> None: ...
    def hamiltonian_vector_field(self, function: DiffScalarField) -> VectorField: ...
    def sharp(self, form: DiffForm) -> VectorField: ...
    def poisson_bracket(self, f: DiffScalarField, g: DiffScalarField) -> DiffScalarField: ...

class PoissonTensorFieldParal(PoissonTensorField, MultivectorFieldParal):
    def __init__(
        self,
        manifold: _PoissonDomain,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
