from collections.abc import Iterable, Sequence

from sage.rings.integer import Integer
from sage.structure.category_object import CategoryObject
from sage.structure.element import Element, Expression
from sage.tensor.modules.comp import Components
from sage.tensor.modules.finite_rank_free_module import (
    FiniteRankFreeModule,
    FiniteRankFreeModule_abstract,
)
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm
from sage.tensor.modules.free_module_automorphism import FreeModuleAutomorphism
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_element import FiniteRankFreeModuleElement
from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleMorphism
from sage.tensor.modules.free_module_tensor import FreeModuleTensor
from sage.tensor.modules.reflexive_module import (
    ReflexiveModule_abstract,
    ReflexiveModule_tensor,
)
from sage.tensor.modules.tensor_free_submodule_basis import TensorFreeSubmoduleBasis_sym

type _Scalar = Element | Expression | Integer | int
type _FormatSpec = int | Integer
type _TensorType = tuple[int, int]
type _ComponentRows = (
    Sequence[_Scalar]
    | Sequence[Sequence[_Scalar]]
    | Sequence[Sequence[Sequence[_Scalar]]]
)
type _ComponentData = (
    _Scalar
    | _ComponentRows
    | FreeModuleTensor
    | FreeModuleAltForm
    | FreeModuleAutomorphism
    | FiniteRankFreeModuleMorphism
)
type _IndexBlock = Iterable[int | Integer]
type _Symmetry = _IndexBlock | Iterable[_IndexBlock] | None
type _BasisSymbol = str | Sequence[str]
type _BasisIndices = Sequence[str] | None

class TensorFreeModule(ReflexiveModule_tensor, FiniteRankFreeModule_abstract):
    Element: type[FreeModuleTensor]

    def __init__(
        self,
        fmodule: FiniteRankFreeModule | CommutativeRing,
        tensor_type: _TensorType | Sequence[int | Integer] | int | Integer,
        name: str | _Name | None = ...,
        latex_name: str | _Name | None = ...,
        category: CategoryObject | None = ...,
    ) -> None: ...
    def _element_constructor_(
        self,
        comp: _ComponentData = ...,
        basis: FreeModuleBasis | None = ...,
        name: str | None = ...,
        latex_name: str | None = ...,
        sym: _Symmetry = ...,
        antisym: _Symmetry = ...,
    ) -> FreeModuleTensor: ...
    def zero(self) -> FreeModuleTensor: ...
    def _an_element_(self) -> FreeModuleTensor: ...
    def _coerce_map_from_(self, other: ReflexiveModule_abstract) -> bool: ...
    def _repr_(self) -> str: ...
    def base_module(self) -> FiniteRankFreeModule: ...
    def tensor_type(self) -> tuple[int, int]: ...
    def basis(
        self,
        symbol: _BasisSymbol,
        latex_symbol: _BasisSymbol | None = ...,
        from_family: Sequence[FiniteRankFreeModuleElement] | None = ...,
        indices: _BasisIndices = ...,
        latex_indices: _BasisIndices = ...,
        symbol_dual: _BasisSymbol | None = ...,
        latex_symbol_dual: _BasisSymbol | None = ...,
    ) -> TensorFreeSubmoduleBasis_sym: ...
    def _basis_sym(self) -> Components[_Scalar, _Scalar, _FormatSpec]: ...
