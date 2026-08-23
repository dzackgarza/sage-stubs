from typing import Generic, Self, TypeVar

import numpy as np
from numpy.typing import DTypeLike, NDArray

from sage.modules.free_module import FreeModule_generic
from sage.modules.free_module_element import FreeModuleElement
from sage.structure.element import RingElement
from sage.structure.parent import ElementConstructorInput

_Scalar = TypeVar("_Scalar", bound=RingElement, default=RingElement)


class Vector_numpy_dense(FreeModuleElement[_Scalar], Generic[_Scalar]):
    def __init__(
        self,
        parent: FreeModule_generic[_Scalar],
        entries: NDArray[np.generic] | ElementConstructorInput | None,
        coerce: bool = ...,
        copy: bool = ...,
    ) -> None: ...
    def __create_vector__(self) -> None: ...
    def __copy__(self, copy: bool = ...) -> Self: ...
    def __len__(self) -> int: ...
    def numpy(self, dtype: DTypeLike | None = ...) -> NDArray[np.generic]: ...
