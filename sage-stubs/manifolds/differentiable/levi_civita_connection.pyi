from sage.manifolds.chart import Chart
from sage.manifolds.differentiable.affine_connection import AffineConnection, _ComponentSet
from sage.manifolds.differentiable.manifold import DifferentiableManifold
from sage.manifolds.differentiable.metric import PseudoRiemannianMetric
from sage.manifolds.differentiable.tensorfield import TensorField
from sage.tensor.modules.free_module_basis import FreeModuleBasis

class LeviCivitaConnection(AffineConnection):
    def __init__(
        self,
        metric: PseudoRiemannianMetric,
        name: str | None = None,
        latex_name: str | None = None,
        init_coef: bool = True,
    ) -> None: ...
    def restrict(self, subdomain: DifferentiableManifold) -> LeviCivitaConnection: ...
    def coef(self, frame: FreeModuleBasis | None = None) -> _ComponentSet: ...
    def torsion(self) -> TensorField: ...
    def riemann(self, name: str | None = None, latex_name: str | None = None) -> TensorField: ...
    def ricci(self, name: str | None = None, latex_name: str | None = None) -> TensorField: ...
