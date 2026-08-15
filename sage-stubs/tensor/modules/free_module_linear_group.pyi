from collections.abc import Sequence

from sage.matrix.matrix2 import Matrix
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.tensor.modules.finite_rank_free_module import FiniteRankFreeModule
from sage.tensor.modules.free_module_automorphism import FreeModuleAutomorphism
from sage.tensor.modules.free_module_basis import FreeModuleBasis
from sage.tensor.modules.free_module_morphism import FiniteRankFreeModuleMorphism
from sage.tensor.modules.free_module_tensor import FreeModuleTensor

type _MatrixLike = Matrix | Sequence[Sequence[Element | int]]

class FreeModuleLinearGroup(UniqueRepresentation, Parent):
    Element: type[FreeModuleAutomorphism]

    def __init__(self, fmodule: FiniteRankFreeModule) -> None: ...
    def _element_constructor_(
        self,
        comp: _MatrixLike | FreeModuleTensor | FiniteRankFreeModuleMorphism | int = ...,
        basis: FreeModuleBasis | None = ...,
        name: str | None = ...,
        latex_name: str | None = ...,
    ) -> FreeModuleAutomorphism: ...
    def _an_element_(self) -> FreeModuleAutomorphism: ...
    def one(self) -> FreeModuleAutomorphism: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def base_module(self) -> FiniteRankFreeModule: ...
