from collections.abc import Iterator, Sequence
from typing import TypeAlias

from sage.rings.integer import Integer
from sage.tensor.modules.free_module_basis import Basis_abstract
from sage.tensor.modules.free_module_tensor import FreeModuleTensor
from sage.tensor.modules.tensor_free_module import TensorFreeModule

_Index: TypeAlias = int | Integer
_IndexTuple: TypeAlias = tuple[_Index, ...]
_Symbol: TypeAlias = str | Sequence[str]
_Indices: TypeAlias = Sequence[str] | None

class TensorFreeSubmoduleBasis_sym(Basis_abstract[_IndexTuple, FreeModuleTensor]):
    def __init__(
        self,
        tensor_module: TensorFreeModule,
        symbol: _Symbol,
        latex_symbol: _Symbol | None = ...,
        indices: _Indices = ...,
        latex_indices: _Indices = ...,
        symbol_dual: _Symbol | None = ...,
        latex_symbol_dual: _Symbol | None = ...,
    ) -> None: ...
    def _repr_(self) -> str: ...
    def keys(self) -> Iterator[_IndexTuple]: ...
    def values(self) -> Iterator[FreeModuleTensor]: ...
    def __getitem__(self, index: _IndexTuple) -> FreeModuleTensor: ...
