from collections.abc import Callable, Sequence

from sage.modules.free_module import FreeModule_generic, ModuleRank
from sage.modules.vector_double_dense import Vector_double_dense
from sage.rings.complex_double import ComplexDoubleElement
from sage.structure.parent import ElementConstructorInput


class Vector_complex_double_dense(Vector_double_dense[ComplexDoubleElement]):
    def __reduce__(
        self,
    ) -> tuple[
        Callable[
            [
                FreeModule_generic[ComplexDoubleElement],
                Sequence[ElementConstructorInput],
                ModuleRank,
                bool | None,
            ],
            Vector_complex_double_dense,
        ],
        tuple[
            FreeModule_generic[ComplexDoubleElement],
            list[ComplexDoubleElement],
            int,
            bool,
        ],
    ]: ...


def unpickle_v0(
    parent: FreeModule_generic[ComplexDoubleElement],
    entries: Sequence[ElementConstructorInput],
    degree: ModuleRank,
) -> Vector_complex_double_dense: ...
def unpickle_v1(
    parent: FreeModule_generic[ComplexDoubleElement],
    entries: Sequence[ElementConstructorInput],
    degree: ModuleRank,
    immutable: bool | None = ...,
) -> Vector_complex_double_dense: ...
