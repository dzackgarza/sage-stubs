from collections.abc import Mapping, Sequence
from typing import TypeAlias, overload

from sage.manifolds.chart import Chart
from sage.manifolds.chart_func import ChartFunction
from sage.manifolds.continuous_map import ContinuousMap
from sage.manifolds.differentiable.scalarfield import DiffScalarField
from sage.manifolds.differentiable.tensorfield import TensorField
from sage.manifolds.differentiable.tensorfield_paral import TensorFieldParal
from sage.manifolds.differentiable.vectorfield import VectorField
from sage.manifolds.point import ManifoldPoint
from sage.manifolds.subset import ManifoldSubset
from sage.manifolds.subsets.pullback import ManifoldSubsetPullback
from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.structure.parent import Parent
from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleMorphism

_CoordinateFunction: TypeAlias = Element | Expression | int | float | complex | str | ChartFunction
_CoordinateFunctions: TypeAlias = (
    _CoordinateFunction
    | Sequence[_CoordinateFunction]
    | Mapping[tuple[Chart, Chart], _CoordinateFunction | Sequence[_CoordinateFunction]]
)
_ChartFunctionRow: TypeAlias = Sequence[ChartFunction]
_JacobianFunctions: TypeAlias = Sequence[_ChartFunctionRow]
_MatrixEntry: TypeAlias = Element | Expression | Integer | int
_JacobianMatrix: TypeAlias = Sequence[Sequence[_MatrixEntry]]

class DiffMap(ContinuousMap):
    def __init__(
        self,
        parent: Parent,
        coord_functions: _CoordinateFunctions | None = None,
        name: str | None = None,
        latex_name: str | None = None,
        is_isomorphism: bool = False,
        is_identity: bool = False,
    ) -> None: ...
    def differential(self, point: ManifoldPoint) -> FiniteRankFreeModuleMorphism: ...
    def differential_functions(self, chart1: Chart | None = None, chart2: Chart | None = None) -> _JacobianFunctions: ...
    def jacobian_matrix(self, chart1: Chart | None = None, chart2: Chart | None = None) -> _JacobianMatrix: ...
    @overload
    def pullback(
        self,
        tensor_or_codomain_subset: ManifoldSubset,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> ManifoldSubset | ManifoldSubsetPullback: ...
    @overload
    def pullback(
        self,
        tensor_or_codomain_subset: DiffScalarField,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> DiffScalarField: ...
    @overload
    def pullback(
        self,
        tensor_or_codomain_subset: TensorField | TensorFieldParal,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> TensorField | TensorFieldParal: ...
    @overload
    def pushforward(self, tensor: VectorField | TensorFieldParal) -> TensorFieldParal: ...
    @overload
    def pushforward(self, tensor: Element) -> Element: ...
