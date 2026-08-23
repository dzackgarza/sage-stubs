from collections.abc import Iterator, Sequence
from typing import Generic, Self, TypeVar

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.rings.integer import Integer
from sage.structure.element import ModuleElement, RingElement

_Element = TypeVar("_Element", bound=ModuleElement, default=ModuleElement)
_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class FiniteZZsubmodule_iterator(
    Iterator[_Element],
    Generic[_Element],
):
    def __init__(
        self,
        basis: Sequence[_Element],
        order: Sequence[int | Integer] | None = ...,
        coset_rep: _Element | None = ...,
        immutable: bool = ...,
    ) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> _Element: ...

class FiniteFieldsubspace_iterator(
    FiniteZZsubmodule_iterator[FreeModuleElement[_Scalar]],
    Generic[_Scalar],
):
    def __init__(
        self,
        basis: Sequence[FreeModuleElement[_Scalar]] | Matrix[_Scalar],
        coset_rep: FreeModuleElement[_Scalar] | None = ...,
        immutable: bool = ...,
    ) -> None: ...

class FiniteFieldsubspace_projPoint_iterator(
    Iterator[FreeModuleElement[_Scalar]],
    Generic[_Scalar],
):
    def __init__(
        self,
        basis: Sequence[FreeModuleElement[_Scalar]] | Matrix[_Scalar],
        normalize: bool = ...,
        immutable: bool = ...,
    ) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> FreeModuleElement[_Scalar]: ...
