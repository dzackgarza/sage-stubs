from collections.abc import Mapping
from typing import TypeAlias

from sage.manifolds.chart import Chart
from sage.manifolds.chart_func import ChartFunction
from sage.manifolds.differentiable.diff_form import DiffForm
from sage.manifolds.differentiable.metric import PseudoRiemannianMetric
from sage.manifolds.differentiable.multivectorfield import MultivectorField
from sage.manifolds.differentiable.symplectic_form import SymplecticForm
from sage.manifolds.differentiable.vectorfield import VectorField
from sage.manifolds.scalarfield import ScalarField
from sage.manifolds.scalarfield_algebra import ScalarFieldAlgebra
from sage.structure.element import Element, Expression

_ScalarExpression: TypeAlias = Element | Expression | int | float | complex | str
_ChartExpression: TypeAlias = _ScalarExpression | ChartFunction
_CoordinateExpression: TypeAlias = _ChartExpression | Mapping[Chart, _ChartExpression]
_ChartSelector: TypeAlias = Chart | str | None
_BilinearForm: TypeAlias = PseudoRiemannianMetric | SymplecticForm
_ExteriorOperand: TypeAlias = DiffForm | MultivectorField

class DiffScalarField(ScalarField):
    def __init__(
        self,
        parent: ScalarFieldAlgebra,
        coord_expression: _CoordinateExpression | None = None,
        chart: _ChartSelector = None,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def tensor_type(self) -> tuple[int, int]: ...
    def differential(self) -> DiffForm: ...
    exterior_derivative = differential
    derivative = differential
    def lie_derivative(self, vector: VectorField) -> DiffScalarField: ...
    lie_der = lie_derivative
    def hodge_dual(self, nondegenerate_tensor: _BilinearForm) -> DiffForm: ...
    def bracket(self, other: DiffScalarField | MultivectorField) -> DiffScalarField | MultivectorField: ...
    def wedge(self, other: _ExteriorOperand) -> _ExteriorOperand: ...
    def degree(self) -> int: ...
    def gradient(self, metric: PseudoRiemannianMetric | None = None) -> VectorField: ...
    def laplacian(self, metric: PseudoRiemannianMetric | None = None) -> DiffScalarField: ...
    def dalembertian(self, metric: PseudoRiemannianMetric | None = None) -> DiffScalarField: ...
