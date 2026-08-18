from collections.abc import Iterable
from typing import Generic, TypeVar

from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import ModuleElement, RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)
_Element = TypeVar("_Element", bound=ModuleElement, default=ModuleElement)


class Module(Parent[_Element], Generic[_Scalar, _Element]):
    Element: type[_Element]
    def __init__(
        self,
        base_ring: Parent[_Scalar],
        category: object | None = ...,
    ) -> None: ...
    def base_ring(self) -> Parent[_Scalar]: ...
    def zero(self) -> _Element: ...
    def an_element(self) -> _Element: ...
    def _element_constructor_(
        self,
        x: ElementConstructorInput,
    ) -> _Element: ...
    def submodule(
        self,
        generators: Iterable[_Element],
        **kwds: object,
    ) -> Module[_Scalar, _Element]: ...
    def quotient(
        self,
        submodule: Module[_Scalar, _Element],
        **kwds: object,
    ) -> Module[_Scalar, _Element]: ...
    def tensor_product(
        self,
        other: Module[_Scalar, ModuleElement],
    ) -> Module[_Scalar, ModuleElement]: ...
    def direct_sum(
        self,
        other: Module[_Scalar, ModuleElement],
    ) -> Module[_Scalar, ModuleElement]: ...
