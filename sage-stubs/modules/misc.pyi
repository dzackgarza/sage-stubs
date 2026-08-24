from collections.abc import Sequence
from typing import TypeVar

from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement

_InputScalar = TypeVar("_InputScalar", bound=RingElement)


def gram_schmidt(
    B: Sequence[FreeModuleElement[_InputScalar]],
) -> tuple[
    Sequence[FreeModuleElement[RingElement]],
    Matrix[RingElement],
]: ...
