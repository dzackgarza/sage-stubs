from collections.abc import Iterable, Sequence
from typing import TypeGuard, TypeVar

from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput, Parent

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


def is_FreeModule(x: object) -> TypeGuard[FreeModule_generic[RingElement]]: ...


def vector(
    ring: Parent[_Scalar],
    entries: Iterable[ElementConstructorInput],
    sparse: bool = ...,
) -> FreeModuleElement[_Scalar]: ...


def free_module_element(
    entries: Iterable[ElementConstructorInput],
    ring: Parent[_Scalar] | None = ...,
    sparse: bool = ...,
) -> FreeModuleElement[_Scalar]: ...


def span(
    vectors: Sequence[FreeModuleElement[_Scalar]],
    ring: Parent[_Scalar] | None = ...,
) -> FreeModule_submodule[_Scalar]: ...
