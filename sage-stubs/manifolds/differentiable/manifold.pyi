from collections.abc import Iterable, Mapping, Sequence
from typing import Protocol

from sage.categories.category import Category
from sage.manifolds.chart import Chart
from sage.manifolds.differentiable.diff_form import DiffForm
from sage.manifolds.differentiable.metric import PseudoRiemannianMetric
from sage.manifolds.differentiable.vectorfield import VectorField
from sage.manifolds.differentiable.vectorfield_module import (
    VectorFieldFreeModule,
    VectorFieldModule,
    _DiffMapLike,
)
from sage.manifolds.differentiable.vectorframe import VectorFrame
from sage.manifolds.manifold import TopologicalManifold, _CoordDef, _ScalarExpression
from sage.manifolds.scalarfield import ScalarField
from sage.manifolds.structure import DifferentialStructure, TopologicalStructure
from sage.manifolds.vector_bundle import TopologicalVectorBundle
from sage.rings.ring import Field
from sage.structure.element import Element, Expression

type _Name = str | None
type _DiffDegree = int
type _CoordinateExpressions = _ScalarExpression | Sequence[_ScalarExpression]
type _CoordFunctionSpec = (
    Mapping[tuple[Chart, Chart], _CoordinateExpressions] | _CoordinateExpressions
)
type _TensorType = tuple[int, int]
type _FrameChangeKey = tuple[Element, Element]
type _Signature = int | tuple[int, int] | tuple[int, int, int]

class _TensorBundle(Protocol): ...
class _TensorFieldModule(Protocol): ...
class _DiffFormModule(Protocol): ...
class _MixedFormAlgebra(Protocol): ...
class _MultivectorModule(Protocol): ...
class _AutomorphismFieldGroup(Protocol): ...
class _TensorField(Protocol): ...
class _SymBilinFormField(Protocol): ...
class _MultivectorField(Protocol): ...
class _DiffForm(Protocol): ...
class _MixedForm(Protocol): ...
class _SymplecticForm(Protocol): ...
class _PoissonTensorField(Protocol): ...
class _AutomorphismField(Protocol): ...
class _VectorFrame(Protocol): ...
class _CoFrame(Protocol): ...
class _TangentSpace(Protocol): ...
class _Curve(Protocol): ...
class _IntegratedCurve(Protocol): ...
class _AffineConnection(Protocol): ...
class _Metric(Protocol): ...
class _DegenerateMetric(Protocol): ...
class _TangentVector(Protocol): ...

