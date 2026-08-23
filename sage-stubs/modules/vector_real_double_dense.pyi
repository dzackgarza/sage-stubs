from collections.abc import Callable, Sequence

from sage.modules.free_module import FreeModule_generic, ModuleRank
from sage.modules.vector_double_dense import Vector_double_dense
from sage.rings.real_double import RealDoubleElement
from sage.structure.parent import ElementConstructorInput


class Vector_real_double_dense(Vector_double_dense[RealDoubleElement]):
    def stats_skew(self, bias: bool = ...) -> RealDoubleElement: ...
    def __reduce__(
        self,
    ) -> tuple[
        Callable[
            [
                FreeModule_generic[RealDoubleElement],
                Sequence[ElementConstructorInput],
                ModuleRank,
                bool | None,
            ],
            Vector_real_double_dense,
        ],
        tuple[
            FreeModule_generic[RealDoubleElement],
            list[RealDoubleElement],
            int,
            bool,
        ],
    ]: ...


def unpickle_v0(
    parent: FreeModule_generic[RealDoubleElement],
    entries: Sequence[ElementConstructorInput],
    degree: ModuleRank,
) -> Vector_real_double_dense: ...
def unpickle_v1(
    parent: FreeModule_generic[RealDoubleElement],
    entries: Sequence[ElementConstructorInput],
    degree: ModuleRank,
    immutable: bool | None = ...,
) -> Vector_real_double_dense: ...
