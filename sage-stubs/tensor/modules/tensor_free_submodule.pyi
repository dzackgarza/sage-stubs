from collections.abc import Iterable, Sequence
from typing import TypeAlias

from sage.categories.morphism import Morphism
from sage.rings.integer import Integer
from sage.structure.category_object import CategoryObject
from sage.structure.element import Element, Expression
from sage.tensor.modules.comp import Components
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_tensor import FreeModuleTensor
from sage.tensor.modules.reflexive_module import ReflexiveModule_abstract
from sage.tensor.modules.tensor_free_module import TensorFreeModule

_Scalar: TypeAlias = Element | Expression | Integer | int
_FormatSpec: TypeAlias = int | Integer
_TensorType: TypeAlias = tuple[int, int]
_ComponentRows: TypeAlias = Sequence[_Scalar] | Sequence[Sequence[_Scalar]] | Sequence[Sequence[Sequence[_Scalar]]]
_ComponentData: TypeAlias = _Scalar | _ComponentRows | FreeModuleTensor
_IndexBlock: TypeAlias = Iterable[int | Integer]
_Symmetry: TypeAlias = _IndexBlock | Iterable[_IndexBlock] | None
class TensorFreeSubmodule_sym(TensorFreeModule):
    def __init__(
        self,
        fmodule: FiniteRankFreeModule,
        tensor_type: _TensorType | Sequence[int | Integer],
        name: str | None = ...,
        latex_name: str | None = ...,
        sym: _Symmetry = ...,
        antisym: _Symmetry = ...,
        *,
        category: CategoryObject | None = ...,
        ambient: ReflexiveModule_abstract | None = ...,
    ) -> None: ...
    def construction(self) -> None: ...
    def _basis_sym(self) -> Components[_Scalar, _Scalar, _FormatSpec]: ...
    def _repr_(self) -> str: ...
    def _is_symmetry_coarsening_of(
        self,
        coarser_comp: Components[_Scalar, _Scalar, _FormatSpec] | tuple[_Symmetry, _Symmetry],
        finer_comp: Components[_Scalar, _Scalar, _FormatSpec] | tuple[_Symmetry, _Symmetry],
    ) -> bool: ...
    def _element_constructor_(
        self,
        comp: _ComponentData = ...,
        basis: FreeModuleBasis | None = ...,
        name: str | None = ...,
        latex_name: str | None = ...,
        sym: _Symmetry = ...,
        antisym: _Symmetry = ...,
    ) -> FreeModuleTensor: ...
    def is_submodule(self, other: ReflexiveModule_abstract) -> bool: ...
    @property
    def lift(self) -> Morphism: ...
    @property
    def reduce(self) -> Morphism: ...
    @property
    def retract(self) -> Morphism: ...
