from typing import Self

from sage.modules.vector_symbolic_dense import Vector_symbolic_dense
from sage.structure.parent import ElementConstructorInput


class Vector_callable_symbolic_dense(Vector_symbolic_dense):
    def arguments(self) -> tuple[object, ...]: ...
    def __call__(
        self,
        *args: ElementConstructorInput,
        **kwds: ElementConstructorInput,
    ) -> Vector_symbolic_dense: ...
    def function(self, *args: object) -> Self: ...
