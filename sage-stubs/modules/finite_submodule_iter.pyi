from collections.abc import Iterator
from typing import Generic, TypeVar

from sage.modules.free_module import FreeModule_generic, FreeModule_submodule
from sage.rings.integer import Integer
from sage.structure.element import RingElement

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class FiniteSubmoduleIterator(
    Iterator[FreeModule_submodule[_Scalar]],
    Generic[_Scalar],
):
    def __init__(
        self,
        module: FreeModule_generic[_Scalar],
        dimension: int | Integer | None = ...,
    ) -> None: ...
    def __iter__(self) -> FiniteSubmoduleIterator[_Scalar]: ...
    def __next__(self) -> FreeModule_submodule[_Scalar]: ...


def finite_submodules(
    module: FreeModule_generic[_Scalar],
    dimension: int | Integer | None = ...,
) -> FiniteSubmoduleIterator[_Scalar]: ...
