from typing import TypeAlias, overload

from sage.manifolds.chart import Chart
from sage.manifolds.differentiable.metric import PseudoRiemannianMetric
from sage.manifolds.differentiable.multivectorfield import MultivectorField, MultivectorFieldParal
from sage.manifolds.differentiable.scalarfield import DiffScalarField
from sage.manifolds.differentiable.symplectic_form import SymplecticForm
from sage.manifolds.differentiable.tensorfield import TensorField
from sage.manifolds.differentiable.tensorfield_paral import TensorFieldParal
from sage.manifolds.differentiable.vectorfield import VectorField
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
_BilinearForm: TypeAlias = PseudoRiemannianMetric | SymplecticForm
_InteriorResult: TypeAlias = DiffScalarField | MultivectorField | MultivectorFieldParal

class DiffForm(TensorField):
    def __init__(
        self,
        vector_field_module: VectorFieldModule,
        degree: _Degree,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def exterior_derivative(self) -> DiffForm: ...
    derivative = exterior_derivative
    def wedge(self, other: DiffForm | DiffScalarField) -> DiffForm: ...
    def degree(self) -> _Degree: ...
    def hodge_dual(
        self,
        nondegenerate_tensor: _BilinearForm | None = None,
        minus_eigenvalues_convention: bool = False,
    ) -> DiffForm: ...
    def interior_product(self, qvect: MultivectorField | MultivectorFieldParal) -> _InteriorResult: ...

class DiffFormParal(FreeModuleAltForm, TensorFieldParal, DiffForm):
    def __init__(
        self,
        vector_field_module: VectorFieldModule,
        degree: _Degree,
        name: str | None = None,
        latex_name: str | None = None,
    ) -> None: ...
    def display(self, *args: _DisplayArgument, **kwds: _DisplayArgument | bool) -> FormattedExpansion: ...
    def disp(self, *args: _DisplayArgument, **kwds: _DisplayArgument | bool) -> FormattedExpansion: ...
    @overload
    def __call__(self, *args: VectorField) -> DiffScalarField: ...
    @overload
    def __call__(self, *args: TensorField | FreeModuleTensor) -> TensorFieldParal | _Scalar: ...
    def exterior_derivative(self) -> DiffFormParal: ...
    derivative = exterior_derivative
    @overload
    def wedge(self, other: DiffForm | DiffScalarField) -> DiffFormParal: ...
    @overload
    def wedge(self, other: FreeModuleAltForm) -> FreeModuleAltForm: ...
    @overload
    def interior_product(self, qvect: MultivectorFieldParal) -> DiffScalarField | MultivectorFieldParal: ...
    @overload
    def interior_product(self, qvect: MultivectorField | MultivectorFieldParal) -> _InteriorResult: ...
    @overload
    def interior_product(self, qvect: AlternatingContrTensor) -> AlternatingContrTensor | _Scalar: ...
