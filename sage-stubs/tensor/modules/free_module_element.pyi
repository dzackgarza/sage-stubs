from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.tensor.modules.alternating_contr_tensor import AlternatingContrTensor
from sage.tensor.modules.comp import CompFullyAntiSym, Components
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
from sage.tensor.modules.free_module_basis import FreeModuleBasis

type _Scalar = Element | Expression | Integer | int
type _FormatSpec = int | Integer
type _ComponentSet = Components[_Scalar, _Scalar, _FormatSpec]

class FiniteRankFreeModuleElement(AlternatingContrTensor):
    def __init__(
        self,
        fmodule: FiniteRankFreeModule,
        name: str | None = ...,
        latex_name: str | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def _new_comp(self, basis: FreeModuleBasis) -> _ComponentSet | CompFullyAntiSym[_Scalar, _Scalar, _FormatSpec]: ...
    def _new_instance(self) -> FiniteRankFreeModuleElement: ...
