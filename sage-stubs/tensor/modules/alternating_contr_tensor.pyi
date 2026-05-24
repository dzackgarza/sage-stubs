from typing import TypeAlias

from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.tensor.modules.comp import CompFullyAntiSym, Components
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
from sage.tensor.modules.format_utilities import FormattedExpansion
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_tensor import FreeModuleTensor

_Scalar: TypeAlias = Element | Expression | Integer | int
_FormatSpec: TypeAlias = int | Integer

class AlternatingContrTensor(FreeModuleTensor):
    def __init__(
        self,
        fmodule: FiniteRankFreeModule,
        degree: int | Integer,
        name: str | None = ...,
        latex_name: str | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _new_instance(self) -> AlternatingContrTensor: ...
    def _new_comp(
        self, basis: FreeModuleBasis
    ) -> Components[_Scalar, _Scalar, _FormatSpec] | CompFullyAntiSym[_Scalar, _Scalar, _FormatSpec]: ...
    def degree(self) -> int | Integer: ...
    def display(self, basis: FreeModuleBasis | None = ..., format_spec: _FormatSpec | None = ...) -> FormattedExpansion: ...
    disp = display
    def wedge(self, other: AlternatingContrTensor) -> AlternatingContrTensor: ...
    def interior_product(self, form: FreeModuleAltForm) -> FreeModuleAltForm | _Scalar: ...
