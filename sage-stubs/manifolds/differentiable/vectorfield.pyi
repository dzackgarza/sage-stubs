from collections.abc import Mapping, Sequence
from typing import Protocol, Self

from sage.manifolds.chart import Chart
from sage.manifolds.scalarfield import ScalarField
from sage.structure.element import Element, Expression
from sage.structure.parent import Parent

type _Name = str | None
type _Scalar = Element | Expression | int | float | complex | str
type _PlotRanges = Mapping[Expression, tuple[_Scalar, _Scalar]]
type _FixedCoords = Mapping[Expression, _Scalar]
type _SampleCounts = int | Mapping[Expression, int]
type _Steps = Mapping[Expression, _Scalar]

class _Metric(Protocol): ...
class _Graphics(Protocol): ...
class _OneForm(Protocol): ...
class _VectorFieldModuleLike(Protocol): ...

class VectorField(Element):
    def __init__(
        self,
        vector_field_module: _VectorFieldModuleLike | Parent[Self],
        name: _Name = ...,
        latex_name: _Name = ...,
    ) -> None: ...
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
    def dot_product(
        self, other: VectorField, metric: _Metric | None = ...
    ) -> ScalarField: ...
    dot = dot_product

    def norm(self, metric: _Metric | None = ...) -> ScalarField: ...
    def cross_product(
        self, other: VectorField, metric: _Metric | None = ...
    ) -> VectorField: ...
    cross = cross_product

class VectorFieldParal(VectorField): ...
