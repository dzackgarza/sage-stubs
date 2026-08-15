from typing import TypeAlias

from sage.manifolds.differentiable.diff_form import DiffForm, DiffFormParal
from sage.manifolds.differentiable.scalarfield import DiffScalarField
from sage.manifolds.differentiable.tensorfield import TensorField
from sage.manifolds.differentiable.tensorfield_paral import TensorFieldParal
from sage.manifolds.chart import Chart
from sage.manifolds.differentiable.vectorfield_module import VectorFieldModule
from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.tensor.modules.alternating_contr_tensor import AlternatingContrTensor
from sage.tensor.modules.format_utilities import FormattedExpansion
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_tensor import FreeModuleTensor

_Degree: TypeAlias = int | Integer
_Scalar: TypeAlias = Element | Expression | Integer | int
_DisplayArgument: TypeAlias = Chart | Integer | int | str | list[str] | FreeModuleBasis | None
_WedgeOperand: TypeAlias = MultivectorField | MultivectorFieldParal | AlternatingContrTensor | DiffScalarField
_InteriorOperand: TypeAlias = DiffForm | DiffFormParal | FreeModuleAltForm
_InteriorResult: TypeAlias = DiffForm | DiffFormParal | FreeModuleAltForm | DiffScalarField | _Scalar
_BracketOperand: TypeAlias = MultivectorField | MultivectorFieldParal | DiffScalarField
_BracketResult: TypeAlias = MultivectorField | MultivectorFieldParal | DiffScalarField

class MultivectorField(TensorField):
    def __init__(
        self,
        vector_field_module: VectorFieldModule,
        degree: _Degree,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def degree(self) -> _Degree: ...
    def wedge(self, other: _WedgeOperand) -> AlternatingContrTensor: ...
    def interior_product(self, form: _InteriorOperand) -> _InteriorResult: ...
    def bracket(self, other: _BracketOperand) -> _BracketResult: ...

class MultivectorFieldParal(AlternatingContrTensor, TensorFieldParal, MultivectorField):
    def __init__(
        self,
        vector_field_module: VectorFieldModule,
        degree: _Degree,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def display(self, *args: _DisplayArgument, **kwds: _DisplayArgument | bool) -> FormattedExpansion: ...
    def disp(self, *args: _DisplayArgument, **kwds: _DisplayArgument | bool) -> FormattedExpansion: ...
    def __call__(self, *args: TensorField | FreeModuleTensor) -> TensorFieldParal | _Scalar: ...
    def wedge(self, other: _WedgeOperand) -> AlternatingContrTensor: ...
    def interior_product(self, form: _InteriorOperand) -> _InteriorResult: ...
    def bracket(self, other: _BracketOperand) -> _BracketResult: ...
