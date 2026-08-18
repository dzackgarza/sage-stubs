from collections.abc import Hashable
from typing import TypeVar

from sage.modules.free_module import FreeModule_submodule
from sage.modules.multi_filtered_vector_space import MultiFilteredVectorSpace_class
from sage.structure.element import FieldElement

_Scalar = TypeVar("_Scalar", bound=FieldElement)
_FiltrationIndex = TypeVar("_FiltrationIndex", bound=Hashable)


def diamond_cutting(
    filtrations: MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar],
) -> dict[tuple[int, ...], FreeModule_submodule[_Scalar]]: ...


def compatible_intersections(
    filtrations: MultiFilteredVectorSpace_class[_FiltrationIndex, _Scalar],
) -> tuple[FreeModule_submodule[_Scalar], ...]: ...
