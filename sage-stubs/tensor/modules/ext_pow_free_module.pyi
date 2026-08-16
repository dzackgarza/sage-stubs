
from sage.rings.integer import Integer
from sage.structure.element import Element, Expression
from sage.tensor.modules.alternating_contr_tensor import AlternatingContrTensor
from sage.tensor.modules.finite_rank_free_module import (
    FiniteRankFreeModule,
    FiniteRankFreeModule_abstract,
)
from sage.tensor.modules.free_module_alt_form import FreeModuleAltForm
from sage.tensor.modules.free_module_basis import FreeModuleBasis

type _Scalar = Element | Expression | Integer | int
type _ComponentRows = (
    list[_Scalar] | list[list[_Scalar]] | list[list[list[_Scalar]]]
)
type _ComponentData = _Scalar | _ComponentRows

class ExtPowerFreeModule(FiniteRankFreeModule_abstract):
    Element: type[AlternatingContrTensor]

    def __init__(
        self,
        fmodule: FiniteRankFreeModule | CommutativeRing,
        degree: int | Integer,
        name: str | _Name | None = ...,
        latex_name: str | _Name | None = ...,
    ) -> None: ...
    def construction(self) -> None: ...
    def _element_constructor_(
        self,
        comp: _ComponentData = ...,
        basis: FreeModuleBasis | None = ...,
        name: str | None = ...,
        latex_name: str | None = ...,
    ) -> AlternatingContrTensor: ...
    def _an_element_(self) -> AlternatingContrTensor: ...
    def zero(self) -> AlternatingContrTensor: ...
    def _repr_(self) -> str: ...
    def base_module(self) -> FiniteRankFreeModule: ...
    def degree(self) -> Integer: ...

class ExtPowerDualFreeModule(FiniteRankFreeModule_abstract):
    Element: type[FreeModuleAltForm]