class DifferentiableManifold(TopologicalManifold):
    def __init__(
        self,
        n: int,
        name: str,
        field: str | Field,
        structure: DifferentialStructure | TopologicalStructure,
        base_manifold: DifferentiableManifold | TopologicalManifold | None = ...,
        diff_degree: _DiffDegree | str | None = ...,
        latex_name: _Name | int = ...,
        start_index: int | Category | None = ...,
        category: Category | str | None = ...,
        unique_tag: str | None = ...,
    ) -> None: ...
    def diff_degree(self) -> _DiffDegree: ...
    def open_subset(
        self,
        name: str,
        latex_name: _Name | str | None = ...,
        coord_def: _CoordDef = ...,
        supersets: Sequence[TopologicalManifold] | None = ...,
    ) -> DifferentiableManifold: ...
    def diff_map(
        self,
        codomain: DifferentiableManifold,
        coord_functions: _CoordFunctionSpec | None = ...,
        chart1: Chart | None = ...,
        chart2: Chart | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _DiffMapLike: ...
    def diffeomorphism(
        self,
        codomain: DifferentiableManifold | None = ...,
        coord_functions: _CoordFunctionSpec | None = ...,
        chart1: Chart | None = ...,
        chart2: Chart | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _DiffMapLike: ...
    def vector_bundle(
        self,
        rank: int,
        name: str,
        field: str = ...,
        latex_name: _Name | str | None = ...,
    ) -> TopologicalVectorBundle: ...
    def tangent_bundle(self, dest_map: _DiffMapLike | None = ...) -> _TensorBundle: ...
    def cotangent_bundle(
        self, dest_map: _DiffMapLike | None = ...
    ) -> _TensorBundle: ...
    def tensor_bundle(
        self, k: int, l: int, dest_map: _DiffMapLike | None = ...
    ) -> _TensorBundle: ...
    def vector_field_module(
        self, dest_map: _DiffMapLike | None = ..., force_free: bool = ...
    ) -> VectorFieldModule | VectorFieldFreeModule: ...
    def tensor_field_module(
        self, tensor_type: _TensorType, dest_map: _DiffMapLike | None = ...
    ) -> _TensorFieldModule: ...
    def diff_form_module(
        self, degree: int, dest_map: _DiffMapLike | None = ...
    ) -> _DiffFormModule: ...
    def mixed_form_algebra(
        self, dest_map: _DiffMapLike | None = ...
    ) -> _MixedFormAlgebra: ...
    de_rham_complex = mixed_form_algebra

    def multivector_module(
        self, degree: int, dest_map: _DiffMapLike | None = ...
    ) -> _MultivectorModule: ...
    def automorphism_field_group(
        self, dest_map: _DiffMapLike | None = ...
    ) -> _AutomorphismFieldGroup: ...
    def vector_field(
        self,
        *comp: _ScalarExpression,
        dest_map: _DiffMapLike | None = ...,
        frame: Element | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> VectorField: ...
    def tensor_field(
        self,
        k: int,
        l: int,
        *comp: _ScalarExpression,
        dest_map: _DiffMapLike | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
        sym: Iterable[int] | Iterable[Iterable[int]] | None = ...,
        antisym: Iterable[int] | Iterable[Iterable[int]] | None = ...,
        specific_type: type[_TensorField] | None = ...,
    ) -> _TensorField: ...
    def sym_bilin_form_field(
        self,
        name: _Name = ...,
        latex_name: _Name = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> _SymBilinFormField: ...
    def multivector_field(
        self,
        degree: int,
        *comp: _ScalarExpression,
        dest_map: _DiffMapLike | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> ScalarField | VectorField | _MultivectorField: ...
    def diff_form(
        self,
        degree: int,
        *comp: _ScalarExpression,
        dest_map: _DiffMapLike | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> DiffForm: ...
    def one_form(
        self,
        *comp: _ScalarExpression,
        dest_map: _DiffMapLike | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> DiffForm: ...
    def mixed_form(
        self,
        name: _Name = ...,
        latex_name: _Name = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> _MixedForm: ...
    def symplectic_form(
        self, name: _Name = ..., latex_name: _Name = ...
    ) -> _SymplecticForm: ...
    def poisson_tensor(
        self, name: _Name = ..., latex_name: _Name = ...
    ) -> _PoissonTensorField: ...
    def automorphism_field(
        self,
        name: _Name = ...,
        latex_name: _Name = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> _AutomorphismField: ...
    def tangent_identity_field(
        self, dest_map: _DiffMapLike | None = ...
    ) -> _AutomorphismField: ...
    def set_orientation(
        self,
        orientation: _VectorFrame | Sequence[_VectorFrame] | Chart | Sequence[Chart],
    ) -> None: ...
    def orientation(self) -> list[Chart]: ...
    def default_frame(self) -> _VectorFrame: ...
    def set_default_frame(self, frame: _VectorFrame) -> None: ...
    def change_of_frame(
        self, frame1: _VectorFrame, frame2: _VectorFrame
    ) -> _AutomorphismField: ...
    def set_change_of_frame(
        self,
        frame1: _VectorFrame,
        frame2: _VectorFrame,
        change_of_frame: _AutomorphismField,
        compute_inverse: bool = ...,
    ) -> None: ...
    def vector_frame(
        self,
        symbol: str | Sequence[str],
        latex_symbol: str | Sequence[str] | None = ...,
        from_frame: _VectorFrame | None = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> VectorFrame: ...
    def frames(self) -> list[_VectorFrame]: ...
    def coframes(self) -> list[_CoFrame]: ...
    def changes_of_frame(self) -> dict[_FrameChangeKey, _AutomorphismField]: ...
    def is_manifestly_parallelizable(self) -> bool: ...
    def tangent_space(self, point: Element) -> _TangentSpace: ...
    def curve(
        self,
        coord_expression: _CoordinateExpressions,
        param: tuple[Expression, _ScalarExpression, _ScalarExpression],
        chart: Chart | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _Curve: ...
    def integrated_curve(
        self,
        equations_rhs: Sequence[_ScalarExpression],
        velocities: Sequence[_ScalarExpression],
        curve_param: Expression,
        initial_tangent_vector: _TangentVector,
        chart: Chart | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _IntegratedCurve: ...
    def integrated_autoparallel_curve(
        self,
        affine_connection: _AffineConnection,
        curve_param: Expression,
        initial_tangent_vector: _TangentVector,
        chart: Chart | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _IntegratedCurve: ...
    def integrated_geodesic(
        self,
        metric: _Metric,
        curve_param: Expression,
        initial_tangent_vector: _TangentVector,
        chart: Chart | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _IntegratedCurve: ...
    def affine_connection(
        self, name: str, latex_name: _Name = ...
    ) -> _AffineConnection: ...
    def metric(
        self,
        name: str,
        signature: _Signature | None = ...,
        latex_name: _Name = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> PseudoRiemannianMetric: ...
    def degenerate_metric(
        self,
        name: str,
        signature: _Signature | None = ...,
        latex_name: _Name = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> _DegenerateMetric: ...
    def riemannian_metric(
        self, name: str, latex_name: _Name = ..., dest_map: _DiffMapLike | None = ...
    ) -> _Metric: ...
    def lorentzian_metric(
        self,
        name: str,
        signature: str = ...,
        latex_name: _Name = ...,
        dest_map: _DiffMapLike | None = ...,
    ) -> _Metric: ...
    def tangent_vector(
        self,
        comp: Sequence[_ScalarExpression],
        point: Element,
        basis: Element | None = ...,
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> _TangentVector: ...
    vector = tangent_vector
