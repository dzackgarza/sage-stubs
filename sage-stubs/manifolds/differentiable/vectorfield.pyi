from collections.abc import Mapping, Sequence
from typing import Protocol, TypeAlias

from sage.manifolds.chart import Chart
from sage.manifolds.scalarfield import ScalarField
from sage.structure.element import Element, Expression

_Name: TypeAlias = str | None
_Scalar: TypeAlias = Element | Expression | int | float | complex | str
_PlotRanges: TypeAlias = Mapping[Expression, tuple[_Scalar, _Scalar]]
_FixedCoords: TypeAlias = Mapping[Expression, _Scalar]
_SampleCounts: TypeAlias = int | Mapping[Expression, int]
_Steps: TypeAlias = Mapping[Expression, _Scalar]

class _Metric(Protocol): ...
class _Graphics(Protocol): ...
class _OneForm(Protocol): ...
class _VectorFieldModuleLike(Protocol): ...

class VectorField(Element):
    def __init__(self, vector_field_module: _VectorFieldModuleLike, name: _Name = ..., latex_name: _Name = ...) -> None: ...
    def __call__(self, scalar: ScalarField | _OneForm) -> ScalarField | Element: ...
    def plot(
        self,
        chart: Chart | None = ...,
        ambient_coords: Sequence[Expression] | None = ...,
        mapping: Element | None = ...,
        chart_domain: Chart | None = ...,
        fixed_coords: _FixedCoords | None = ...,
        ranges: _PlotRanges | None = ...,
        number_values: _SampleCounts | None = ...,
        steps: _Steps | None = ...,
        parameters: Mapping[Expression, _Scalar] | None = ...,
        label_axes: bool = ...,
        **extra_options: str | float | bool,
    ) -> _Graphics: ...
    def bracket(self, other: VectorField) -> VectorField: ...
    def curl(self, metric: _Metric | None = ...) -> VectorField: ...
    def dot_product(self, other: VectorField, metric: _Metric | None = ...) -> ScalarField: ...
    dot = dot_product
    def norm(self, metric: _Metric | None = ...) -> ScalarField: ...
    def cross_product(self, other: VectorField, metric: _Metric | None = ...) -> VectorField: ...
    cross = cross_product

class VectorFieldParal(VectorField): ...
