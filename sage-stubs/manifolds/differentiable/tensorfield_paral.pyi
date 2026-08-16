from collections.abc import Iterable, Sequence
from typing import overload

from sage.manifolds.chart import Chart
from sage.manifolds.differentiable.diff_map import DiffMap
from sage.manifolds.differentiable.manifold import DifferentiableManifold
from sage.manifolds.differentiable.tensorfield import TensorField, TensorType
from sage.manifolds.differentiable.vectorfield_module import VectorFieldModule
from sage.manifolds.point import ManifoldPoint
from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.tensor.modules.comp import Components
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
from sage.tensor.modules.format_utilities import FormattedExpansion
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_tensor import FreeModuleTensor

type _Index = int | Integer
type _IndexBlock = Iterable[_Index]
type _Symmetry = _IndexBlock | Iterable[_IndexBlock] | None
type _Scalar = Element | Expression | Integer | int
type _Components = Components[_Scalar, _Scalar, int | Integer]
type _TensorArgument = TensorField | FreeModuleTensor
type _DisplayArgument = (
    FreeModuleBasis | Chart | int | Integer | str | list[str] | None
)

class TensorFieldParal(FreeModuleTensor, TensorField):
    def __init__(
        self,
        vector_field_module: VectorFieldModule | FiniteRankFreeModule,
        tensor_type: TensorType | _TensorType | Sequence[int | Integer],
        name: str | None = None,
        latex_name: str | None = None,
        sym: _Symmetry = None,
        antisym: _Symmetry = None,
    ) -> None: ...
    def set_comp(
        self, basis: FreeModuleBasis | _BasisArg | None = None
    ) -> _Components: ...
    def add_comp(
        self, basis: FreeModuleBasis | _BasisArg | None = None
    ) -> _Components: ...
    def comp(
        self,
        basis: FreeModuleBasis | _BasisArg | None = None,
        from_basis: FreeModuleBasis | _BasisArg | None = None,
    ) -> Components: ...
    def base_module(self) -> FiniteRankFreeModule: ...
    def tensor_type(self) -> tuple[int | Integer, int | Integer]: ...
    def tensor_rank(self) -> int | Integer: ...
    def copy_from(self, other: TensorField | FreeModuleTensor) -> None: ...
    def copy(
        self, name: str | None = None, latex_name: str | None = None
    ) -> TensorFieldParal: ...
    def __pos__(self) -> TensorFieldParal: ...
    def __neg__(self) -> TensorFieldParal: ...
    def __truediv__(self, other: _Scalar) -> TensorFieldParal: ...
    def display(
        self, *args: _DisplayArgument, **kwds: _DisplayArgument | bool
    ) -> FormattedExpansion: ...
    def disp(
        self, *args: _DisplayArgument, **kwds: _DisplayArgument | bool
    ) -> FormattedExpansion: ...
    def lie_derivative(self, vector: TensorField) -> TensorFieldParal: ...
    lie_der = lie_derivative

    def restrict(
        self, subdomain: DifferentiableManifold, dest_map: DiffMap | None = None
    ) -> TensorFieldParal: ...
    def __call__(self, *args: _TensorArgument) -> TensorFieldParal | _Scalar: ...
    def contract(
        self, *args: int | Integer | TensorField | FreeModuleTensor
    ) -> TensorFieldParal: ...
    def symmetrize(
        self, *pos: int | Integer, basis: FreeModuleBasis | None = None
    ) -> TensorFieldParal: ...
    def antisymmetrize(
        self, *pos: int | Integer, basis: FreeModuleBasis | None = None
    ) -> TensorFieldParal: ...
    @overload
    def __mul__(self, other: TensorField) -> TensorFieldParal: ...
    @overload
    def __mul__(self, other: _Scalar | FreeModuleTensor) -> TensorFieldParal: ...
    @overload
    def display_comp(
        self,
        frame: FreeModuleBasis | None = None,
        chart: Chart | None = None,
        coordinate_labels: bool = True,
        only_nonzero: bool = True,
        only_nonredundant: bool = False,
    ) -> FormattedExpansion: ...
    @overload
    def display_comp(
        self,
        basis: FreeModuleBasis | _BasisArg | None = None,
        format_spec: int | Integer | _FormatSpec | Chart | None = None,
        symbol: str | bool | None = None,
        latex_symbol: str | bool | None = None,
        index_labels: list[str] | bool | None = None,
        index_latex_labels: list[str] | None = None,
        only_nonzero: bool = True,
        only_nonredundant: bool = False,
    ) -> FormattedExpansion: ...
    def at(self, point: ManifoldPoint) -> FreeModuleTensor: ...
    def along(self, mapping: DiffMap) -> TensorFieldParal: ...
    def series_expansion(
        self, symbol: Expression, order: int
    ) -> list[TensorFieldParal]: ...
    def truncate(self, symbol: Expression, order: int) -> TensorFieldParal: ...
    def set_calc_order(
        self, symbol: Expression, order: int, truncate: bool = False
    ) -> None: ...
