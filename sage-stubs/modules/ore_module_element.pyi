from collections.abc import Sequence
from typing import Generic, Literal, Never, TypeVar, overload

from sage.modules.free_module_element import (
    FreeModuleElement,
    FreeModuleElement_generic_dense,
)
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)

class OreModuleElement(
    FreeModuleElement_generic_dense[_Scalar],
    Generic[_Scalar],
):
    def parent(self) -> OreModule[_Scalar]: ...
    def _repr_(self) -> str: ...
    def _latex_(self) -> str: ...
    def is_mutable(self) -> bool: ...
    def __setitem__(
        self,
        i: int | slice,
        v: ElementConstructorInput | Sequence[ElementConstructorInput],
    ) -> Never: ...
    def __hash__(self) -> int: ...
    def vector(self) -> FreeModuleElement[_Scalar]: ...
    @overload
    def image(self, integral: Literal[True]) -> OreModuleElement[_Scalar]: ...
    @overload
    def image(
        self,
        integral: Literal[False] = ...,
    ) -> OreModuleElement[RingElement]: ...

from sage.modules.ore_module import OreModule
